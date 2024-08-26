import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        self.load_tasks()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(padx=10, pady=5)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)
        
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=5)
        
        self.update_task_listbox()
    
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def save_tasks(self):
        with open("todos.txt", 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def load_tasks(self):
        try:
            with open("todos.txt", 'r') as file:
                self.tasks = [line.strip() for line in file]
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
