import unittest
from unittest.mock import mock_open, patch, MagicMock, call
from modules.substitute_text import substitute_text, mapping_dict
import modules.main_window as main_window
import modules.about_windows as about_windows
from modules.logo import logo
from tkinter import BOTH
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


class TestMainGUI(unittest.TestCase):

    @patch("tkinter.filedialog.askopenfilename")
    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data="mocked file content",
    )
    def test_open_file(self, mock_open, mock_askopenfilename):
        mock_askopenfilename.return_value = "dummy_path"

        main_window.input_text_box = MagicMock()
        main_window.open_file()

        main_window.input_text_box.delete.assert_called_once_with(
            1.0, main_window.tk.END
        )
        main_window.input_text_box.insert.assert_called_once_with(
            main_window.tk.END, "mocked file content"
        )

    @patch("tkinter.filedialog.asksaveasfilename")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_save_text_file(self, mock_open, mock_asksaveasfilename):
        mock_asksaveasfilename.return_value = "dummy_save_path"

        main_window.output_text_box = MagicMock()
        main_window.output_text_box.get.return_value = "content to save"

        main_window.save_text_file()

        mock_open.assert_called_once_with("dummy_save_path", "w")
        mock_open().write.assert_called_once_with("content to save")

    @patch("modules.main_window.substitute_text", return_value="modified text")
    @patch("modules.main_window.output_text_box", new_callable=MagicMock)
    @patch("modules.main_window.input_text_box", new_callable=MagicMock)
    def test_process_text(
        self, mock_input_text_box, mock_output_text_box, mock_substitute_text
    ):
        # Simulate modified text in input_text_box
        mock_input_text_box.edit_modified.return_value = True
        mock_input_text_box.get.return_value = "some text"

        # Call the process_text function
        main_window.process_text()

        # Check that input_text_box methods were called correctly
        expected_calls = [call(), call(False)]
        mock_input_text_box.edit_modified.assert_has_calls(expected_calls)

        # Check that output_text_box methods were called correctly
        mock_output_text_box.config.assert_any_call(state="normal")
        mock_output_text_box.delete.assert_called_once_with(1.0, main_window.tk.END)
        mock_output_text_box.insert.assert_called_once_with(
            main_window.tk.END, "modified text"
        )
        mock_output_text_box.config.assert_any_call(state="disabled")

        # Check that substitute_text was called with the correct arguments
        mock_substitute_text.assert_called_once_with("some text")

    def test_copy_text(self):
        event = MagicMock()
        event.widget = MagicMock()

        main_window.copy_text(event)

        event.widget.event_generate.assert_called_once_with("<<Copy>>")

    def test_cut_text(self):
        event = MagicMock()
        event.widget = MagicMock()

        main_window.cut_text(event)

        event.widget.event_generate.assert_called_once_with("<<Cut>>")

    def test_paste_text(self):
        event = MagicMock()
        event.widget = MagicMock()

        main_window.paste_text(event)

        event.widget.event_generate.assert_called_once_with("<<Paste>>")


