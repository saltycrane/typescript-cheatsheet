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
DEFINITELY_VERSION = "8201a5f"
VERSIONS = [
    {
        "cheatsheet": DEFINITELY_VERSION,
        "react": DEFINITELY_VERSION,
        "react-dom": DEFINITELY_VERSION,
        "react-dom/server": DEFINITELY_VERSION,
        "react-dom/test-utils": DEFINITELY_VERSION,
        "react-native": DEFINITELY_VERSION,
    }
]
GROUPS = [
    Group(
        "react",
        "react",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react/index.d.ts", "react", None)],
    ),
    Group(
        "react-dom",
        "react-dom",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react-dom/index.d.ts", "react-dom", None)],
    ),
    Group(
        "react-dom/server",
        "react-dom/server",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react-dom/server/index.d.ts", "react-dom-server", None)],
    ),
    Group(
        "react-dom/test-utils",
        "react-dom/test-utils",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [
            File(
                "types/react-dom/test-utils/index.d.ts",
                "react-dom-test-utils",
                None,
            )
        ],
    ),
    Group(
        "react-native",
        "react-native",
        DEFINITELY_BASE_URL,
        DEFINITELY_RAW_BASE_URL,
        [File("types/react-native/index.d.ts", "react-native", None)],
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
        "Fixes welcome.</p>\n",
        "<p>See also my\n",
        '<a href="/typescript-cheat-sheet/latest/">TypeScript cheat sheet</a>.\n',
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
