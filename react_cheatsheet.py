"""
Usage: python3 react_cheatsheet.py

"""
from cheatsheet import File, make_cheatsheet


################
# constants
################
OUTPUT_TEMPLATE = "dist/react/{version}.html"
GITHUB_BASE_URL = "https://github.com/DefinitelyTyped/DefinitelyTyped/tree"
GITHUB_RAW_BASE_URL = (
    "https://raw.githubusercontent.com/DefinitelyTyped/DefinitelyTyped"
)
PUBLISH_BASE_URL = "/typescript-react-cheat-sheet"
VERSIONS = ["cad160cba6d54462be720e0c93e8607d01a4a2d0"]
FILES = [
    File("types/react/index.d.ts", "React"),
    File("types/react-dom/index.d.ts", "React DOM"),
    File("types/react-native/index.d.ts", "React Native"),
]
BUILTINS = []


def write_introduction_paragraph(fout, version):
    INTRODUCTON_LINES = [
        "<p>\n",
        '<a href="https://www.typescriptlang.org/">TypeScript</a> \n',
        "is a typed superset of JavaScript that compiles to plain JavaScript. \n",
        "This is a list of TypeScript types generated from the declaration files for \n",
        "<code>react</code>, ",
        "<code>react-dom</code>, and ",
        "<code>react-native</code> in \n",
        f'<a href="{GITHUB_BASE_URL}/{version}">{GITHUB_BASE_URL}/{version[0:7]}</a>. \n',
        "The script to generate this list is \n",
        '<a href="https://github.com/saltycrane/typescript-cheatsheet">on github</a>.\n',
        "Fixes welcome.\n",
        "See also my\n",
        '<a href="/typescript-cheat-sheet/latest/">TypeScript cheat sheet</a>,\n',
        '<a href="/flow-type-cheat-sheet/latest/">Flow type cheat sheet</a>,\n',
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
        GITHUB_BASE_URL,
        GITHUB_RAW_BASE_URL,
        PUBLISH_BASE_URL,
        VERSIONS,
        FILES,
        BUILTINS,
        write_introduction_paragraph,
        write_list_of_versions,
    )


if __name__ == "__main__":
    main()
