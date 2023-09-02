import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.pack()

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.update_contact_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term in contact.name.lower() or search_term in contact.phone:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        selected_idx = self.contact_listbox.curselection()
        if selected_idx:
            contact_idx = selected_idx[0]
            contact = self.contacts[contact_idx]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact.name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact.phone)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact.email)
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact.address)

            self.contacts.pop(contact_idx)
            self.update_contact_listbox()

    def delete_contact(self):
        selected_idx = self.contact_listbox.curselection()
        if selected_idx:
            contact_idx = selected_idx[0]
            self.contacts.pop(contact_idx)
            self.update_contact_listbox()
            self.clear_entry_fields()

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

