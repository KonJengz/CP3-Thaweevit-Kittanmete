from tkinter import *
import math

def calculateBMI(event):
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    calculateBMI = round((weight / (math.pow(height/100,2))),2)
    print(calculateBMI)
    if calculateBMI < 18.5:
        labelResult.configure(text=[calculateBMI, '= คุณผอมเกินไป'])
    elif calculateBMI < 22.9:
        labelResult.configure(text=[calculateBMI, "= น้ำหนักปกติ"])
    elif calculateBMI < 24.9:
        labelResult.configure(text=[calculateBMI, "= น้ำหนักเกิน"])
    elif calculateBMI < 29.9:
        labelResult.configure(text=[calculateBMI, "= คุณอ้วน"])
    else:
        labelResult.configure(text=[calculateBMI, "= คุณอ้วนมาก"])

main =Tk()
labelHeight = Label(main, text="ความสูง(cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(main, text="น้ำหนัก(kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(main, text="คำนวณ")
calculateButton.bind('<Button-1>',calculateBMI)
calculateButton.grid(row=2, column=0)
labelResult = Label(main, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
main.mainloop()