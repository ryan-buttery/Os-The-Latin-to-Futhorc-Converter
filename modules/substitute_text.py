from modules.mappings import mappings as m
from modules.roman import int_to_roman


mapping_dict = dict(m)


def substitute_text(input_text: str) -> str:
    """
    Converts a string of latin letters and arabic numerals to futhorc runes and roman numerals respectively.

    Args:
    input_text (str): The string of text you would like to convert.
    """
    input_text = input_text.lower()
    result = []
    i = 0
    while i < len(input_text):
        # Check if the current character is a digit
        if input_text[i].isdigit():
            # Find the full number
            num_str = ""
            while i < len(input_text) and input_text[i].isdigit():
                num_str += input_text[i]
                i += 1
            # Convert the number to an integer
            number = int(num_str)
            # Convert the integer to a Roman numeral
            roman_numeral = int_to_roman(number)
            # Add the Roman numeral to the result
            result.append(roman_numeral)
        # Firstly deal with substitutions that have three original chars
        elif input_text[i : i + 3] in mapping_dict:
            result.append(mapping_dict[input_text[i : i + 3]])
            i += 3
        # then  deal with substitutions that have two original letters or punctuation followed by a space
        elif input_text[i : i + 2] in mapping_dict:
            result.append(mapping_dict[input_text[i : i + 2]])
            i += 2
        # Now substitute single letters into the correct rune
        elif input_text[i] in mapping_dict:
            result.append(mapping_dict[input_text[i]])
            i += 1
        # If I am a dumb dumb who missed something in the mapping, just add it and feel bad later.
        else:
            result.append(input_text[i])
            i += 1
    return "".join(result)
