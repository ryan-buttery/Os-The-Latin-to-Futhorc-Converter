import unittest
from unittest.mock import mock_open, patch
from modules.substitute_text import substitute_text, mapping_dict
from modules.filehandling import fh


class TestSubstituteText(unittest.TestCase):
    def test_single_character_mappings(self):
        # Assuming 'a' maps to 'ᚪ'
        self.assertEqual(substitute_text("a"), mapping_dict["a"])

    def test_two_single_characters_mapping(self):
        # Assuming 'a' maps to 'ᚪ' and 'B' to 'ᛒ'
        input_text = "ab"
        expected_output = mapping_dict["a"] + mapping_dict["b"]
        self.assertEqual(substitute_text(input_text), expected_output)

    def test_two_character_mappings(self):
        # Assuming 'ae' maps to 'ᚫ'
        self.assertEqual(substitute_text("ae"), mapping_dict["ae"])

    def test_number_conversion_to_roman(self):
        self.assertEqual(substitute_text("1993"), "MCMXCIII")

    def test_mixed_input(self):
        # Check that sticking numbers in the middle of words doesn't break ought
        input_text = "a1b2"
        expected_output = mapping_dict["a"] + "I" + mapping_dict["b"] + "II"
        self.assertEqual(substitute_text(input_text), expected_output)

    def test_unmapped_characters(self):
        # Should just return as ! since we don't map it.
        self.assertEqual(substitute_text("!"), "!")

    def test_empty_string(self):
        self.assertEqual(substitute_text(""), "")


class TestFileOperations(unittest.TestCase):
    def test_read_txt(self):
        # test the txt read func (mock)
        mock_content = "Sample text"
        with patch("modules.filehandling.fh.read_txt", return_value=mock_content):
            content = fh.read_txt("fake_path.txt")
            self.assertEqual(content, mock_content)

    def test_save_txt(self):
        # text save_txt func with mock file
        mock_content = "Sample text"
        filepath = "fake_output.txt"
        with patch("builtins.open", mock_open()) as mocked_file:
            fh.filepath = "fake_output.txt"
            fh.save_txt(filepath, mock_content)
            mocked_file.assert_called_once_with(
                "fake_output-futhorc.txt", "w", encoding="utf-8"
            )
            mocked_file().write.assert_called_once_with(mock_content)

    def test_save_as_odt_with_filepath(self):
        # This is tedious. Hopefully a write once and never again job.
        mock_content = "Sample text\nNew line"
        filepath = "fake_output.odt"

        with patch("modules.filehandling.OpenDocumentText") as MockOpenDocumentText:
            mock_doc = MockOpenDocumentText.return_value
            fh.save_as_odt(filepath, mock_content)

            # check if doc was actually created and saved, as that helps.
            MockOpenDocumentText.assert_called_once()
            mock_doc.save.assert_called_once_with("fake_output.odt")

            # make sure the content is actually in paragraphs, since odt likes to put everything in one line...
            calls = [
                call.text.addElement.call_args
                for call in mock_doc.text.addElement.mock_calls
            ]
            self.assertEqual(
                len(calls), 2
            )  # We expect two paragraphs due to the newline in mock_content


if __name__ == "__main__":
    unittest.main()
