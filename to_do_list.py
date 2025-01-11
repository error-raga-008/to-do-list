import tkinter as tk

my_c = 1

def on_button_click():
    global user_inp
    user_inp = entry.get()

    f1.config(text=user_inp)
    entry.delete(0, tk.END)

    if user_inp == "1":
        f1.config(text="Add A New Task")
        add()
    elif user_inp == "2":
        f1.config(text="Mark A Task Done")
        done()
    else:
        f1.config(text="Error 404")

def add():
    List_widget.delete(1.0, tk.END)
    List_widget.insert(tk.END, "ENTERING A NEW TASK\n")
    button.config(text="+ADD")
    button.config(command=ined)
    
    back_button.place(x=290, y=50)

def ined():
        global my_c
        my_c = 1
        user_inp = entry.get()
        entry.delete(0, tk.END)

        if user_inp == "":
            List_widget.delete(1.0, tk.END)
            List_widget.insert(tk.END, "Enter something\n")
            
        else:
            List_widget.delete(1.0, tk.END)
            List_widget.insert(tk.END, "ENTERING A NEW TASK\n")

            if t1.cget("text") == "":
                if my_c == 1:
                    t1.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 1
                 t1.config(text=f"Task {my_c}:{user_inp}")


            elif t2.cget("text") == "":
                if my_c == 2:
                    t2.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 2
                 t2.config(text=f"Task {my_c}:{user_inp}")

            elif t3.cget("text") == "":
                if my_c == 3:
                    t3.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 3
                 t3.config(text=f"Task {my_c}:{user_inp}")

            elif t4.cget("text") == "":
                if my_c == 4:
                    t4.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 4
                 t4.config(text=f"Task {my_c}:{user_inp}")

            elif t5.cget("text") == "":
                if my_c == 5:
                    t5.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 5
                 t5.config(text=f"Task {my_c}:{user_inp}")

            elif t6.cget("text") == "":
                if my_c == 6:
                    t6.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 6
                 t6.config(text=f"Task {my_c}:{user_inp}")

            elif t7.cget("text") == "":
                if my_c == 7:
                    t7.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 7
                 t7.config(text=f"Task {my_c}:{user_inp}")

            elif t8.cget("text") == "":
                if my_c == 8:
                    t8.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 8
                 t8.config(text=f"Task {my_c}:{user_inp}")

            elif t9.cget("text") == "":
                if my_c == 9:
                    t9.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 9
                 t9.config(text=f"Task {my_c}:{user_inp}")

            elif t0.cget("text") == "":
                if my_c == 10:
                    t0.config(text=f"Task {my_c}:{user_inp}")
                    my_c+=1
                else:
                 my_c = 10
                 t0.config(text=f"Task {my_c}:{user_inp}")
        
            else:
                List_widget.insert(tk.END, "\nComplete REST OF THE TASK\n")

def done():
    List_widget.delete(1.0, tk.END)
    List_widget.insert(tk.END, " Enter the task No.\n You Want To Delete")
    button.config(text="DONE")
    button.config(command=outed)
    
    
    back_button.place(x=290, y=50)

def outed():
    user_inp = entry.get()
    entry.delete(0, tk.END)

    if user_inp == "":
        List_widget.delete(1.0, tk.END)
        List_widget.insert(tk.END, "Enter something\n")
            
    else:
        if user_inp == "1":
            t1.config(text=f"")

        elif user_inp == "2":
            t2.config(text=f"")

        elif user_inp == "3":
            t3.config(text=f"")

        elif user_inp == "4":
            t4.config(text=f"")

        elif user_inp == "5":
            t5.config(text=f"")

        elif user_inp == "6":
            t6.config(text=f"")

        elif user_inp == "7":
            t7.config(text=f"")

        elif user_inp == "8":
            t8.config(text=f"")

        elif user_inp == "9":
            t9.config(text=f"")

        elif user_inp == "10":
            t0.config(text=f"")
    
        else:
            List_widget.insert(tk.END, "\nInvalid Number\n")

def reset_ui():
    # Reset the UI to the original state
    List_widget.delete(1.0, tk.END)
    List_widget.insert(tk.END, "1.Add Task (Enter 1)\n\n")
    List_widget.insert(tk.END, "2.Mark Task Done (Enter 2)\n")
    f1.config(text="")
    button.config(text="Submit")
    button.config(command=on_button_click)
    back_button.place_forget()  # Hide the Back button


root = tk.Tk()
font = ("Arial", 12)  # Use a larger font size
root.configure(background="black")
root.geometry("600x300")  

root.title("TO DO LIST")

# Label
label = tk.Label(root, text="Your to-do list", fg="white", bg="black", font=("Arial", 16))
label.pack()

# Entry field
entry = tk.Entry(root, fg="white", bg="grey", font=("Arial", 12))
entry.pack(side="left", padx=10, pady=2, anchor="nw")
entry.place(x=20, y=50)

# Submit button
button = tk.Button(root, text="Submit", command=on_button_click, fg="white", bg="black", font=font)
button.pack(side="left", pady=1, anchor="nw")
button.place(x=220, y=50)

# Back button (initially hidden)
back_button = tk.Button(root, text="Back", command=lambda: reset_ui(), fg="white", bg="black", font=font)
back_button.place_forget()  # Hide the Back button initially

# Dynamic label for user input
f1 = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 16))
f1.pack(side="left", anchor="nw")
f1.place(x=20, y=73) 

# Task area
List_widget = tk.Text(root, wrap=tk.WORD, height=10, width=40, fg="white", bg="black", font=("Arial", 16))
List_widget.pack(padx=5, pady=5, anchor="nw")
List_widget.place(x=20, y=100, height=110, width=300)

# Initial task list instructions
List_widget.insert(tk.END, "1.Add Task (Enter 1)\n\n")
List_widget.insert(tk.END, "2.Mark Task Done (Enter 2)\n")

# Task container
task_container = tk.Frame(root, bg="black", highlightbackground="grey", highlightthickness=1, width=500, height=300)
task_container.place(x=500, y=25)  
task_container.pack(anchor="ne", expand=True)


#Task List
t1 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t1.pack(fill="both", expand=True)

t2 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t2.pack(fill="both", expand=True)

t3 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t3.pack(fill="both", expand=True)

t4 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t4.pack(fill="both", expand=True)

t5 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t5.pack(fill="both", expand=True)

t6 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t6.pack(fill="both", expand=True)

t7 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t7.pack(fill="both", expand=True)

t8 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t8.pack(fill="both", expand=True)

t9 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t9.pack(fill="both", expand=True)

t0 = tk.Label(task_container, bg="black", highlightbackground="grey", highlightthickness=1,text=f"", fg="white", font=("Arial", 12), anchor="w")
t0.pack(fill="both", expand=True)

root.mainloop()