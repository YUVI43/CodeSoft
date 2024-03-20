import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input/output
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('=',)
]

# Create buttons and add them to the grid
for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        btn = tk.Button(root, text=label, padx=20, pady=20)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
