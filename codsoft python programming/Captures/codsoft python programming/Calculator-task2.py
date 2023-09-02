import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

# Set custom colors
bg_color = "#282c34"  # Dark background
button_color = "green"  # Button color
text_color = "white"  # Text color
entry_bg_color = "black"  # Entry box color

# Set the overall theme
root.configure(bg=bg_color)

entry = tk.Entry(root, width=20, font=('Arial', 16), bg=entry_bg_color, fg=text_color)
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (value, row, column) in buttons:
    button = tk.Button(root, text=value, width=5, height=2,
                       font=('Arial', 16), bg=button_color, fg=text_color,
                       command=lambda v=value: click_button(v) if v != '=' else calculate())
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 16),
                         bg=button_color, fg=text_color, command=clear_entry)
clear_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

root.mainloop()

