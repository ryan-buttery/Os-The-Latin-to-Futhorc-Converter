from mappings import mappings as m
from inout import inout as ino

mapping_dict = dict(m)

def substitute_text(input_text: str) -> str:
    input_text = input_text.lower()

    result = []
    i = 0
    while i < len(input_text):
        # Firstly deal with substitutions that have two original letters or punctuation followed by a space
        if input_text[i:i+2] in mapping_dict:
            result.append(mapping_dict[input_text[i:i+2]])
            i += 2
        # Now substitute single letters into the correct rune
        elif input_text[i] in mapping_dict:
            result.append(mapping_dict[input_text[i]])
            i += 1
        # If I am a dumb dumb who missed something in the mapping, just add it and feel bad later.
        else:
            result.append(input_text[i])
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    filepath = './text.txt'
    input_string = ino.read_txt(filepath)
    output_string = substitute_text(input_string)
    ino.save_txt(filepath, output_string)