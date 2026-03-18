from tkinter import *

# morse code data
morse = {}
with open('morse-code.csv') as file:
    file.readline()
    data = file.readlines()
    for line in data:
        info = line.split(',')
        morse[info[0]] = info[1][:-1]

def text_to_morse():
    text = text_input.get()
    result = ""
    for char in text:
        if char.upper() in morse:
            result += morse[char.upper()]
            result += " "
        else:
            result += "/"
    output["text"] = result
    output.config(bg='white')

# UI
window = Tk()
window.title("Morse Code Converter")
window.minsize(height=500, width=350)
window.config(background="black")

title = Label(text="TEXT TO MORSE", fg="white", bg="black", font=("Trebuchet MS", 25, 'bold'))
title.grid(column=0, row=0, columnspan=3, padx=20, pady=20)

input_label = Label(text='Message', fg="black", bg="white", font=("Courier", 12, 'bold'))
input_label.grid(column=0, row=1, pady=10, padx=10)

text_input = Entry(width=50)
text_input.grid(column=1, row=1, padx=20, columnspan=2)

click = Button(text="Enter", font=("Courier", 8, 'bold'), command=text_to_morse, width=10)
click.grid(column=0, row=3, columnspan=3, pady=10)

output_label = Label(text='Output', fg="black", bg="white", font=("Courier", 12, 'bold'))
output_label.grid(column=0, row=4, pady=10)

output = Label(text="", fg="black", bg="black", font=("Courier", 14, 'bold'), wraplength=300, justify="center")
output.grid(column=1, row=4, columnspan=2)


window.mainloop()
