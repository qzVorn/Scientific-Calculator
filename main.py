import tkinter as tk
from math import *
from fractions import Fraction

class ScientificCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.configure(bg='#2E8B57')  # Sea green background
        self.window.geometry("400x650")  # Increased height for new button
        
        # Create display with modern styling and rounded corners
        self.display = tk.Entry(self.window, width=20, justify='right', 
                              font=('Arial', 24), bg='white', fg='#2E8B57',
                              bd=10, relief='flat')
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')
        
        # Button layout with fraction button added
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('√', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3),
            ('frac', 7, 0)  # Added fraction button
        ]
        
        # Configure grid weights for responsive layout
        for i in range(8):  # Increased range for new row
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
        
        for (text, row, col) in buttons:
            # Different styling for different button types
            if text in ['=', 'C']:
                bg_color = '#1a5233'  # Darker green for special buttons
            elif text in ['+', '-', '*', '/', '^']:
                bg_color = '#3cb371'  # Medium sea green for operators
            else:
                bg_color = '#4CAF50'  # Regular green for numbers and functions
                
            button = tk.Button(self.window, text=text, 
                             font=('Arial', 14, 'bold'),
                             width=5, height=2,
                             bg=bg_color, fg='white',
                             activebackground='#66bb6a',  # Lighter green when clicked
                             activeforeground='white',
                             relief='raised',  # Changed to raised for 3D effect
                             bd=3,  # Increased border width
                             command=lambda t=text: self.button_click(t))
            
            # Add rounded corners using custom border radius
            button.config(borderwidth=0, highlightthickness=0)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    
    def button_click(self, value):
        if value == '=':
            try:
                # Replace special functions with their math module equivalents
                expression = self.display.get()
                expression = expression.replace('sin', 'sin(radians')
                expression = expression.replace('cos', 'cos(radians')
                expression = expression.replace('tan', 'tan(radians')
                expression = expression.replace('√', 'sqrt')
                expression = expression.replace('^', '**')
                
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        elif value == 'frac':
            try:
                # Get the current expression and evaluate it
                expression = self.display.get()
                if not expression:
                    return
                    
                # Evaluate the expression first if it contains operations
                if any(op in expression for op in ['+', '-', '*', '/', '^']):
                    expression = expression.replace('^', '**')
                    num = eval(expression)
                else:
                    num = float(expression)
                
                # Convert to fraction and format display
                frac = Fraction(num).limit_denominator()
                numerator = frac.numerator
                denominator = frac.denominator
                
                # Format the display to show proper fraction
                if denominator == 1:
                    result = str(numerator)
                else:
                    result = f"{numerator}/{denominator}"
                
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current + value)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.run()
