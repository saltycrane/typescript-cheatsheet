import math
import re
import urllib.request
from collections import namedtuple


################
# records
################
File = namedtuple('File', ['filepath', 'heading'])
FileResult = namedtuple(
    'FileResult', ['filepath', 'heading', 'type_results'])
LinkInfo = namedtuple('Variation', [
    'display',  # string
    'type',     # interface | type | var | const | function | namespace
    'filepath', # string
    'line_no',  # number
])
TypeResult = namedtuple(
    'TypeResult', [
        'version',    # string
        'name',       # string
        'variations', # LinkInfo[]
        'members',    # TypeResult[] | None
    ])


################
# globals
################
OUTPUT_TEMPLATE = ''
GITHUB_BASE_URL = ''
GITHUB_RAW_BASE_URL = ''
PUBLISH_BASE_URL = ''
VERSIONS = []
FILES = []
BUILTINS = []
INTRODUCTON_LINES = []
write_introduction_paragraph = None
write_list_of_versions = None


################
# main
################
def make_cheatsheet(
    output_template,
    github_base_url,
    github_raw_base_url,
    publish_base_url,
    versions,
    files,
    builtins,
    write_introduction_paragraph_func,
    write_list_of_versions_func,
):
    global OUTPUT_TEMPLATE
    global GITHUB_BASE_URL
    global GITHUB_RAW_BASE_URL
    global PUBLISH_BASE_URL
    global VERSIONS
    global FILES
    global BUILTINS
    global INTRODUCTON_LINES
    global write_introduction_paragraph
    global write_list_of_versions
    OUTPUT_TEMPLATE = output_template
    GITHUB_BASE_URL = github_base_url
    GITHUB_RAW_BASE_URL = github_raw_base_url
    PUBLISH_BASE_URL = publish_base_url
    VERSIONS = versions
    FILES = files
    BUILTINS = builtins
    write_introduction_paragraph = write_introduction_paragraph_func
    write_list_of_versions = write_list_of_versions_func

    for version in VERSIONS:
        file_results = get_file_results(version)
        write_output(file_results, version)


################
# get_file_results
################
def get_file_results(version):
    """get results for all files
    """
    file_results = []
    for filepath, heading in FILES:
        raw_url = f'{GITHUB_RAW_BASE_URL}/{version}/{filepath}'
        print('raw_url', raw_url)
        body = download_file(raw_url)
        type_results = parse_file(body, version, filepath)
        type_results = post_process(type_results)
        file_results.append(FileResult(filepath, heading, type_results))
    return file_results


def download_file(url):
    response = urllib.request.urlopen(url)
    body = response.read().decode('utf-8')
    return body


def parse_file(body, version, filepath):
    """extract types from the file using regular expressions
    """
    type_results = []
    indentation = ''
    namespace = None
    multiline = False
    for single_line_index, single_line in enumerate(body.splitlines()):

        # multi-line handling... if the line starts a type declaration but
        # finishes on a subsequent line, enter multiline state and start
        # concatenating lines until the final character is found.
        CHAR_DENOTING_END_OF_MULTILINE = {
            'declare class': '{',
            'type': '=',
        }

        # start of multi-line
        match = re.search(r'^\s*(declare class|type) .+', single_line)
        if match and CHAR_DENOTING_END_OF_MULTILINE[match.group(1)] not in single_line:
            multiline = True
            line_index = single_line_index
            line = single_line
            end_char = CHAR_DENOTING_END_OF_MULTILINE[match.group(1)]
            continue

        # in multiline state
        elif multiline:
            line = line + single_line
            # end of multiline
            if end_char in single_line:
                multiline = False
            # still in multiline state
            else:
                continue

        # not a multiline, treat as normal
        else:
            line_index = single_line_index
            line = single_line

        # start of a namespace
        match = re.search(
            r'^\s*(export\s+)?(declare\s+)?namespace\s+(?P<name>.+)\s*{', line)
        if match:
            indentation = r'\s+'
            namespace = TypeResult(
                version,
                match.group('name'),
                variations=[
                    LinkInfo(
                        match.group('name'),
                        'namespace',
                        filepath,
                        line_index + 1,
                    )
                ],
                members=[],
            )
            continue

        # end of a namespace
        match = re.search(r'^}', line)
        if match and namespace:
            print("Members count: ", len(namespace.members))
            indentation = ''
            type_results.append(namespace)
            namespace = None
            continue

        # choose whether to append matches to namespace.members or the
        # top-level results list
        if namespace:
            appender = namespace.members
        else:
            appender = type_results

        def add_result(pattern, type):
            match = re.search(pattern, line)
            if not match:
                return
            link_info = LinkInfo(
                match.group('name') + match.groupdict().get('sig', ''),
                type,
                filepath,
                line_index + 1,
            )
            existing_result = next(
                (x for x in appender if x.name == match.group('name')), None)
            if existing_result:
                existing_result.variations.append(link_info)
            else:
                appender.append(
                    TypeResult(
                        version,
                        match.group('name'),
                        variations=[link_info],
                        members=None,
                    )
                )

        # e.g. interface Element extends React.ReactElement<any, any> {
        add_result(r'^\s*(export\s+)?interface\s+(?P<name>\w+)(?P<sig>\s+extends\s+[^<]*\s*\<.*\>).*{', 'interface')
        # e.g. interface IntrinsicClassAttributes<T> extends React.ClassAttributes<T> {
        add_result(r'^\s*(export\s+)?interface\s+(?P<name>\w+)(?P<sig>\<.*\>).*{', 'interface')
        # e.g. interface IntrinsicElements {
        add_result(r'^\s*(export\s+)?interface\s+(?P<name>\w+)[^<]*{', 'interface')
        add_result(r'^\s*(export\s+)?type\s+(?P<name>[^=]+)\s+=', 'type')
        add_result(r'^\s*(export\s+)?(declare\s+)?var\s+(?P<name>[^:]+)\s*:', 'var')
        add_result(r'^\s*(export\s+)?(declare\s+)?const\s+(?P<name>[^:]+)\s*:', 'const')
        add_result(r'^\s*(export\s+)?(declare\s+)?function\s+(?P<name>\w+)(?P<sig>\<.*\>)\(', 'function')
        add_result(r'^\s*(export\s+)?(declare\s+)?function\s+(?P<name>\w+)[^<]*\(', 'function')

    print('Count:', len(type_results))
    return type_results


