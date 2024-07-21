from substitute_text import substitute_text
from filehandling import fh
import tkinter as tk
from tkinter import filedialog, Text, scrolledtext

# Aesthetics
heading_font: tuple = ("Serif", 16, "bold")
subheading_font: tuple = ("Serif", 12, "bold")


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


def select_all(event):
    event.widget.tag_add(tk.SEL, "1.0", tk.END)
    event.widget.mark_set(tk.INSERT, "1.0")
    event.widget.see(tk.INSERT)
    return "break"  # Prevent the default behavior


def select_all_and_copy():
    # Select all text
    output_text_box.tag_add(tk.SEL, "1.0", tk.END)
    output_text_box.mark_set(tk.INSERT, "1.0")
    output_text_box.see(tk.INSERT)
    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(output_text_box.get("1.0", tk.END))


root = tk.Tk()
root.title("Latin to Futhorc Converter")
root.geometry()
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create menu (file)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Import from txt file", command=open_file)
file_menu.add_command(label="Save as txt file", command=save_text_file)
file_menu.add_command(label="Save as LibreOffice Document", command=save_odt_file)
file_menu.add_command(label="Exit", command=exit_app)

# Add file menu to menubar
menubar.add_cascade(label="File", menu=file_menu)

main_heading_frame = tk.Frame(root)
main_heading_frame.pack(fill=tk.X)
# Create the main heading

main_heading = tk.Label(main_heading_frame, text="Latin to Futhorc Converter")
main_heading.config(font=heading_font)
main_heading.pack(padx=10, pady=10, anchor=tk.W, side=tk.LEFT)


main_frame = tk.Frame(root)
main_frame.pack(fill=tk.X)

input_frame = tk.LabelFrame(main_frame, text="Input")
input_frame.pack(padx=10, pady=10, anchor=tk.W, side=tk.LEFT)
input_frame.config(font=(subheading_font))

output_frame = tk.LabelFrame(main_frame, text="Output")
output_frame.config(font=(subheading_font))
output_frame.pack(padx=10, pady=10, anchor=tk.W, side=tk.RIGHT)

input_text_box = scrolledtext.ScrolledText(input_frame, wrap="word")
input_text_box.pack(padx=10, pady=10, expand=True, fill="both")
input_text_box.bind("<Control-a>", select_all)
input_text_box.bind("<Control-A>", select_all)
input_text_box.bind("<<Modified>>", process_text)

output_text_box = scrolledtext.ScrolledText(output_frame, wrap="word", state="disabled")
output_text_box.pack(padx=10, pady=10, expand=True, fill="both")
output_text_box.bind("<Control-a>", select_all)
output_text_box.bind("<Control-A>", select_all)

copy_button = tk.Button(output_frame, text="Copy Output", command=select_all_and_copy)
copy_button.pack(pady=10)
root.mainloop()
