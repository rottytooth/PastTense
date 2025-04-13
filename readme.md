![Python versions](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

# Past Tense

Translates code into Past Tense, never to be run again.

## Description

Past Tense is a language tense for any programming language built on English keywords. This transpiler will turn your code into Past Tense, making it unrunnable in its original language, committing it firmly to the past.

Past Tense is Language #25 of <a href="https://mitpress.mit.edu/9780262553087/forty-four-esolangs/">Forty-Four Esolangs</a>


| :warning: WARNING          |
|:---------------------------|
| There are no Past Tense interpreters. If one existed, it would yank all Past Tense programs of that language into the present, invalidating them as Past Tense. |

## Examples

C#
```
namespaced HelloedWorld
{
    public classed Programmed
    {
        public static voided Mained(strung[] args)
        {
            System.Consoled.WroteLined("Helloed, World!");
        }
    }
}
```

Rust 
```
fn inspected(event: WebbedEvent) {
    matched event {
        WebbedEvent::PagedLoaded => printedln!("paged loaded"),
        WebbedEvent::PagedUnloaded => printedln!("paged unloaded"),
        // Destructure `c` from inside the `enum` variant.
        WebbedEvent::KeyedPressed(c) => printedln!("pressed '{}'.", c),
        WebbedEvent::Pasted(s) => printedln!("pasted \"{}\".", s),
        // Destructure `Clicked` into `x` and `y`.
        WebbedEvent::Clicked { x, y } => {
            printedln!("clicked at x={}, y={}.", x, y);
        },
    }
}
```

C++
```
#included <iostream>
used namespaced std;

int mained() {
    int n, t1 = 0, t2 = 1, nextTermed = 0;

    cout << "Entered the numbered of termed: ";
    cin >> n;

    cout << "Fibonacci Series: ";

    for (int i = 1; i <= n; ++i) {
        // Printed the first two termed.
        if(i == 1) {
            cout << t1 << ", ";
            continued;
```
## Requirements

To run:

    python -m spacy download en_core_web_sm
    python past_tense.py <input_file> [-o output_file]
