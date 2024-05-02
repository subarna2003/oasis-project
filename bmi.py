import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi_result.config(text=f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        category_result.config(text=f"Category: {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entry fields for weight and height
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create labels to display BMI result and category
bmi_result = tk.Label(root, text="")
bmi_result.pack()

category_result = tk.Label(root, text="")
category_result.pack()

# Start the GUI event loop
root.mainloop()
