"""
Usage: python3 typescript_cheatsheet.py

"""
from cheatsheet import File, make_cheatsheet


################
# constants
################
OUTPUT_TEMPLATE = 'dist/typescript/{version}.html'
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


def write_introduction_paragraph(fout, version):
    INTRODUCTON_LINES = [
        '<p>\n',
        '<a href="https://www.typescriptlang.org/">TypeScript</a> \n',
        'is a typed superset of JavaScript that compiles to plain JavaScript. \n',
        'This is a list of TypeScript types generated from the declaration files in \n',
        f'<a href="{GITHUB_BASE_URL}/{version}">{GITHUB_BASE_URL}/{version}</a>. \n',
        'The script to generate this list is \n',
        '<a href="https://github.com/saltycrane/typescript-cheatsheet">on github</a>.\n',
        'Fixes welcome.\n',
        'See also my\n',
        '<a href="/typescript-react-cheat-sheet/latest/">TypeScript React cheat sheet</a>,\n',
        '<a href="/flow-type-cheat-sheet/latest/">Flow type cheat sheet</a>,\n',
        'and <a href="/blog/2017/08/docker-cheat-sheet/">Docker cheat sheet</a>.\n',
        '</p>\n\n',
    ]
    for line in INTRODUCTON_LINES:
        fout.write(line)


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


if __name__ == '__main__':
    main()
