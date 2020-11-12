import tkinter
from tkinter import *
from tkinter.messagebox import *
import math

# important info
Font = 'Serif'

# important functions


def click_btn_function(event):
    # print("btn clicked")
    # saving the event(the button being clicked) and printing it
    b = event.widget
    text = b['text']
    # printing the same in the textfield

    if text == "=":
        try:
            prev_exp = textfield.get()
            answer = eval(prev_exp)
            textfield.delete(0, END)
            textfield.insert(0, answer)
        except Exception as e:
            print("Error...., e")
            showerror("Error...", e)  # showing error in message box to the user
        return

    if text == "AC":
        textfield.delete(0, END)
        return

    if text == "<==":
        expr = textfield.get()
        expr = expr[0:len(expr)-1]
        textfield.delete(0, END)
        textfield.insert(0, expr)
        return

    textfield.insert(END, text)


# creating window
window = Tk()
window.title("Calculator")
window.geometry("240x230")

# textfield
textfield = Entry(window, font=Font, width=20, justify=CENTER)
textfield.pack(side=TOP, pady=10, fill=X, padx=10)

# adding button frame which will be visible when we will add buttons
buttonframe = Frame(window)
buttonframe.pack(side=TOP, padx=10)

# adding buttons
temp = 1
for i in range(3):
    for j in range(3):
        btn = Button(buttonframe, text=temp, font=Font, width=2, activebackground='orange', activeforeground='white',
                     relief='ridge')
        btn.grid(row=i, column=j)
        temp += 1
        # binding the buttons, when button-1 is clicked it creates an event which is passed to the click_btn_function
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonframe, text='0', font=Font, width=2, activebackground='orange', activeforeground='white',
                 relief='ridge')
zeroBtn.grid(row=3, column=0)
zeroBtn.bind('<Button-1>', click_btn_function)

dotBtn = Button(buttonframe, text='.', font=Font, width=2, activebackground='orange', activeforeground='white',
                relief='ridge')
dotBtn.grid(row=3, column=1)
dotBtn.bind('<Button-1>', click_btn_function)

equalBtn = Button(buttonframe, text='=', font=Font, width=2, activebackground='orange', activeforeground='white',
                  relief='ridge')
equalBtn.grid(row=3, column=2)
equalBtn.bind('<Button-1>', click_btn_function)

list1 = ['+', '-', '*', '/']
idx = 0
j = 3
for i in range(4):
    btn = Button(buttonframe, text=list1[idx], font=Font, width=2, activebackground='orange', activeforeground='white',
                 relief='ridge')
    btn.grid(row=i, column=j)
    idx += 1
    # binding buttons
    btn.bind('<Button-1>', click_btn_function)

clearBtn = Button(buttonframe, text='<==', font=Font, width=8, activebackground='orange', activeforeground='white',
                  relief='ridge')
clearBtn.grid(row=4, column=0, columnspan=2)
clearBtn.bind('<Button-1>', click_btn_function)

allclearBtn = Button(buttonframe, text='AC', font=Font, width=8, activebackground='orange', activeforeground='white',
                     relief='ridge')
allclearBtn.grid(row=4, column=2, columnspan=2)
allclearBtn.bind('<Button-1>', click_btn_function)


window.mainloop()
