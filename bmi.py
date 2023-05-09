from tkinter import *


def bmi_calculator():
    w = w_user.get()
    h = h_user.get()

    if w == "" or h == "":
        print("Invalid value!")
    else:
        BMI = float(w) / ((float(h)) /100) ** 2
        calculated_result = display_result(BMI)
        result.config(text=calculated_result)

def display_result(BMI):
    calculated_result = "Your BMI: {}".format(BMI)
    if BMI <= 18.5:
        calculated_result += "\nUnder Weight!"
    elif 18.5 < BMI <= 24.9:
        calculated_result += "\nNormal!"
    elif 25 < BMI <= 29.9:
        calculated_result += "\nOver Weight!"
    elif 30 < BMI <= 34.9:
        calculated_result += "\nObesity (Class 1)"
    elif 35 < BMI <= 39.9:
        calculated_result += "\nObesity (Class 2)"
    else:
        calculated_result += "\nObesity (Class 3)"

    return calculated_result


window = Tk()
window.geometry("300x200")
window.title("BMI Calculator")
window.config(background="#DEFE28")
window.config(padx=20,pady=20)

weight = Label(text="Please enter your weight: kg", bg="DarkBlue", fg="#DEFE28")
weight.pack()
w_user = Entry(width=5)
w_user.pack()

height = Label(text="Please enter your height: cm", bg="DarkBlue", fg="#DEFE28")
height.pack()
h_user = Entry(width=5)
h_user.pack()

button = Button(text="CALCULATE",highlightbackground="DarkBlue", fg="#DEFE28", command=bmi_calculator)
button.pack()

result = Label()
result.pack()

window.mainloop()