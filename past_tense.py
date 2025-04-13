import argparse
import os
import re
import spacy
import pyinflect


nlp = spacy.load("en_core_web_sm")

# for keywords not in a standard dictionary
keywords = {
    "namespace": "namespaced",
    "println": "printedln",
    "Destructure": "Destructured"
}

def load_file(filepath):
    """
    Load the contents of a file.
    """
    with open(filepath, 'r', encoding="utf-8") as file:
        return file.read()
    
def save_file(filepath, content):
    """
    Save content to a file.
    """
    with open(filepath, 'w', encoding="utf-8") as file:
        file.write(content)

def to_the_past(text):
    """
    Convert a word to its past tense form using spaCy and pyinflect.
    """
    verb_list = ['VB', 'VBP', 'VBZ']

    doc_dep = nlp(text)
    for token in doc_dep:
        # if it's not read as a verb already, see if it can be read that way
        if token.tag_ not in verb_list:
            token.tag_ = 'VB'
        if token.tag_ in verb_list:
            # print(token.text, token.lemma_, token.pos_, token.tag_) 
            translate = token._.inflect("VBD")
            if translate:
                text = text.replace(token.text, translate)
    return text

def main():
    parser = argparse.ArgumentParser(description="Translate working code into Past Tense.")
    parser.add_argument("filepath", type=str, help="The code file to read")
    parser.add_argument("-o", "--outfile", type=str, default=None, help="The file to output")
    args = parser.parse_args()

    try:
        code = load_file(args.filepath)
    except FileNotFoundError:
        print(f"Error: The file {args.filepath} does not exist.")
        return

    # Split into tokens
    non_alpha = "([^a-zA-Z])"
    camel_case = "(?<=[a-z])(?=[A-Z])"
    code_list = re.split(f'{non_alpha}|{camel_case}', code)
    code_list = [x for x in code_list if x is not None]

    for idx, c in enumerate(code_list):
        if c in keywords:
            code_list[idx] = keywords[c]
        elif c.isalpha():
            code_list[idx] = to_the_past(c)

    code_out = ''.join(code_list)

    if args.outfile:
        save_file(args.outfile, code_out)
    else:
        print(code_out)

if __name__ == "__main__":
    main()
