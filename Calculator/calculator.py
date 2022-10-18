from ast import operator
import tkinter as tk
from unicodedata import digit
import math

LARGE_FONT_STYLE = ("Arial", 40, "bold")                        # Variable for the color which depends on font standard form.
SMALL_FONT_STYLE = ("Arial", 16)                                # Variable for the color which depends on color standard form.
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"                                          # Variable for the color which depends on color standard form.
LABEL_COLOR = "#25265E"                                         # Variable for the color which depends on color standard form.

class Calculator:
    def __init__ (self):
        self.window = tk.Tk()           # Creating an instance of Tk initializes this interpreter and creates the root window.
        self.window.geometry("667x667") # Specify the geometry of the window.
        self.window.resizable(0, 0)     # resizable() method is used to allow Tkinter root window to change it’s size according to the users need as well we can prohibit
                                        # resizing of the Tkinter window.So, basically, if user wants to create a fixed size window, this method can be used.

        self.window.title("Calculator")                        # Put the APP title.
        self.total_expression = ""                             # initial status
        self.current_expression = ""                           # initial status

        self.display_frame = self.create_display_frame()                    # assign each variable to the function that used in
        self.total_label, self.label = self.create_display_labels()         # assign each variable to the function that used in

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3), 
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}    # maps the operation sympols
        self.buttons_frame = self.create_buttons_frame()                        # assign each variable to the function that used in
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=2)                        # Helps buttons to expand as we used non-zero weight
        for x in range(1, 6):
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()


    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.Create_len_button()
        self.Create_factorial_button()
        self.Create_sin_button()
        self.Create_cos_button()
        self.Create_tan_button()



    def create_display_labels(self):
        # labeling this variable and adding anchor: where the value will be on screen and the color properties like the text displayed and font size 
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg= LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = SMALL_FONT_STYLE)
        total_label.pack(expand = True, fill = "both") 

        # labeling this variable and adding anchor: where the value will be on screen and the color properties like the text displayed and font size 
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg= LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = LARGE_FONT_STYLE)
        label.pack(expand = True, fill = "both") 

        return total_label, label

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()


    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg= LIGHT_GRAY) # Specify some properties of the frame.
        frame.pack(expand = True, fill = "both")                    # Will allow our frame to expand and fill any empty space around.
        return frame

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg = "#071330", fg = "#FFFFFF", font = DIGITS_FONT_STYLE, borderwidth=0, command= lambda x = digit: self.add_to_expression(x)) # we made x = digit here so we get the value at each loop not only the last value
            button.grid(row= grid_value[0], column=grid_value[1],sticky=tk.NSEW)


    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= lambda x = operator : self.append_operator(x))
            button.grid(row=i, column=4,sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text = "C", bg= "#DD571C", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)           # coulmnspan to make it take more than one coulmn
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text = "x\u00b2", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)           # coulmnspan to make it take more than one coulmn
    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()


    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text = "\u221ax", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)           # coulmnspan to make it take more than one coulmn

    def len_function(self):
        self.current_expression = str(eval(f"math.log({self.current_expression}, math.e)"))

    def Create_len_button(self):
        button = tk.Button(self.buttons_frame,text = "lnx", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.len_function)
        button.grid(row=0, column=5, sticky=tk.NSEW)

    def sin_function(self):
        self.current_expression = str(eval(f"round(math.sin(math.radians({self.current_expression})), 2)"))

    def Create_sin_button(self):
        button = tk.Button(self.buttons_frame,text = "Sinx", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.sin_function)
        button.grid(row=2, column=5, sticky=tk.NSEW)

    def cos_function(self):
        self.current_expression = str(eval(f"round(math.cos(math.B8D8D8({self.current_expression})), 2)"))

    def Create_cos_button(self):
        button = tk.Button(self.buttons_frame,text = "Cosx", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.cos_function)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    def tan_function(self):
        self.current_expression = str(eval(f"round(math.tan(math.radians({self.current_expression})), 2)"))

    def Create_tan_button(self):
        button = tk.Button(self.buttons_frame,text = "Tanx", bg= "#071330", fg = "wHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.tan_function)
        button.grid(row=4, column=5, sticky=tk.NSEW)

    def factorial_function(self):
        self.current_expression = str(eval(f"math.factorial({self.current_expression})"))

    def Create_factorial_button(self):
        button = tk.Button(self.buttons_frame,text = "!", bg= "#071330", fg = "WHITE", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.factorial_function)
        button.grid(row=1, column=5, sticky=tk.NSEW)


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        
        except Exception as e:
            self.current_expression = "Error"
        
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text = "=", bg= "#DD571C", fg = "#FFFFFF", font = DEFAULT_FONT_STYLE, borderwidth=0, command= self.evaluate)
        button.grid(row=4, column=3, columnspan = 2, sticky=tk.NSEW)           # coulmnspan to make it take more than one coulmn

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)                                           # Specify some properties of the frame.
        frame.pack(expand=True, fill = "both")                                  # Will allow our frame to expand and fill any empty space around.
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text= expression)

    def update_label(self):
        self.label.config(text= self.current_expression[:11])

    def run(self):
        self.window.mainloop()  # is a method on the main window which we execute when we want to run our application. This method will loop forever,
                                # waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program
                                #  with a keyboard interrupt in the console.

if __name__ == "__main__":
    calc = Calculator()         # These two lines of codes will run only when calculator.py is run as a script from the terminal.
    calc.run()

