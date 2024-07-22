from tkinter import Toplevel, Label, Button, PhotoImage, Frame, BOTH, Tk
import webbrowser

# pop ups

heading_font: tuple = ("Serif", 16, "bold")
subheading_font: tuple = ("Serif", 14, "bold")
regular_text_font: tuple = ("Serif", 12)


def show_about():
    # create Toplevel window and add main label
    about_window = Toplevel()
    about_window.title("About Ōs")

    # Load the icon image
    icon_path = "./icons/favicon_square.png"
    icon_image = PhotoImage(file=icon_path)

    # Create a frame for the heading and icon
    about_window_content_frame = Frame(about_window)
    about_window_content_frame.pack(pady=10, padx=10, fill=BOTH)

    # Create the icon label and pack it in the frame
    icon_label = Label(about_window_content_frame, image=icon_image)
    icon_label.pack(side="left", padx=10)

    # Keep a reference to the image to prevent garbage collection
    icon_label.image = icon_image

    about_title = "Ōs: The Latin to Futhorc Converter\n"
    label_about_title = Label(
        about_window_content_frame,
        text=about_title,
        wraplength=500,
        justify="left",
        font=heading_font,
        anchor="e",
    )
    label_about_title.pack(pady=10, padx=10)

    about_text = (
        "Created by Ryan Buttery.\n\n"
        "Copyright 2024 Ryan Buttery and Ōs contributors.\n"
        "All rights reserved."
    )
    label_about_body = Label(
        about_window_content_frame,
        text=about_text,
        wraplength=500,
        justify="left",
        font=regular_text_font,
        anchor="s",
    )
    label_about_body.pack(pady=10, padx=10)

    # pack links
    github_hyperlink_text = "Project GitHub"
    github_hyperlink_url = (
        "https://github.com/ryan-buttery/futhorc-transliterationtron-9000/"
    )
    github_link = Label(
        about_window_content_frame,
        text=github_hyperlink_text,
        fg="blue",
        cursor="hand2",
        wraplength=500,
        font=subheading_font,
        anchor="e",
    )
    github_link.pack(pady=0, padx=10)

    rb_hyperlink_text = "My Site"
    rb_hyperlink_url = "https://ryanbuttery.co.uk"
    rb_link = Label(
        about_window_content_frame,
        text=rb_hyperlink_text,
        fg="blue",
        cursor="hand2",
        wraplength=500,
        font=subheading_font,
        anchor="w",
    )
    rb_link.pack(pady=0, padx=10)

    # make the links do hyperlinky things
    def open_github_url(event):
        webbrowser.open_new(github_hyperlink_url)

    def open_rb_url(event):
        webbrowser.open_new(rb_hyperlink_url)

    # Bind the click event to the hyperlinks
    github_link.bind("<Button-1>", open_github_url)
    rb_link.bind("<Button-1>", open_rb_url)

    # pack close btn
    close_button = Button(about_window, text="Close", command=about_window.destroy)
    close_button.pack(pady=10)


def show_license() -> None:
    # create Toplevel window and add main label
    license_window = Toplevel()
    license_window.title("Licensing and Legal Information")
    license_text = (
        "Ōs: The Latin to Futhorc Converter\n\n"
        "This program is free software; you can redistribute it and/or modify "
        "it under the terms of the GNU General Public License as published by "
        "the Free Software Foundation; either version 2 of the License, or "
        "(at your option) any later version.\n"
        "This program is distributed in the hope that it will be useful, "
        "but WITHOUT ANY WARRANTY; without even the implied warranty of "
        "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the "
        "GNU General Public License for more details.\n"
        "You should have received a copy of the GNU General Public License along "
        "with this program; if not, write to the Free Software Foundation, Inc., "
        "51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA."
    )
    label_text = Label(
        license_window, text=license_text, wraplength=500, justify="left"
    )
    label_text.pack(pady=10, padx=10)

    # pack link
    hyperlink_text = "GNU GPL 2.0 License"
    hyperlink_url = "https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html"
    link = Label(
        license_window, text=hyperlink_text, fg="blue", cursor="hand2", wraplength=500
    )
    link.pack(pady=5, padx=10)

    # make the link to hyperlinky things
    def open_url(event):
        webbrowser.open_new(hyperlink_text)

    # pack link
    link.bind("<Button-1>", open_url)

    # footer label
    copyright_text = (
        "Copyright © 2024 Ryan Buttery and Ōs contributors. All rights reserved."
    )
    label_copyright = Label(
        license_window, text=copyright_text, wraplength=500, justify="left"
    )
    label_copyright.pack(pady=10, padx=10)

    # pack close btn
    close_button = Button(license_window, text="Close", command=license_window.destroy)
    close_button.pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    root.title("about debug")
    root.geometry("300x300")
    about_button = Button(root, text="About", command=show_about)
    about_button.pack(pady=10)
    about_button = Button(root, text="License", command=show_license)
    about_button.pack(pady=10)
    close_button = Button(root, text="Close", command=root.destroy)
    close_button.pack(pady=10)
    root.mainloop()
