import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get values from entry boxes and convert to float
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate and display the result
        product = num1 * num2
        result_label.config(text=f"Product: {product}", fg="blue")
    except ValueError:
        # Show an error message if inputs are not numbers
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# 1. Initialize the main window
root = tk.Tk()
root.title("Multiplication Tool")
root.geometry("300x250")

# 2. Add UI Elements
tk.Label(root, text="First Number:").pack(pady=(10, 0))
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Second Number:").pack(pady=(10, 0))
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Multiply", command=calculate_product, bg="lightgrey")
calc_button.pack(pady=20)

# Label to show result
result_label = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
result_label.pack()

# 3. Start the application loop
root.mainloop()

