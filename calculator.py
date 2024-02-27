import tkinter as tk
from tkinter import ttk
import math
import random

window = tk.Tk()
window.title("Calculator")
window.geometry("350x350")
window.configure(bg='deepskyblue')

expression = ""  

def press(num):
    """Concatenates digits and operators to the input field"""
    global expression
    expression += str(num)
    input_field.delete(0, tk.END)
    input_field.insert(0, expression)

def equal_press():
    """Evaluates the expression and displays the result"""
    try:
        global expression
        total = str(eval(expression))  
        input_field.delete(0, tk.END)
        input_field.insert(0, total)
    except (SyntaxError, ZeroDivisionError):
        input_field.delete(0, tk.END)
        input_field.insert(0, 'Error')
    expression = ""

def clear():
    """Clears the input/output field"""
    global expression
    expression = ""
    input_field.delete(0, tk.END)

def backspace():
    """Removes the last character from the input field"""
    global expression
    expression = expression[:-1]
    input_field.delete(0, tk.END)
    input_field.insert(0, expression)

def square_root():
    """Calculates the square root of the current expression"""
    global expression
    try:
        result = math.sqrt(eval(expression))
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
        expression = str(result)
    except (SyntaxError, ValueError):
        input_field.delete(0, tk.END)
        input_field.insert(0, 'Error')
    except ZeroDivisionError:
        input_field.delete(0, tk.END)
        input_field.insert(0, 'Undefined')
    expression = ""

def square():
    """Calculates the square of the current expression"""
    global expression
    try:
        result = eval(expression)**2
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
        expression = str(result)
    except (SyntaxError, ValueError):
        input_field.delete(0, tk.END)
        input_field.insert(0, 'Error')
    expression = ""

def percentage():
    """Calculates the percentage of the current expression"""
    global expression
    try:
        result = eval(expression) / 100
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
        expression = str(result)
    except (SyntaxError, ValueError):
        input_field.delete(0, tk.END)
        input_field.insert(0, 'Error')
    expression = ""

def memory_store():
    """Stores the current value in memory"""
    global memory
    memory = input_field.get()

def memory_recall():
    """Recalls the value stored in memory"""
    global expression
    try:
        expression += memory
        input_field.delete(0, tk.END)
        input_field.insert(0, expression)
    except NameError:
        pass

def memory_clear():
    """Clears the value stored in memory"""
    global memory
    try:
        del memory
    except NameError:
        pass

def change_color():
    """Changes the background color of the window"""
    colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightskyblue', 'lightyellow', 'lightgrey',
              'lightseagreen', 'lightsalmon', 'lightcyan', 'lightgoldenrodyellow', 'lightsteelblue', 'lightpink',
              'lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightskyblue', 'lightyellow', 'lightgrey']
    new_color = random.choice(colors)
    window.configure(bg=new_color)
    window.after(random.randint(2000, 3000), change_color)

input_field = ttk.Entry(window, justify='right', font=('verdana', 16, 'bold'))
input_field.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=6)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    ttk.Button(window, text=text, command=lambda text=text: press(text)).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

# Special buttons
ttk.Button(window, text='=', command=equal_press).grid(row=5, column=2, columnspan=2, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='Clear', command=clear).grid(row=5, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='Backspace', command=backspace).grid(row=6, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='√', command=square_root).grid(row=6, column=2, sticky='nsew', padx=5, pady=5)
ttk.Button(window, text='x^2', command=square).grid(row=6, column=3, sticky='nsew', padx=5, pady=5)

# Start color change loop
window.after(2000, change_color)

# Copyright notice
copyright_label = tk.Label(window,  text="\u00A9 2024 Abdullah Al Sady", font=('Arial', 8), bg='deepskyblue')
copyright_label.grid(row=7, column=0, columnspan=5, sticky='nsew')

window.mainloop()
