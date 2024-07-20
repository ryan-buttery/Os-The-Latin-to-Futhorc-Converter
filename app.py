from mappings import mappings as m
from inout import inout as ino
from roman import int_to_roman

mapping_dict = dict(m)

def substitute_text(input_text: str) -> str:
    input_text = input_text.lower()

    result = []
    i = 0
    while i < len(input_text):
         # Check if the current character is a digit
        if input_text[i].isdigit():
            # Find the full number
            num_str = ''
            while i < len(input_text) and input_text[i].isdigit():
                num_str += input_text[i]
                i += 1
            # Convert the number to an integer
            number = int(num_str)
            # Convert the integer to a Roman numeral
            roman_numeral = int_to_roman(number)
            # Add the Roman numeral to the result
            result.append(roman_numeral)
        # Firstly deal with substitutions that have two original letters or punctuation followed by a space
        elif input_text[i:i+2] in mapping_dict:
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
    filepath = 'example.txt'
    input_string = ino.read_txt(filepath)
    output_string = substitute_text(input_string)
    ino.save_txt(output_string)