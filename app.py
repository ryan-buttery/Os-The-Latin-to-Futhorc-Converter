from mappings import mappings as m


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

# Example usage
input_string = "This is a list of strange runes. ae oe eo th st. That was fun."
output_string = substitute_text(input_string)
print(output_string)