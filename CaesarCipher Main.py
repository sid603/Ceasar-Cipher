import tkinter as tk
from tkinter import messagebox


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def encrypt_text():
    try:
        message = text_input.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        output = caesar_cipher(message, shift, "encrypt")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer")


def decrypt_text():
    try:
        message = text_input.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        output = caesar_cipher(message, shift, "decrypt")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer")


# -------- GUI Setup --------
root = tk.Tk()
root.title("Caesar Cipher Encryption Tool")
root.geometry("500x450")
root.resizable(False, False)

tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Message:").pack()
text_input = tk.Text(root, height=6, width=55)
text_input.pack(pady=5)

tk.Label(root, text="Shift Value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Encrypt", width=15, command=encrypt_text).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Decrypt", width=15, command=decrypt_text).grid(row=0, column=1, padx=10)

tk.Label(root, text="Output:").pack()
text_output = tk.Text(root, height=6, width=55)
text_output.pack(pady=5)

root.mainloop()
