import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.root.configure(background="#f0f0f0")

        self.password_label = tk.Label(root, text="Generated Password:", background="#f0f0f0")
        self.password_label.pack(pady=10)

        self.password_display = tk.Label(root, text="", background="white", relief="solid", width=20, height=2)
        self.password_display.pack()

        self.length_label = tk.Label(root, text="Password Length:", background="#f0f0f0")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, background="#007acc", fg="white")
        self.generate_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, background="red", fg="white")
        self.quit_button.pack()

    def generate_password(self):
        password_length = int(self.length_entry.get())
        if password_length <= 0:
            self.password_display.config(text="Invalid Length", fg="red")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_display.config(text=generated_password, fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

