![Python versions](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

# Past Tense

Translates code into Past Tense, never to be run again.

## Description

Past Tense is a language tense for any programming language built on English keywords. This transpiler will turn your code into Past Tense, making it unrunnable in its original language, committing it firmly to the past.

| :warning: WARNING          |
|:---------------------------|
| There are no Past Tense interpreters. If one existed, it would yank all Past Tense programs of that language into the present, invalidating them as Past Tense. |

## Example

HelloWorld.cs
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
## Requirements

To run:

    python -m spacy download en_core_web_sm
    python past_tense.py <input_file> [-o output_file]
