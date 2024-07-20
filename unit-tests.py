import unittest
from app import substitute_text, mapping_dict

class TestSubstituteText(unittest.TestCase):

    def test_single_character_mappings(self):
        # Assuming 'a' maps to 'ᚪ'
        self.assertEqual(substitute_text('a'), mapping_dict['a'])

    def test_two_character_mappings(self):
        # Assuming 'ae' maps to 'ᚫ'
        self.assertEqual(substitute_text('ae'), mapping_dict['ae'])

    def test_number_conversion_to_roman(self):
        self.assertEqual(substitute_text('1993'), 'MCMXCIII')

    def test_mixed_input(self):
        # Check that sticking numbers in the middle of words doesn't break ought
        input_text = 'a1b2'
        expected_output = mapping_dict['a'] + 'I' + mapping_dict['b'] + 'II'
        self.assertEqual(substitute_text(input_text), expected_output)

    def test_unmapped_characters(self):
        # Should just return as ! since we don't map it. 
        self.assertEqual(substitute_text('!'), '!')

    def test_empty_string(self):
        self.assertEqual(substitute_text(''), '')

if __name__ == '__main__':
    unittest.main()
