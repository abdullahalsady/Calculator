import tkinter as tk
from tkinter import ttk  # For more modern-looking widgets

window = tk.Tk()
window.title("Calculator")
window.geometry("350x250")  # Adjust the window size as needed
window.configure(bg='deepskyblue')  # Example background color


expression = ""  # Stores the calculation

# Create the input/output field (use ttk.Entry for a modern look)
input_field = ttk.Entry(window, justify='right', font=('verdana', 16, 'bold'))
input_field.grid(row=0, columnspan=4, sticky='nsew', padx=5, pady=6)


def press(num):
    """Concatenates digits to the input field"""
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


# Basic number buttons (using a loop for efficiency)
for i in range(9, -1, -1):
    button = ttk.Button(window, text=str(i), command=lambda i=i: press(i))
    button.grid(row=i // 3 + 1, column=i % 3, sticky='nsew', padx=6, pady=6)

# Other buttons
decimal = ttk.Button(window, text='.', command=lambda: press('.'))
decimal.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)

add = ttk.Button(window, text='+', command=lambda: press('+'))
add.grid(row=1, column=3, sticky='nsew', padx=5, pady=5)

subtract = ttk.Button(window, text='-', command=lambda: press('-'))
subtract.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)

multiply = ttk.Button(window, text='*', command=lambda: press('*'))
multiply.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)

divide = ttk.Button(window, text='/', command=lambda: press('/'))
divide.grid(row=4, column=3, sticky='nsew', padx=5, pady=5)

equal = ttk.Button(window, text='=', command=equal_press)
equal.grid(row=4, column=2, sticky='nsew', padx=6, pady=6)

clear = ttk.Button(window, text='Clear', command=clear)
clear.grid(row=4, column=1, sticky='nsew', padx=5, pady=5)


window.mainloop()
