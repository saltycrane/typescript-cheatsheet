"""
Usage: python3 typescript_cheatsheet.py

"""
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
TypeResult = namedtuple(
    'TypeResult', ['version', 'filepath', 'name', 'type', 'line_no', 'members'])


################
# constants
################
GITHUB_BASE_URL = 'https://github.com/Microsoft/TypeScript/tree'
GITHUB_RAW_BASE_URL = 'https://raw.githubusercontent.com/Microsoft/TypeScript'
PUBLISH_BASE_URL = '/typescript-cheat-sheet'
VERSIONS = [
    'v3.2.4',
]
FILES = [
    File('lib/lib.dom.d.ts', 'DOM'),
    File('lib/lib.dom.iterable.d.ts', 'DOM Iterable'),
    File('lib/lib.es5.d.ts', 'ES5'),
    File('lib/lib.es2015.collection.d.ts', 'ES2015 Collection'),
    File('lib/lib.es2015.core.d.ts', 'ES2015 Core'),
    File('lib/lib.es2015.generator.d.ts', 'ES2015 Generator'),
    File('lib/lib.es2015.iterable.d.ts', 'ES2015 Iterable'),
    File('lib/lib.es2015.promise.d.ts', 'ES2015 Promise'),
    File('lib/lib.es2015.proxy.d.ts', 'ES2015 Proxy'),
    File('lib/lib.es2015.reflect.d.ts', 'ES2015 Reflect'),
    File('lib/lib.es2015.symbol.d.ts', 'ES2015 Symbol'),
    File('lib/lib.es2015.symbol.wellknown.d.ts', 'ES2015 Symbol Well Known'),
    File('lib/lib.es2016.array.include.d.ts', 'ES2016 Array Include'),
    File('lib/lib.es2017.intl.d.ts', 'ES2017 Intl'),
    File('lib/lib.es2017.object.d.ts', 'ES2017 Object'),
    File('lib/lib.es2017.sharedmemory.d.ts', 'ES2017 Shared Memory'),
    File('lib/lib.es2017.string.d.ts', 'ES2017 String'),
    File('lib/lib.es2017.typedarrays.d.ts', 'ES2017 Typed Arrays'),
    File('lib/lib.es2018.intl.d.ts', 'ES2018 Intl'),
    File('lib/lib.es2018.promise.d.ts', 'ES2018 Promise'),
    File('lib/lib.es2018.regexp.d.ts', 'ES2018 Regexp'),
    File('lib/lib.esnext.array.d.ts', 'ESNext Array'),
    File('lib/lib.esnext.asynciterable.d.ts', 'ESNext Async Iterable'),
    File('lib/lib.esnext.bigint.d.ts', 'ESNext Big Int'),
    File('lib/lib.esnext.intl.d.ts', 'ESNext Intl'),
    File('lib/lib.esnext.symbol.d.ts', 'ESNext Symbol'),
    File('lib/lib.scripthost.d.ts', 'Script Host'),
    File('lib/lib.webworker.d.ts', 'Web Worker'),
    File('lib/lib.webworker.importscripts.d.ts', 'Web Worker Import Scripts'),
]

BUILTINS = [
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#abstract-classes"><code>abstract</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#any"><code>any</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#array"><code>Array</code> (<code>[]</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#type-assertions"><code>as</code> (type assertions)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#boolean"><code>boolean</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#class-types">Class types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html">Classes</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#conditional-types">Conditional types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#discriminated-unions">Discriminated unions</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/enums.html"><code>enum</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#predefined-conditional-types"><code>Exclude&lt;T, U&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#extending-interfaces"><code>extends</code> (w/ interfaces)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#predefined-conditional-types"><code>Extract&lt;T, U&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#function-types">Function types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/functions.html">Functions</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/generics.html">Generics (<code>&lt;&gt;</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#hybrid-types">Hybrid types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types"><code>in</code> operator</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#index-types">Index types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#indexable-types">Indexable types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-inference-in-conditional-types"><code>infer</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#instanceof-type-guards"><code>instanceof</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#predefined-conditional-types"><code>InstanceType&lt;T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html"><code>interface</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types">Intersection types (<code>&amp;</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#user-defined-type-guards"><code>is</code> (type predicate)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#index-types"><code>keyof</code> index type query operator</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types">Mapped types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#never"><code>never</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#predefined-conditional-types"><code>NonNullable&lt;T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#null-and-undefined"><code>null</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#number"><code>number</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#numeric-literal-types">Numeric literal types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#object"><code>object</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#optional-properties">Optional properties (<code>?</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#understanding-private"><code>private</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#understanding-protected"><code>protected</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#public-private-and-protected-modifiers"><code>public</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#readonly-modifier"><code>readonly</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#readonly-properties"><code>readonly</code> (w/ interfaces)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#predefined-conditional-types"><code>ReturnType&lt;T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#enum-member-types">Singleton types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#string"><code>string</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#string-literal-types">String literal types</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#tuple">Tuples</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-aliases"><code>type</code> aliases</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#type-assertions">Type assertions (<code>&lt;&gt;</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#typeof-type-guards"><code>typeof</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#null-and-undefined"><code>undefined</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#union-types">Union types (<code>|</code> syntax)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#new-unknown-top-type"><code>unknown</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/basic-types.html#void"><code>void</code></a></li>',
]