class TestHelpGUI(unittest.TestCase):

    @patch("modules.about_windows.Toplevel")
    @patch("modules.about_windows.PhotoImage")
    @patch("modules.about_windows.Label")
    @patch("modules.about_windows.Button")
    @patch("modules.about_windows.Frame")
    @patch("modules.about_windows.decode_base64_image")
    def test_show_about(
        self, mock_decode_base64_image, mock_frame, mock_button, mock_label, mock_photoimage, mock_toplevel
    ):
        # Mock the frame instance
        mock_frame_instance = MagicMock()
        mock_frame.return_value = mock_frame_instance

        # Mock the return value of decode_base64_image
        mock_photoimage_instance = MagicMock()
        mock_decode_base64_image.return_value = mock_photoimage_instance

        # Call the function
        about_windows.show_about()

        # Check that Toplevel window was created
        mock_toplevel.assert_called_once()

        # Check that decode_base64_image was called with the correct logo
        mock_decode_base64_image.assert_called_once_with(logo)

        # Check that Frame was created in Toplevel
        mock_frame.assert_called_once_with(mock_toplevel())
        mock_frame_instance.pack.assert_called_once_with(pady=10, padx=10, fill='both')

        # Check that the icon label was created with the image inside the frame
        mock_label.assert_any_call(mock_frame_instance, image=mock_photoimage_instance)

        # Check that the about title and body labels were created inside the frame
        mock_label.assert_any_call(
            mock_frame_instance,
            text="Ōs: The Latin to Futhorc Converter\nᚩ᛬ᚦᛖ᛫ᛚᚪᛏᛁᚾ᛫ᛏᚩ᛫ᚠᚢᚦᚩᚱᚳ᛫ᚳᚩᚾᚠᛖᚱᛏᛖᚱ",
            wraplength=500,
            justify="left",
            font=about_windows.heading_font,
            anchor="e",
        )
        mock_label.assert_any_call(
            mock_frame_instance,
            text="Created by Ryan Buttery.\n\nCopyright 2024 Ryan Buttery and Ōs contributors.\nAll rights reserved.",
            wraplength=500,
            justify="left",
            font=about_windows.regular_text_font,
            anchor="s",
        )

        # Check that the GitHub link was created with the correct text inside the frame
        mock_label.assert_any_call(
            mock_frame_instance,
            text="Project GitHub",
            fg="blue",
            cursor="hand2",
            wraplength=500,
            font=about_windows.subheading_font,
            anchor="e",
        )

        # Check that the personal site link was created with the correct text inside the frame
        mock_label.assert_any_call(
            mock_frame_instance,
            text="My Site",
            fg="blue",
            cursor="hand2",
            wraplength=500,
            font=about_windows.subheading_font,
            anchor="w",
        )

        # Check that the footer label was created inside the frame
        mock_label.assert_any_call(
            mock_frame_instance,
            text="Made with ❤️ by a proud Mercian!",
            wraplength=500,
            justify="center",
            font=about_windows.regular_text_font,
            anchor="s",
        )

        # Check that the close button was created
        mock_button.assert_called_once_with(
            mock_toplevel(), text="Close", command=mock_toplevel().destroy
        )

    @patch("modules.about_windows.Toplevel")
    @patch("modules.about_windows.Label")
    @patch("modules.about_windows.Button")
    def test_show_license(self, mock_button, mock_label, mock_toplevel):
        # Call the function
        about_windows.show_license()

        # Check that Toplevel window was created
        mock_toplevel.assert_called_once()

        # Check that the license text label was created
        license_text = (
            "Ōs: The Latin to Futhorc Converter\nᚩ᛬ᚦᛖ᛫ᛚᚪᛏᛁᚾ᛫ᛏᚩ᛫ᚠᚢᚦᚩᚱᚳ᛫ᚳᚩᚾᚠᛖᚱᛏᛖᚱ\n\n"
            "This program is free software; you can redistribute it and/or modify "
            "it under the terms of the GNU General Public License as published by "
            "the Free Software Foundation; with version 2 of the License.\n"
            "This program is distributed in the hope that it will be useful, "
            "but WITHOUT ANY WARRANTY; without even the implied warranty of "
            "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the "
            "GNU General Public License for more details.\n"
            "You should have received a copy of the GNU General Public License along "
            "with this program; if not, write to the Free Software Foundation, Inc., "
            "51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA."
        )
        mock_label.assert_any_call(
            mock_toplevel(), text=license_text, wraplength=500, justify="left"
        )

        # Check that the GNU GPL link was created with the correct text
        mock_label.assert_any_call(
            mock_toplevel(),
            text="GNU GPL 2.0 License",
            fg="blue",
            cursor="hand2",
            wraplength=500,
        )

        # Check that the copyright text label was created
        mock_label.assert_any_call(
            mock_toplevel(),
            text="Copyright © 2024 Ryan Buttery and Ōs contributors. All rights reserved.",
            wraplength=500,
            justify="left",
        )

        # Check that the close button was created
        mock_button.assert_called_once_with(
            mock_toplevel(), text="Close", command=mock_toplevel().destroy
        )


if __name__ == "__main__":
    unittest.main()
