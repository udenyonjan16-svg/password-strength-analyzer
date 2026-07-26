import tkinter as tk
from tkinter import messagebox
import random
import string
import re

# ---------------- Functions ---------------- #

def check_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        result_label.config(text="Weak Password", fg="red")
    elif score <= 4:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showwarning(
                "Invalid Length",
                "Password length must be at least 8."
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        generated_password.delete(0, tk.END)
        generated_password.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter a valid number."
        )


def copy_password():
    password = generated_password.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied successfully!")


def clear_fields():
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password.delete(0, tk.END)
    result_label.config(text="")


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x500")
root.resizable(False, False)

# ---------------- Title ---------------- #

title = tk.Label(
    root,
    text="Password Strength Analyzer and\nSecure Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

# ---------------- Password Section ---------------- #

password_label = tk.Label(
    root,
    text="Enter Password:",
    font=("Arial", 12)
)
password_label.pack()

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    show="*"
)
password_entry.pack(pady=5)

check_button = tk.Button(
    root,
    text="Check Strength",
    command=check_password,
    width=20
)
check_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold")
)
result_label.pack()

# ---------------- Generator Section ---------------- #

length_label = tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12)
)
length_label.pack(pady=(20, 5))

length_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 12),
    justify="center"
)
length_entry.pack()

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
)
generate_button.pack(pady=10)

generated_password = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    justify="center"
)
generated_password.pack()

copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    width=20
)
copy_button.pack(pady=10)

# ---------------- Bottom Buttons ---------------- #

button_frame = tk.Frame(root)
button_frame.pack(pady=25)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=10,
    command=clear_fields
)
clear_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=10,
    command=root.destroy
)
exit_button.grid(row=0, column=1, padx=10)

# ---------------- Run Program ---------------- #

root.mainloop()