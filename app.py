from mappings import mappings as m
from inout import inout as ino
from roman import int_to_roman
import argparse


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
    # filepath = './example.txt'
    # input_string = ino.read_txt(filepath)
    # output_string = substitute_text(input_string)
    # ino.save_as_odt(content=output_string)
    # # ino.save_txt(output_string)

    parser = argparse.ArgumentParser(description="Substitute text and save as .txt or .odt")
    parser.add_argument("input_file", nargs='?', default='./example.txt', type=str, help="Path to the input text file")
    args = parser.parse_args()

    input_string = ino.read_txt(args.input_file)
    output_string = substitute_text(input_string)

    # Prompt the user to select the output file type
    print("Select the output file type by typing the appropriate number:")
    print("[1] Text File (.txt)")
    print("[2] Libre Office Document (.odt)")
    
    file_type = input("Enter your choice: ").strip()
    
    if file_type == "1":
        output_file = args.input_file.rsplit('.', 1)[0] + ".txt"
        ino.save_txt(output_file, output_string)
        print(f"Output saved to {output_file}")
    elif file_type == "2":
        output_file = args.input_file.rsplit('.', 1)[0] + ".odt"
        ino.save_as_odt(output_file, output_string)
        print(f"Output saved to {output_file}")
    else:
        print("Invalid choice. No output file created.")