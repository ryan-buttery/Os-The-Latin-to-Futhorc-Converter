from modules.substitute_text import substitute_text
from modules.filehandling import fh
import tkinter as tk
from tkinter import filedialog, scrolledtext
import os
import re
import sys

# Aesthetics
heading_font: tuple = ("Serif", 16, "bold")
subheading_font: tuple = ("Serif", 14, "bold")
input_text_font: tuple = ("Serif", 12)
output_text_font: tuple = ("Serif", 12, "bold")


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        input_text_box.delete(1.0, tk.END)
        input_text_box.insert(tk.END, content)


def save_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        content = output_text_box.get(1.0, tk.END)
        with open(file_path, "w") as file:
            file.write(content)


def save_odt_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".odt")
    if file_path:
        content = output_text_box.get(1.0, tk.END)
        fh.save_as_odt(filepath=file_path, content=content)


def process_text(event=None):
    if input_text_box.edit_modified():
        output_text_box.config(state="normal")
        content = input_text_box.get(1.0, tk.END)
        modified_content = substitute_text(content)
        output_text_box.delete(1.0, tk.END)
        output_text_box.insert(tk.END, modified_content)
        input_text_box.edit_modified(False)
        output_text_box.config(state="disabled")


def exit_app():
    root.destroy()


def paste_from_clipboard():
    # Enable the ScrolledText widget temporarily to paste content
    input_text_box.insert(tk.INSERT, root.clipboard_get())


def clear_text():
    # Enable the ScrolledText widget temporarily to clear content
    input_text_box.delete("1.0", tk.END)


def select_all_and_copy():
    # Select all text
    output_text_box.tag_add(tk.SEL, "1.0", tk.END)
    output_text_box.mark_set(tk.INSERT, "1.0")
    output_text_box.see(tk.INSERT)
    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(output_text_box.get("1.0", tk.END))


# keyboard shortcut enablers
def select_all(event):
    event.widget.tag_add(tk.SEL, "1.0", tk.END)
    event.widget.mark_set(tk.INSERT, "1.0")
    event.widget.see(tk.INSERT)
    return "break"  # Prevent the default behavior


def delete_word(event):
    # Get the current cursor position
    cursor_position = input_text_box.index(tk.INSERT)

    # Get all the text before the cursor
    text_before_cursor = input_text_box.get("1.0", cursor_position)

    # Find the position of the start of the word or symbol before the cursor
    match = re.search(r"[\w]+|[^\w\s]", text_before_cursor[::-1])
    if match:
        start_pos = len(text_before_cursor) - match.end()
        # Delete from start_pos to the cursor position
        input_text_box.delete(f"1.0 + {start_pos} chars", cursor_position)

    return "break"


# right click menu functions


def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)
    context_menu.entryconfig("Cut", command=lambda: cut_text(event))
    context_menu.entryconfig("Copy", command=lambda: copy_text(event))
    context_menu.entryconfig("Paste", command=lambda: paste_text(event))
    context_menu.entryconfig("Select All", command=lambda: select_all(event))


def copy_text(event=None):
    event.widget.event_generate("<<Copy>>")


def cut_text(event=None):
    event.widget.event_generate("<<Cut>>")


def paste_text(event=None):
    event.widget.event_generate("<<Paste>>")


root = tk.Tk()
root.title("Latin to Futhorc Converter")

root.geometry()

if sys.platform.startswith("win"):
    icon_path = resource_path("icons/favicon_square.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"Icon file not found at {icon_path}")
else:
    icon_path = resource_path("icons/favicon_square.png")
    if os.path.exists(icon_path):
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    else:
        print(f"Icon file not found at {icon_path}")

# create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create menu (file)
file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Import from txt file", command=open_file)
file_menu.add_command(label="Save as txt file", command=save_text_file)
file_menu.add_command(label="Save as LibreOffice Document", command=save_odt_file)
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# create edit bar

edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label="Copy Output", command=select_all_and_copy)
edit_menu.add_command(label="Paste Input", command=paste_from_clipboard)
edit_menu.add_command(label="Clear Input", command=clear_text)
menubar.add_cascade(label="Edit", menu=edit_menu)


# right click menu

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut", command=cut_text)
context_menu.add_command(label="Copy", command=copy_text)
context_menu.add_command(label="Paste", command=paste_text)
context_menu.add_command(label="Select All", command=select_all)

# create the main frame to contain everything
main_heading_frame = tk.Frame(root)
main_heading_frame.pack(fill=tk.X)

# Create the main heading
main_heading = tk.Label(
    main_heading_frame, text="Latin to Futhorc Converter / ᛚᚪᛏᛁᚾ᛫ᛏᚩ᛫ᚠᚢᚦᚩᚱᚳ᛫ᚳᚩᚾᚠᛖᚱᛏᛖᚱ"
)
main_heading.config(font=heading_font)
main_heading.pack(padx=10, pady=10, anchor=tk.W, side=tk.LEFT)


main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

input_frame = tk.LabelFrame(main_frame, text="Input / ᛁᚾᛈᚢᛏ")
input_frame.pack(padx=10, pady=10, anchor=tk.W, side=tk.LEFT, fill=tk.BOTH, expand=True)
input_frame.config(font=(subheading_font))

output_frame = tk.LabelFrame(main_frame, text="Output / ᚩᚢᛏᛈᚢᛏ")
output_frame.config(font=(subheading_font))
output_frame.pack(
    padx=10, pady=10, anchor=tk.W, side=tk.RIGHT, fill=tk.BOTH, expand=True
)

input_text_box = scrolledtext.ScrolledText(input_frame, wrap="word")
input_text_box.config(font=input_text_font)
input_text_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
input_text_box.bind("<Control-a>", select_all)
input_text_box.bind("<Control-A>", select_all)
input_text_box.bind("<<Modified>>", process_text)
input_text_box.bind("<Control-BackSpace>", delete_word)
input_text_box.bind("<Button-3>", show_context_menu)


# paste_button = tk.Button(input_frame, text="Paste", command=paste_from_clipboard)
# paste_button.pack(pady=10, anchor=tk.CENTER)


output_text_box = scrolledtext.ScrolledText(output_frame, wrap="word", state="disabled")
output_text_box.config(font=output_text_font)
output_text_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
output_text_box.bind("<Control-a>", select_all)
output_text_box.bind("<Control-A>", select_all)
output_text_box.bind("<Button-3>", show_context_menu)

# copy_button = tk.Button(output_frame, text="Copy", command=select_all_and_copy)
# copy_button.pack(pady=10)
root.mainloop()
