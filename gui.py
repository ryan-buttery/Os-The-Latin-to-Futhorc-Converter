from substitute_text import substitute_text
from filehandling import fh
import tkinter as tk
from tkinter import filedialog, Text


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
        content = input_text_box.get(1.0, tk.END)
        modified_content = substitute_text(content)
        output_text_box.delete(1.0, tk.END)
        output_text_box.insert(tk.END, modified_content)
        input_text_box.edit_modified(False)


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Latin to Futhorc Converter")

open_button = tk.Button(root, text="Import .txt File", command=open_file)
open_button.pack(side="top")

input_text_box = Text(root, wrap="word")
input_text_box.pack(expand=True, fill="both")
input_text_box.bind("<<Modified>>", process_text)

output_text_box = Text(root, wrap="word")
output_text_box.pack(expand=True, fill="both")

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side="right")

save_odt_file_button = tk.Button(root, text="Save as .odt", command=save_odt_file)
save_odt_file_button.pack(side="right")

save_text_file_button = tk.Button(root, text="Save as .txt", command=save_text_file)
save_text_file_button.pack(side="right")

# process_button = tk.Button(root, text="Convert to runic", command=process_text)
# process_button.pack(side="right")


root.mainloop()