def post_process(type_results):
    """sort and clean the results
    """
    def transform_result(type_result):
        version, name, variations, members = type_result
        variations = sorted(variations, key=lambda x: len(x.display))
        variations = sorted(variations, key=lambda x: x.type)
        if members:
            members = post_process(members)
        return TypeResult(
            version,
            name,
            variations,
            members,
        )

    type_results = [transform_result(result) for result in type_results]
    type_results = sorted(type_results, key=lambda result: result.name.lower())
    return type_results


################
# write_output
################
def write_output(file_results, version):
    fout = open(OUTPUT_TEMPLATE.format(version=version), 'w')
    fout.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">\n\n')
    write_introduction_paragraph(fout, version)
    write_list_of_versions(fout, version)
    write_table_of_contents(fout)
    write_builtins_panel(fout)
    write_panels_of_results(fout, file_results)
    fout.close()


def write_table_of_contents(fout):
    if BUILTINS:
        lines = ['<li><a href="#builtins">Built-ins</a></li>']
    else:
        lines = []
    lines = lines + [
        f'<li><a href="#{filepath}">{heading}</a></li>\n'
        for filepath, heading in FILES]
    write_panel_with_3_columns(
        fout,
        lines,
        '<h4 id="toc">Table of Contents</h4>',
    )


def write_builtins_panel(fout):
    if not BUILTINS:
        return
    write_panel_with_3_columns(
        fout,
        BUILTINS,
        '<h4 id="builtins">Built-ins</h4>',
    )


def write_panels_of_results(fout, file_results):
    for filepath, heading, type_results in file_results:
        lines = generate_output_lines(type_results)
        write_panel_with_3_columns(
            fout,
            lines,
            f'<h4 id={filepath}>{heading}</h4>',
        )


def generate_output_lines(type_results):
    """generate html output lines to write for a list of results
    """
    output_lines = []
    for type_result in type_results:
        lines = generate_result(type_result)
        output_lines.extend(lines)
    return output_lines


# TODO: <ul> and <li> tags should not be added both here and in write_panel
# _with_3_columns()
def generate_result(type_result):
    """recursively generate html lines to write starting at a single result
    """
    lines = []
    version, name, variations, members = type_result
    if members:
        link = generate_alinks(version, variations)
        lines.append('<li>{link}<ul>'.format(link=link))
        for child_result in members:
            child_lines = generate_result(child_result)
            lines.extend(child_lines)
        # mutate list so that <ul> tags don't count as items in the list when
        # grouping columns
        lines[-1] = '{last_line}</ul></li>'.format(last_line=lines[-1])
    else:
        link = generate_alinks(version, variations)
        lines.append('<li>{link}</li>'.format(link=link))
    return lines


# TODO: try running again
def generate_alinks(version, variations):
    """return html for a single <a> link
    """
    alinks = []
    for display, type, filepath, line_no in variations:
        github_url = f'{GITHUB_BASE_URL}/{version}/{filepath}#L{line_no}'
        display = html_escape(display)
        alinks.append(
            f'<a href="{github_url}">{display}</a> <small>({type})</small>')
    return ' &#8729; '.join(alinks)


def write_panel_with_3_columns(fout, items, heading):
    """group items into 3 columns of ~equal length and write as bootstrap columns
    """
    N_COLUMNS = 3.0
    rows_per_col = int(math.ceil(len(items) / N_COLUMNS))
    grouped = []
    group = []
    row_count = 0

    for item in items:
        group.append(item)

        row_count += 1
        if row_count >= rows_per_col:
            grouped.append(group)
            group = []
            row_count = 0

    if group:
        grouped.append(group)

    # start bootstrap panel
    fout.write('<div class="panel panel-default">\n')
    fout.write(f'<div class="panel-heading">{heading}</div>\n')
    fout.write('<div class="panel-body">\n')
    fout.write('<div class="row">\n')

    # start bootstrap columns
    ul_tag_count = 0
    for group in grouped:
        extra_ul_tags = '<ul>' * ul_tag_count
        fout.write('<div class="col-sm-4"><ul>' + extra_ul_tags + '\n')
        for line in group:
            if '<ul>' in line:
                ul_tag_count += 1
            if '</ul>' in line:
                ul_tag_count -= 1
            fout.write(line + '\n')
        extra_ul_tags = '</ul>' * ul_tag_count
        fout.write(extra_ul_tags + '</ul></div>\n')
    # end bootstrap columns

    fout.write('</div></div></div>\n')
    # end bootstrap panel


def html_escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text
