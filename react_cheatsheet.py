"""
Usage: python3 react_cheatsheet.py

"""
from cheatsheet import File, Group, make_cheatsheet


################
# constants
################
DEFINITELY_BASE_URL = "https://github.com/DefinitelyTyped/DefinitelyTyped/tree"
DEFINITELY_RAW_BASE_URL = (
    "https://raw.githubusercontent.com/DefinitelyTyped/DefinitelyTyped"
)
OUTPUT_TEMPLATE = "dist/react/{cheatsheet_version}.html"
PUBLISH_BASE_URL = "/typescript-react-cheat-sheet"
DEFINITELY_VERSION = "480aadc"
VERSIONS = [
    {
        "cheatsheet": DEFINITELY_VERSION,
        "react": DEFINITELY_VERSION,
        "react-dom": DEFINITELY_VERSION,
        "react-native": DEFINITELY_VERSION,
    }
]
GROUPS = [
    Group(
        "React",
        "react",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react/index.d.ts", "react")],
    ),
    Group(
        "React DOM",
        "react-dom",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react-dom/index.d.ts", "react-dom")],
    ),
    Group(
        "React Native",
        "react-native",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react-native/index.d.ts", "react-native")],
    ),
]
BUILTINS = []


# TODO: in middle of converting react_cheatsheet.py


def write_introduction_paragraph(fout, cheatsheet_version):
    INTRODUCTON_LINES = [
        "<p>\n",
        '<a href="https://www.typescriptlang.org/">TypeScript</a> \n',
        "is a typed superset of JavaScript that compiles to plain JavaScript. \n",
        "This is a list of TypeScript types generated from the declaration files for \n",
        "<code>react</code>, ",
        "<code>react-dom</code>, and ",
        "<code>react-native</code> in \n",
        f'<a href="{DEFINITELY_BASE_URL}/{cheatsheet_version}">',
        f"{DEFINITELY_BASE_URL}/{cheatsheet_version}</a>. \n",
        "The script to generate this list is \n",
        '<a href="https://github.com/saltycrane/typescript-cheatsheet">on github</a>.\n',
        "Fixes welcome.\n",
        "See also my\n",
        '<a href="/typescript-cheat-sheet/latest/">TypeScript cheat sheet</a>,\n',
        'and <a href="/blog/2017/08/docker-cheat-sheet/">Docker cheat sheet</a>.\n',
        "</p>\n\n",
    ]
    for line in INTRODUCTON_LINES:
        fout.write(line)


def write_list_of_versions(fout, this_version):
    pass


def main():
    make_cheatsheet(
        OUTPUT_TEMPLATE,
        PUBLISH_BASE_URL,
        VERSIONS,
        GROUPS,
        BUILTINS,
        write_introduction_paragraph,
        write_list_of_versions,
    )


if __name__ == "__main__":
    main()
