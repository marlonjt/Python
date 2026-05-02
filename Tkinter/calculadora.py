from tkinter import *

root = Tk()

main_frame = Frame(root)
main_frame.pack()

# variables for calculate in screen
display_text = StringVar()
operation = ""
result = 0
reset_screen = False


# functions clear display for reset display_text and result
def clear_display():
    global result
    display_text.set("")
    result = 0
    init_number.config(text=f"Total: {result}")


# functions for calculate operations
def handle_button_click(keyboard_number):
    global operation, reset_screen
    if reset_screen != False:
        display_text.set(keyboard_number)
        reset_screen = False
    else:
        display_text.set(display_text.get() + keyboard_number)


# function suma for bottom +
def handle_sum(number):
    global operation, result, reset_screen

    try:
        if not reset_screen:
            result += int(number)
            display_text.set(result)
            init_number.config(text=f"Total: {result}")

        operation = "suma"
        reset_screen = True
    except:
        init_number.config(text="Error: Input a number")


# function subtraction for bottom -
def handle_subtraction(number):
    global operation, result, reset_screen

    try:
        if operation == "":
            result = int(number)
        elif operation != "" and reset_screen == False:
            result -= int(number)
            display_text.set(result)
            init_number.config(text=f"Total: {result}")

        operation = "resta"
        reset_screen = True
    except:
        init_number.config(text="Error: Input a number")


# function multiplication for bottom *
def handle_multiplication(number):
    global operation, result, reset_screen

    try:
        if operation == "":
            result = int(number)
        elif operation != "" and reset_screen == False:
            result *= int(number)
            display_text.set(result)
            init_number.config(text=f"Total: {result}")

        operation = "multiplication"
        reset_screen = True
    except:
        init_number.config(text="Error: Input a number")


# function divide for bottom /
def handle_division(number):
    global operation, result, reset_screen

    try:
        if operation == "":
            result = int(number)
        elif operation != "" and reset_screen == False:
            if int(number) == 0:
                init_number.config(text="Cannot divide by zero")
                return

            result /= int(number)
            display_text.set(result)
            init_number.config(text=f"Total: {result}")

        operation = "division"
        reset_screen = True
    except:
        init_number.config(text="Error: Input a number")


# function result with bottom =
def calculate_total():
    global result, operation, reset_screen

    if operation == "suma":
        display_text.set(result + int(display_text.get()))

    if operation == "resta":
        display_text.set(result - int(display_text.get()))

    if operation == "multiplication":
        display_text.set(result * int(display_text.get()))

    if operation == "division":
        display_text.set(result / int(display_text.get()))

    reset_screen = True
    operation = ""


# screen the calculate
screen = Entry(main_frame, bd=5, textvariable=display_text)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")

# Clear display text and operations
init_number = Label(main_frame, text="")
init_number.grid(row=2, column=1, columnspan=3)

btn_clear_display = Button(main_frame, text="C", command=clear_display)
btn_clear_display.grid(row=2, column=4)

# UI Layout: First row of numeric buttons
btn7 = Button(main_frame, text="7", width=3, command=lambda: handle_button_click("7"))
btn7.grid(row=3, column=1)
btn8 = Button(main_frame, text="8", width=3, command=lambda: handle_button_click("8"))
btn8.grid(row=3, column=2)
btn9 = Button(main_frame, text="9", width=3, command=lambda: handle_button_click("9"))
btn9.grid(row=3, column=3)
btnDiv = Button(
    main_frame, text="/", width=3, command=lambda: handle_division(display_text.get())
)
btnDiv.grid(row=4, column=4)

# UI Layout: Second row of numeric buttons
btn4 = Button(main_frame, text="4", width=3, command=lambda: handle_button_click("4"))
btn4.grid(row=4, column=1)
btn5 = Button(main_frame, text="5", width=3, command=lambda: handle_button_click("5"))
btn5.grid(row=4, column=2)
btn6 = Button(main_frame, text="6", width=3, command=lambda: handle_button_click("6"))
btn6.grid(row=4, column=3)
btnMul = Button(
    main_frame,
    text="*",
    width=3,
    command=lambda: handle_multiplication(display_text.get()),
)
btnMul.grid(row=3, column=4)

# UI Layout: Third row of numeric buttons
btn3 = Button(main_frame, text="3", width=3, command=lambda: handle_button_click("3"))
btn3.grid(row=5, column=1)
btn2 = Button(main_frame, text="2", width=3, command=lambda: handle_button_click("2"))
btn2.grid(row=5, column=2)
btn1 = Button(main_frame, text="1", width=3, command=lambda: handle_button_click("1"))
btn1.grid(row=5, column=3)
btnRest = Button(
    main_frame,
    text="-",
    width=3,
    command=lambda: handle_subtraction(display_text.get()),
)
btnRest.grid(row=5, column=4)

# UI Layout: Fourth row of numeric buttons
btn0 = Button(main_frame, text="0", width=3, command=lambda: handle_button_click("0"))
btn0.grid(row=6, column=1)
btnComa = Button(main_frame, text=",", width=3)
btnComa.grid(row=6, column=2)
btnIgual = Button(main_frame, text="=", width=3, command=lambda: calculate_total())
btnIgual.grid(row=6, column=3)
btnSum = Button(
    main_frame, text="+", width=3, command=lambda: handle_sum(display_text.get())
)
btnSum.grid(row=6, column=4)


root.mainloop()
