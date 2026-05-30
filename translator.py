import tkinter as tk
from tkinter import ttk, messagebox

from googletrans import Translator, LANGUAGES
import pyperclip

# Translator object
translator = Translator()

# Main window
window = tk.Tk()
window.title("Language Translation Tool")
window.geometry("700x500")
window.config(bg="lightblue")

# Title
title = tk.Label(
    window,
    text="Language Translation Tool",
    font=("TimesNewRoman", 20, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

# Input text label
input_label = tk.Label(
    window,
    text="Enter Text",
    font=("TimesNewRoman", 15),
    bg="lightblue"
)
input_label.pack()

# Input text box
input_text = tk.Text(window, height=8, width=70)
input_text.pack(pady=10)

# Language list
language_list = list(LANGUAGES.values())

# Source language
source_label = tk.Label(
    window,
    text="Source Language",
    font=("TimesNewRoman", 15),
    bg="lightblue"
)
source_label.pack()

source_combo = ttk.Combobox(
    window,
    values=language_list,
    width=30
)
source_combo.pack()
source_combo.set("english")

# Target language
target_label = tk.Label(
    window,
    text="Target Language",
    font=("TimesNewRoman", 15),
    bg="lightblue"
)
target_label.pack()

target_combo = ttk.Combobox(
    window,
    values=language_list,
    width=30
)
target_combo.pack()
target_combo.set("telugu")

# Output label
output_label = tk.Label(
    window,
    text="Translated Text",
    font=("TimesNewRoman", 15,"bold"),
    bg="lightblue"
)
output_label.pack(pady=10)

# Output text box
output_text = tk.Text(window, height=8, width=70)
output_text.pack()

# Translate function
def translate_text():

    text = input_text.get(1.0, tk.END).strip()

    source_lang = source_combo.get()
    target_lang = target_combo.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text")
        return

    try:

        # Convert language names to codes
        source_code = None
        target_code = None

        for code, language in LANGUAGES.items():

            if language == source_lang:
                source_code = code

            if language == target_lang:
                target_code = code

        translated = translator.translate(
            text,
            src=source_code,
            dest=target_code
        )

        output_text.delete(1.0, tk.END)

        output_text.insert(
            tk.END,
            translated.text
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy function
def copy_text():

    translated = output_text.get(1.0, tk.END)

    pyperclip.copy(translated)

    messagebox.showinfo(
        "Copied",
        "Translated text copied to clipboard"
    )

# Translate button
translate_button = tk.Button(
    window,
    text="Translate",
    font=("TimesNewRoman", 15, "bold"),
    bg="green",
    fg="white",
    command=translate_text
)
translate_button.pack(pady=10)

# Copy button
copy_button = tk.Button(
    window,
    text="Copy Text",
    font=("TimesNewRoman", 15, "bold"),
    bg="blue",
    fg="white",
    command=copy_text
)
copy_button.pack()

# Run application
window.mainloop()