import tkinter as tk


def button_click(value):
    text_widget.insert(tk.INSERT, str(value))


def calculate():
    expression = text_widget.get("1.0", tk.END).strip()
    try:
        result = eval(expression)
        reset()
        text_widget.insert(tk.END, str(result))
    except SyntaxError:
        reset()
        text_widget.insert(tk.END, "Error")
    except ZeroDivisionError:
        reset()
        text_widget.insert(tk.END, "Error! Division by zero.")


def reset():
    text_widget.delete("1.0", tk.END)


root = tk.Tk()
root.geometry("300x350")
root.title("Calculator")

label = tk.Label(root, text="Calculator", font=("Arial", 15))
label.pack()

# Create text widget
text_widget = tk.Text(root, height=2)
text_widget.pack(padx=20, pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

button7 = tk.Button(button_frame, text="7", font=("Arial", 15), command=lambda: button_click(7))
button7.grid(row=0, column=0, sticky=tk.W+tk.E)

button8 = tk.Button(button_frame, text="8", font=("Arial", 15), command=lambda: button_click(8))
button8.grid(row=0, column=1, sticky=tk.W+tk.E)

button9 = tk.Button(button_frame, text="9", font=("Arial", 15), command=lambda: button_click(9))
button9.grid(row=0, column=2, sticky=tk.W+tk.E)

button_multiply = tk.Button(button_frame, text="*", font=("Arial", 15), command=lambda: button_click("*"))
button_multiply.grid(row=0, column=3, sticky=tk.W+tk.E)

button4 = tk.Button(button_frame, text="4", font=("Arial", 15), command=lambda: button_click(4))
button4.grid(row=1, column=0, sticky=tk.W+tk.E)

button5 = tk.Button(button_frame, text="5", font=("Arial", 15), command=lambda: button_click(5))
button5.grid(row=1, column=1, sticky=tk.W+tk.E)

button6 = tk.Button(button_frame, text="6", font=("Arial", 15), command=lambda: button_click(6))
button6.grid(row=1, column=2, sticky=tk.W+tk.E)

button_subtract = tk.Button(button_frame, text="-", font=("Arial", 15), command=lambda: button_click("-"))
button_subtract.grid(row=1, column=3, sticky=tk.W+tk.E)

button1 = tk.Button(button_frame, text="1", font=("Arial", 15), command=lambda: button_click(1))
button1.grid(row=2, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(button_frame, text="2", font=("Arial", 15), command=lambda: button_click(2))
button2.grid(row=2, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(button_frame, text="3", font=("Arial", 15), command=lambda: button_click(3))
button3.grid(row=2, column=2, sticky=tk.W+tk.E)

button_addition = tk.Button(button_frame, text="+", font=("Arial", 15), command=lambda: button_click("+"))
button_addition.grid(row=2, column=3, sticky=tk.W+tk.E)

button_clear = tk.Button(button_frame, text="CE", font=("Arial", 15), command=reset)
button_clear.grid(row=3, column=0, sticky=tk.W+tk.E)

button0 = tk.Button(button_frame, text="0", font=("Arial", 15), command=lambda: button_click(0))
button0.grid(row=3, column=1, sticky=tk.W+tk.E)

button_divide = tk.Button(button_frame, text="/", font=("Arial", 15), command=lambda: button_click("/"))
button_divide.grid(row=3, column=2, sticky=tk.W+tk.E)

button_equal = tk.Button(button_frame, text="=", font=("Arial", 15), command=calculate)
button_equal.grid(row=3, column=3, sticky=tk.W+tk.E)

button_frame.pack(fill="x")

root.mainloop()