################
# main
################
def main():
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
    for line_index, line in enumerate(body.splitlines()):
        def match_and_append(pattern, type):
            match = re.search(pattern, line)
            if match:
                result = TypeResult(
                    version, filepath, match.group('name'), type, line_index + 1, None)
                type_results.append(result)

        match_and_append(r'^\s*interface\s+(?P<name>\w+\<.*\>).*{', 'interface')
        match_and_append(r'^\s*interface\s+(?P<name>\w+)[^<]*{', 'interface')
        match_and_append(r'^\s*type\s+(?P<name>.+)\s+=', 'type')
        match_and_append(r'^\s*declare\s+var\s+(?P<name>.+)\s*:', 'var')
        match_and_append(r'^\s*declare\s+const\s+(?P<name>.+)\s*:', 'const')
        match_and_append(r'^\s*declare\s+function\s+(?P<name>\w+\<.*\>)\(', 'function')
        match_and_append(r'^\s*declare\s+function\s+(?P<name>\w+)[^<]*\(', 'function')
        match_and_append(r'^\s*declare\s+namespace\s+(?P<name>.+)\s*{', 'namespace')

    print('Count:', len(type_results))
    return type_results


def post_process(type_results):
    """sort and clean the results
    """
    def transform_result(type_result):
        version, filepath, name, type, line_no, members = type_result
        return TypeResult(version, filepath, name, type, line_no, members)

    type_results = [transform_result(result) for result in type_results]
    type_results = sorted(type_results, key=lambda result: result.type)
    type_results = sorted(type_results, key=lambda result: result.name.lower())
    return type_results


################
# write_output
################
def write_output(file_results, version):
    OUTPUT_FILE = f'dist/{version}.html'
    fout = open(OUTPUT_FILE, 'w')
    write_header(fout)
    write_introduction_paragraph(fout, version)
    write_list_of_versions(fout, version)
    write_table_of_contents(fout)
    write_builtins_panel(fout)
    write_panels_of_results(fout, file_results)
    write_footer(fout)
    fout.close()


def write_header(fout):
    # fout.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">\n\n')
    fout.write('{% extends "v2/typescript_cheatsheet/base.html" %}\n')
    fout.write('{% block cheatsheet %}\n\n')


def write_introduction_paragraph(fout, version):
    fout.write('<p>\n')
    fout.write('<a href="https://www.typescriptlang.org/">TypeScript</a> \n')
    fout.write('is a typed superset of JavaScript that compiles to plain JavaScript. \n')
    fout.write('This is a list of TypeScript types generated from the declaration files in \n')
    fout.write(f'<a href="{GITHUB_BASE_URL}/{version}/lib">{GITHUB_BASE_URL}/{version}/lib</a>. \n')
    fout.write('The script to generate this list is \n')
    fout.write('<a href="https://github.com/saltycrane/typescript-cheatsheet">on github</a>.\n')
    fout.write('Fixes welcome.\n')
    fout.write('See also my\n')
    fout.write('<a href="/flow-type-cheat-sheet/latest/">Flow type cheat sheet</a>\n')
    fout.write('and <a href="/blog/2017/08/docker-cheat-sheet/">Docker cheat sheet</a>.\n')
    fout.write('</p>\n\n')


def write_list_of_versions(fout, this_version):
    version_list = []
    for index, version in enumerate(VERSIONS):
        if index == 0:
            slug = 'latest'
        else:
            slug = version
        if version == this_version:
            version_list.append(
                f' <strong style="font-size: 120%">{version}</strong>')
        else:
            version_list.append(
                f' <a href="{PUBLISH_BASE_URL}/{slug}/">{version}</a>')

    version_string = ''.join(version_list)
    fout.write(f'<p>TypeScript version: {version_string}</p>\n\n')


def write_table_of_contents(fout):
    lines = ['<li><a href="#builtins">Built-ins</a></li>'] + [
        f'<li><a href="#{filepath}">{heading}</a></li>\n'
        for filepath, heading in FILES]
    write_panel_with_3_columns(
        fout,
        lines,
        '<h4 id="toc">Table of Contents</h4>',
    )


def write_builtins_panel(fout):
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


def write_footer(fout):
    fout.write('{% endblock %}\n')


def generate_output_lines(type_results):
    """generate html output lines to write for a list of results
    """
    output_lines = []
    for type_result in type_results:
        lines = generate_result(type_result)
        output_lines.extend(lines)
    return output_lines


# TODO: <ul> and <li> tags should not be added both here and in write_panel_with_3_columns()
def generate_result(type_result):
    """recursively generate html lines to write starting at a single result
    """
    lines = []
    version, filepath, name, type, line_no, members = type_result
    if members:
        link = generate_alink(version, filepath, line_no, name, type)
        lines.append('<li>{link}<ul>'.format(link=link))
        for child_result in members:
            child_lines = generate_result(child_result, version)
            lines.extend(child_lines)
        # mutate list so that <ul> tags don't count as items in the list when
        # grouping columns
        lines[-1] = '{last_line}</ul></li>'.format(last_line=lines[-1])
    else:
        link = generate_alink(version, filepath, line_no, name, type)
        lines.append('<li>{link}</li>'.format(link=link))
    return lines


def generate_alink(version, filepath, line_no, name, type):
    """return html for a single <a> link
    """
    github_url = f'{GITHUB_BASE_URL}/{version}/{filepath}#L{line_no}'
    name = html_escape(name)
    alink = f'<a href="{github_url}">{name}</a> <small>({type})</small>'
    return alink


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


if __name__ == '__main__':
    main()
