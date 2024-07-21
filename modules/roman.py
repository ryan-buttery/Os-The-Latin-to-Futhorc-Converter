def int_to_roman(number):
    """
    Converts an integer to a Roman numeral.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the number.
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman_numeral = ""

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            roman_numeral += sym[i]
            div -= 1
        i -= 1

    return roman_numeral
