import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.open_add_task_window)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.open_update_task_window)
        self.update_button.pack()

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_task_complete)
        self.complete_button.pack()

        self.load_sample_data()

    def open_add_task_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Task")

        tk.Label(add_window, text="Title:").pack()
        title_entry = tk.Entry(add_window)
        title_entry.pack()

        tk.Label(add_window, text="Description:").pack()
        description_entry = tk.Entry(add_window)
        description_entry.pack()

        tk.Label(add_window, text="Due Date (YYYY-MM-DD):").pack()
        due_date_entry = tk.Entry(add_window)
        due_date_entry.pack()

        add_button = tk.Button(add_window, text="Add Task",
                               command=lambda: self.add_task(title_entry.get(), description_entry.get(), due_date_entry.get(), add_window))
        add_button.pack()

    def open_update_task_window(self):
        selected_idx = self.task_listbox.curselection()
        if selected_idx:
            task_idx = selected_idx[0]
            task = self.tasks[task_idx]

            update_window = tk.Toplevel(self.root)
            update_window.title("Update Task")

            tk.Label(update_window, text="Title:").pack()
            title_entry = tk.Entry(update_window)
            title_entry.insert(tk.END, task.title)
            title_entry.pack()

            tk.Label(update_window, text="Description:").pack()
            description_entry = tk.Entry(update_window)
            description_entry.insert(tk.END, task.description)
            description_entry.pack()

            tk.Label(update_window, text="Due Date (YYYY-MM-DD):").pack()
            due_date_entry = tk.Entry(update_window)
            due_date_entry.insert(tk.END, task.due_date)
            due_date_entry.pack()

            update_button = tk.Button(update_window, text="Update Task",
                                      command=lambda: self.update_task(task_idx, title_entry.get(), description_entry.get(), due_date_entry.get(), update_window))
            update_button.pack()

    def add_task(self, title, description, due_date, window):
        if title and due_date:
            task = Task(title, description, due_date)
            self.tasks.append(task)
            self.update_task_listbox()
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Title and Due Date are required.")

    def update_task(self, task_idx, title, description, due_date, window):
        if 0 <= task_idx < len(self.tasks) and title and due_date:
            task = self.tasks[task_idx]
            task.title = title
            task.description = description
            task.due_date = due_date
            self.update_task_listbox()
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Invalid task index or missing information.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            self.task_listbox.insert(tk.END, f"{idx}. [{status}] {task.title} - Due: {task.due_date}")

    def mark_task_complete(self):
        selected_idx = self.task_listbox.curselection()
        if selected_idx:
            task_idx = selected_idx[0]
            if 0 <= task_idx < len(self.tasks):
                self.tasks[task_idx].completed = True
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "Invalid task index selected.")

    def load_sample_data(self):
        task1 = Task("Complete Project", "Finish the project tasks", "2023-08-31")
        task2 = Task("Buy Groceries", "Get items for dinner", "2023-08-20")
        self.tasks.append(task1)
        self.tasks.append(task2)
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop() 
