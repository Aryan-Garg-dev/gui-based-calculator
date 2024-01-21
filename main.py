import tkinter as tk

window = tk.Tk()
window.title("PyCalculator")
window.geometry("300x430")

INPUT_FILL = "#B2533E"
OUTPUT_FILL = "#FCE09B"
FILL = "#4F4A45"
WIDTH = 2
LINE_FILL = "#6C5F5B"
FONT = ("Times New Roman", 20, "normal")
input_string = ""


def make_button(loc, tag, button):
    button_dict[tag] = tk.Button(
        master=window,
        width=4, font=FONT, fg="white",
        bg=LINE_FILL, text=f"{button}",
        command=lambda: press(f"{button}")
    )
    canvas.create_window(loc[0], loc[1], window=button_dict[tag])


def press(num):
    global input_string
    input_string += num
    input_label.config(text=input_string)


def evaluate():
    global input_string
    if len(input_string) > 0:
        output = eval(input_string)
        output_label.config(text=output)


def clear():
    global input_string
    input_string = ""
    input_label.config(text="")
    output_label.config(text="")


def percentage():
    global input_string
    input_string += "/100"
    input_label.config(text=input_string)
    output_label.config(text=eval(input_string))


def expo():
    global input_string
    input_string += "**("
    input_label.config(text=input_string)




input_label = tk.Label(window, text="input", bg=INPUT_FILL, width=30, height=2, font=FONT)
input_label.pack()

output_label = tk.Label(window, text="output", bg=OUTPUT_FILL, width=30, height=2, font=FONT)
output_label.pack()

canvas = tk.Canvas(window, height=300, width=300, bg=FILL, borderwidth=0, highlightthickness=0)
canvas.pack()
canvas.create_line(0, 60, 400, 60, fill=LINE_FILL, width=WIDTH)
canvas.create_line(0, 120, 400, 120, fill=LINE_FILL, width=WIDTH)
canvas.create_line(0, 180, 400, 180, fill=LINE_FILL, width=WIDTH)
canvas.create_line(0, 240, 400, 240, fill=LINE_FILL, width=WIDTH)

canvas.create_line(75, 0, 75, 300, fill=LINE_FILL, width=WIDTH)
canvas.create_line(150, 0, 150, 300, fill=LINE_FILL, width=WIDTH)
canvas.create_line(225, 0, 225, 300, fill=LINE_FILL, width=WIDTH)
canvas.create_line(300, 0, 300, 300, fill=LINE_FILL, width=WIDTH)

clear_button = tk.Button(window, text="C", font=FONT, width=4, fg="red", command=clear)
canvas.create_window(38, 30, window=clear_button)
brac1_button = tk.Button(window, text="(", font=FONT, width=2, bg="#8E8FFA", command=lambda: press("("))
canvas.create_window(95, 30, window=brac1_button)
brac2_button = tk.Button(window, text=")", font=FONT, width=2, bg="#B2C8BA", command=lambda: press(")"))
canvas.create_window(130, 30, window=brac2_button)
per_button = tk.Button(window, text="%", font=FONT, width=4, command=percentage)
canvas.create_window(188, 30, window=per_button)
div_button = tk.Button(window, text="/", font=FONT, width=4, command=lambda: press("/"))
canvas.create_window(263, 30, window=div_button)
mul_button = tk.Button(window, text="X", font=FONT, width=4, command=lambda: press("*"))
canvas.create_window(263, 90, window=mul_button)
sub_button = tk.Button(window, text="-", font=FONT, width=4, command=lambda: press("-"))
canvas.create_window(263, 150, window=sub_button)
add_button = tk.Button(window, text="+", font=FONT, width=4, command=lambda: press("+"))
canvas.create_window(263, 210, window=add_button)
eq_button = tk.Button(window, text="=", font=FONT, width=4, bg=INPUT_FILL, command=evaluate)
canvas.create_window(263, 270, window=eq_button)
exp_button = tk.Button(window, text="x^y", font=FONT, width=4, bg=LINE_FILL, fg="white", command=expo)
canvas.create_window(38, 270, window=exp_button)
dec_button = tk.Button(window, text=".", font=FONT, width=4, bg=LINE_FILL, fg="white", command=lambda: press("."))
canvas.create_window(188, 270, window=dec_button)

locations = [(113, 270),
             (38, 210), (113, 210), (188, 210),
             (38, 150), (113, 150), (188, 150),
             (38, 90), (113, 90), (188, 90),
             ]
button_dict = {}
for i in range(len(locations)):
    make_button(locations[i], f"B{i}", i)

window.mainloop()

