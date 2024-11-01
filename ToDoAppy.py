import tkinter as tk

checkbox_vars = []

def todoliste():
    task = entry1.get()
    if task:
        var = tk.BooleanVar()
        checkbox_vars.append(var) 

        task_frame = tk.Frame(taskListbox_frame)
        task_frame.pack(fill=tk.X, padx=5, pady=5)

        checkbutton = tk.Checkbutton(
            task_frame,
            text=task,
            variable=var
        )
        checkbutton.pack(side=tk.LEFT)

        entry1.delete(0, tk.END)

root = tk.Tk()
root.config(bg="#2e2e2e")
root.title("Übung 28.10.2024")

label1 = tk.Label(root, text="ToDo eingeben: ", bg="#2e2e2e", fg="white")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

taskListbox_frame = tk.Frame(root, bg="#2e2e2e")
taskListbox_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

button1 = tk.Button(root, text="Hinzufügen", bg="red", fg="white", command=todoliste)
button1.grid(row=0, column=2)

label2 = tk.Label(root, text="", bg="#2e2e2e", fg="white")
label2.grid(row=2, column=0, columnspan=3)

root.mainloop()
