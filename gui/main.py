import tkinter as tk
from tkinter.messagebox import showerror, showinfo

root = tk.Tk()
root.title("Email Checker")

header_text = tk.Label(root, text="Enter your academic e-Mail address")
header_text.pack()

input_box = tk.Entry(root, width=40)
input_box.pack()

def check_email():
    global input_box
    val = input_box.get()
    if not val.endswith("ac.uk"):
        showerror(title="Invalid e-Mail", message="This is not a valid UK academic email address!")
    else:
        showinfo(title="Valid e-Mail", message="Yep, valid email!")

opts = {'fill': 'both', 'padx': 10, 'pady': 16, 'ipadx': 5}
submit_btn = tk.Button(
        root,
        text="Continue",
        command=lambda: check_email()
        ).pack(**opts)

root.mainloop()
