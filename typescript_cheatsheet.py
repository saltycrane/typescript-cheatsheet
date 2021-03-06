"""
Usage: python3 typescript_cheatsheet.py

"""
from cheatsheet import File, Group, Version, make_cheatsheet


################
# constants
################
TYPESCRIPT_BASE_URL = "https://github.com/Microsoft/TypeScript/tree"
TYPESCRIPT_RAW_BASE_URL = (
    "https://raw.githubusercontent.com/Microsoft/TypeScript"
)
OUTPUT_TEMPLATE = "dist/typescript/{cheatsheet_version}.html"
PUBLISH_BASE_URL = "/typescript-cheat-sheet"
DEFINITELY_VERSION = "8201a5f"

VERSIONS = [
    {
        "cheatsheet": "v3.3.4000",
        "es": "v3.3.4000",
        "dom": "v3.3.4000",
        "scripthost": "v3.3.4000",
        "webworker": "v3.3.4000",
        "node": DEFINITELY_VERSION,
    },
    {
        "cheatsheet": "v3.2.4",
        "es": "v3.2.4",
        "dom": "v3.2.4",
        "scripthost": "v3.2.4",
        "webworker": "v3.2.4",
        "node": DEFINITELY_VERSION,
    },
    {
        "cheatsheet": "v3.1.6",
        "es": "v3.1.6",
        "dom": "v3.1.6",
        "scripthost": "v3.1.6",
        "webworker": "v3.1.6",
        "node": DEFINITELY_VERSION,
    },
]

