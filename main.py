#abdallah_202311568

import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # GUI components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.itemconfig(index, {'bg': 'light grey'})
            messagebox.showinfo("Task Completed", f"Task '{self.tasks[index]}' marked as completed.")

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(task + '\n')
            messagebox.showinfo("Save Successful", "Tasks saved to 'tasks.txt'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving tasks: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoList(root)
    root.mainloop()
