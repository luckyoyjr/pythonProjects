import tkinter as tk
from tkinter import messagebox

def count_characters(event=None):
    text = text_box.get("1.0", tk.END).strip()
    char_count = len(text)
    word_count = len(text.split())

    char_label.config(text=f"Characters: {char_count}/280")
    word_label.config(text=f"Words: {word_count}")

    if char_count > 280:
        text_box.delete("1.0", tk.END)
        text_box.insert("1.0", text[:280])
        messagebox.showwarning("Limit Reached", "You have reached the 280 character limit!")

root = tk.Tk()
root.title("Comment Box with Word Counter")
root.geometry("400x300")

text_box = tk.Text(root, height=10, width=40)
text_box.pack()

char_label = tk.Label(root, text="Characters: 0/280")
char_label.pack()

word_label = tk.Label(root, text="Words: 0")
word_label.pack()

text_box.bind("<KeyRelease>", count_characters)

root.mainloop()

