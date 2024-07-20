from app import substitute_text
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


def process_text():
    content = input_text_box.get(1.0, tk.END)
    modified_content = substitute_text(content)
    output_text_box.delete(1.0, tk.END)
    output_text_box.insert(tk.END, modified_content)


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Latin to Futhorc Converter")

input_text_box = Text(root, wrap="word")
input_text_box.pack(expand=True, fill="both")
output_text_box = Text(root, wrap="word")

output_text_box.pack(expand=True, fill="both")

open_button = tk.Button(root, text="Open .txt File", command=open_file)
open_button.pack(side="left")

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side="right")

save_button = tk.Button(root, text="Save as .txt", command=save_text_file)
save_button.pack(side="right")

process_button = tk.Button(root, text="Convert to runic", command=process_text)
process_button.pack(side="right")


root.mainloop()
