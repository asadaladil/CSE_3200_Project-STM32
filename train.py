import tkinter as tk
from tkinter import messagebox

def Train(parent):
    result = {"value": None}

    input_window = tk.Toplevel(parent)
    input_window.title("Hand Written Digit Testing")
    input_window.geometry("300x150")

    def submit():
        user_input = entry.get()
        try:
            val = int(user_input)
            result["value"] = val
            input_window.destroy() # close window after submission
            print("User Input: ",val)
            
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")

    tk.Label(input_window, text="Enter Actual number:", font=("Arial", 12)).pack(pady=10)
    
    entry = tk.Entry(input_window, font=("Arial", 12))
    entry.pack(pady=5)
    entry.bind('<Return>', lambda event: submit())
    
    tk.Button(input_window, text="Submit", command=submit).pack(pady=20)

    parent.wait_window(input_window) # wait until parent calls 

    return result["value"]