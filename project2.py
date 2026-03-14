import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Smart Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(root, height=60, bg="lightgrey")
        self.input_frame.pack(fill="both")

        self.input_field = tk.Entry(
            self.input_frame,
            textvariable=self.input_text,
            font=("Arial", 20),
            justify="right",
            bd=5
        )

        self.input_field.pack(fill="both", ipadx=8, ipady=8)

        # Buttons frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.create_buttons()

    def press(self, num):
        self.expression += str(num)
        self.input_text.set(self.expression)

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def create_buttons(self):
        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
            ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
        ]

        for (text,row,col) in buttons:
            tk.Button(
                self.buttons_frame,
                text=text,
                width=8,
                height=3,
                font=("Arial",12),
                command=lambda t=text: self.press(t) if t!="=" else self.equal()
            ).grid(row=row, column=col)

        # Extra buttons
        tk.Button(
            self.buttons_frame,
            text="C",
            width=8,
            height=3,
            font=("Arial",12),
            command=self.clear
        ).grid(row=5, column=0)

        tk.Button(
            self.buttons_frame,
            text="⌫",
            width=8,
            height=3,
            font=("Arial",12),
            command=self.backspace
        ).grid(row=5, column=1)

        tk.Button(
            self.buttons_frame,
            text="(",
            width=8,
            height=3,
            font=("Arial",12),
            command=lambda: self.press("(")
        ).grid(row=5, column=2)

        tk.Button(
            self.buttons_frame,
            text=")",
            width=8,
            height=3,
            font=("Arial",12),
            command=lambda: self.press(")")
        ).grid(row=5, column=3)


# Run the calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
