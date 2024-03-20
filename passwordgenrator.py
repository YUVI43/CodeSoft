import random
import string
import tkinter as tk

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI elements
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)
length_entry.insert(tk.END, "12")

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_display = tk.Text(root, height=5, width=50, state=tk.DISABLED)
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