GROUPS = [
    Group(
        "ES5, ES2015-ES2019, ESNext",
        "es",
        TYPESCRIPT_BASE_URL,
        TYPESCRIPT_RAW_BASE_URL,
        [
            File("lib/lib.es5.d.ts", "es5", None),
            File("lib/lib.es2015.collection.d.ts", "es2015.collection", None),
            File("lib/lib.es2015.core.d.ts", "es2015.core", None),
            File("lib/lib.es2015.generator.d.ts", "es2015.generator", None),
            File("lib/lib.es2015.iterable.d.ts", "es2015.iterable", None),
            File("lib/lib.es2015.promise.d.ts", "es2015.promise", None),
            File("lib/lib.es2015.proxy.d.ts", "es2015.proxy", None),
            File("lib/lib.es2015.reflect.d.ts", "es2015.reflect", None),
            File("lib/lib.es2015.symbol.d.ts", "es2015.symbol", None),
            File(
                "lib/lib.es2015.symbol.wellknown.d.ts",
                "es2015.symbol.wellknown",
                None,
            ),
            File(
                "lib/lib.es2016.array.include.d.ts",
                "es2016.array.include",
                None,
            ),
            File("lib/lib.es2017.intl.d.ts", "es2017.intl", None),
            File("lib/lib.es2017.object.d.ts", "es2017.object", None),
            File(
                "lib/lib.es2017.sharedmemory.d.ts", "es2017.sharedmemory", None
            ),
            File("lib/lib.es2017.string.d.ts", "es2017.string", None),
            File("lib/lib.es2017.typedarrays.d.ts", "es2017.typedarrays", None),
            File("lib/lib.es2018.intl.d.ts", "es2018.intl", None),
            File("lib/lib.es2018.promise.d.ts", "es2018.promise", None),
            File("lib/lib.es2018.regexp.d.ts", "es2018.regexp", None),
            File(
                "lib/lib.es2019.array.d.ts", "es2019.array", Version(3, 3, 4000)
            ),
            File(
                "lib/lib.es2019.string.d.ts",
                "es2019.string",
                Version(3, 3, 4000),
            ),
            File(
                "lib/lib.es2019.symbol.d.ts",
                "es2019.symbol",
                Version(3, 3, 4000),
            ),
            File("lib/lib.esnext.array.d.ts", "esnext.array", None),
            File(
                "lib/lib.esnext.asynciterable.d.ts",
                "esnext.asynciterable",
                None,
            ),
            File(
                "lib/lib.esnext.bigint.d.ts", "esnext.bigint", Version(3, 2, 4)
            ),
            File("lib/lib.esnext.intl.d.ts", "esnext.intl", None),
            File("lib/lib.esnext.symbol.d.ts", "esnext.symbol", None),
        ],
    ),
    Group(
        "DOM",
        "dom",
        TYPESCRIPT_BASE_URL,
        TYPESCRIPT_RAW_BASE_URL,
        [
            File("lib/lib.dom.d.ts", "dom", None),
            File("lib/lib.dom.iterable.d.ts", "dom.iterable", None),
        ],
    ),
    Group(
        "Script Host",
        "scripthost",
        TYPESCRIPT_BASE_URL,
        TYPESCRIPT_RAW_BASE_URL,
        [File("lib/lib.scripthost.d.ts", None, None)],
    ),
    Group(
        "Web Worker",
        "webworker",
        TYPESCRIPT_BASE_URL,
        TYPESCRIPT_RAW_BASE_URL,
        [
            File("lib/lib.webworker.d.ts", "webworker", None),
            File(
                "lib/lib.webworker.importscripts.d.ts",
                "webworker.importscripts",
                None,
            ),
        ],
    ),
    Group(
        "Node.js",
        "node",
        "https://github.com/DefinitelyTyped/DefinitelyTyped/tree",
        "https://raw.githubusercontent.com/DefinitelyTyped/DefinitelyTyped",
        [
            File("types/node/assert.d.ts", None, None),
            File("types/node/async_hooks.d.ts", None, None),
            File("types/node/buffer.d.ts", None, None),
            File("types/node/child_process.d.ts", None, None),
            File("types/node/cluster.d.ts", None, None),
            File("types/node/console.d.ts", None, None),
            File("types/node/constants.d.ts", None, None),
            File("types/node/crypto.d.ts", None, None),
            File("types/node/dgram.d.ts", None, None),
            File("types/node/dns.d.ts", None, None),
            File("types/node/domain.d.ts", None, None),
            File("types/node/events.d.ts", None, None),
            File("types/node/fs.d.ts", None, None),
            File("types/node/globals.d.ts", None, None),
            File("types/node/http.d.ts", None, None),
            File("types/node/http2.d.ts", None, None),
            File("types/node/https.d.ts", None, None),
            File("types/node/index.d.ts", None, None),
            File("types/node/inspector.d.ts", None, None),
            File("types/node/module.d.ts", None, None),
            File("types/node/net.d.ts", None, None),
            File("types/node/node-tests.ts", None, None),
            File("types/node/os.d.ts", None, None),
            File("types/node/path.d.ts", None, None),
            File("types/node/perf_hooks.d.ts", None, None),
            File("types/node/process.d.ts", None, None),
            File("types/node/punycode.d.ts", None, None),
            File("types/node/querystring.d.ts", None, None),
            File("types/node/readline.d.ts", None, None),
            File("types/node/repl.d.ts", None, None),
            File("types/node/stream.d.ts", None, None),
            File("types/node/string_decoder.d.ts", None, None),
            File("types/node/timers.d.ts", None, None),
            File("types/node/tls.d.ts", None, None),
            File("types/node/trace_events.d.ts", None, None),
            File("types/node/tsconfig.json", None, None),
            File("types/node/tslint.json", None, None),
            File("types/node/tty.d.ts", None, None),
            File("types/node/url.d.ts", None, None),
            File("types/node/util.d.ts", None, None),
            File("types/node/v8.d.ts", None, None),
            File("types/node/vm.d.ts", None, None),
            File("types/node/worker_threads.d.ts", None, None),
            File("types/node/zlib.d.ts", None, None),
        ],
    ),
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
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types"><code>Partial&lt;T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types"><code>Pick&lt;T, K extends keyof T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#understanding-private"><code>private</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#understanding-protected"><code>protected</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#public-private-and-protected-modifiers"><code>public</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/classes.html#readonly-modifier"><code>readonly</code> (w/ classes)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types"><code>Readonly&lt;T&gt;</code></a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/interfaces.html#readonly-properties"><code>readonly</code> (w/ interfaces)</a></li>',
    '<li><a href="https://www.typescriptlang.org/docs/handbook/advanced-types.html#mapped-types"><code>Record&lt;T, K extends keyof T&gt;</code></a></li>',
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


def write_introduction_paragraph(fout, cheatsheet_version):
    INTRODUCTON_LINES = [
        "<p>\n",
        '<a href="https://www.typescriptlang.org/">TypeScript</a> \n',
        "is a typed superset of JavaScript that compiles to plain JavaScript. \n",
        "This is a list of TypeScript types generated from the declaration files in \n",
        f'<a href="{TYPESCRIPT_BASE_URL}/{cheatsheet_version}">',
        f"{TYPESCRIPT_BASE_URL}/{cheatsheet_version}</a>. \n",
        "The script to generate this list is \n",
        '<a href="https://github.com/saltycrane/typescript-cheatsheet">on github</a>.\n',
        "Fixes welcome.</p>\n",
        "<p>See also my\n",
        '<a href="/typescript-react-cheat-sheet/latest/">TypeScript React cheat sheet</a>.\n',
        "</p>\n\n",
    ]
    for line in INTRODUCTON_LINES:
        fout.write(line)


def write_list_of_versions(fout, this_version):
    version_list = []
    for index, version_map in enumerate(VERSIONS):
        version = version_map["cheatsheet"]
        if index == 0:
            slug = "latest"
        else:
            slug = version
        if version == this_version:
            version_list.append(
                f' <strong style="font-size: 120%">{version}</strong>'
            )
        else:
            version_list.append(
                f' <a href="{PUBLISH_BASE_URL}/{slug}/">{version}</a>'
            )
    version_string = "".join(version_list)
    fout.write(f"<p>TypeScript version: {version_string}</p>\n\n")


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
