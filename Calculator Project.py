#Importing Modules
from tkinter import *
from math import factorial

# Creating the Main Window
root=Tk()
root.title("My Calculator") 

# Display Field (Input Field)
display=Entry(root,font=("Arail",20),bd=10,relief=RIDGE,justify="right")
display.grid(row=1,columnspan=6,sticky=N+E+W+S)

#Function to Insert Numbers
def get_input(num):
    display.insert(END,num)
#Function to Insert Operators
def get_operation(operator):
    display.insert(END,operator)
#Function to Calculate the Result
def calculate():
    entire_string=display.get()
    try:
        result=eval(entire_string)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR")
#Function to Clear the Display
def clear_all():
    display.delete(0,END)
#Function To clear last element
def undo():
    entire_string=display.get()
    if entire_string:
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"ERROR")
#Function to calculate factorial
def fact():
    try:
        result=factorial(int(display.get()))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR")

#UI DESIGN(BUTTONS)
    #ROW 2
Button(root, text="1", command=lambda:get_input(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root, text="2", command=lambda:get_input(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root, text="3", command=lambda:get_input(3)).grid(row=2,column=2,sticky=N+S+E+W)
Button(root,text="+", command=lambda:get_operation("+")).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text="pi",command=lambda:get_operation("*3.14")).grid(row=2,column=4,sticky=N+S+E+W)
Button(root,text="<-",command=undo).grid(row=2,column=5,sticky=N+S+E+W)
    #ROW 3
Button(root,text="4",command=lambda:get_input(4)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text="5",command=lambda:get_input(5)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text="6",command=lambda:get_input(6)).grid(row=3,column=2,sticky=N+S+E+W)
Button(root,text="-",command=lambda:get_operation("-")).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text="%",command=lambda:get_operation("%")).grid(row=3,column=4,sticky=N+S+E+W)
Button(root, text="x!",command=fact).grid(row=3,column=5,sticky=N+S+E+W)
    #ROW 4
Button(root,text="7",command=lambda:get_input(7)).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text="8",command=lambda:get_input(8)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text="9",command=lambda:get_input(9)).grid(row=4,column=2,sticky=N+S+E+W)
Button(root,text="*",command=lambda:get_operation("*")).grid(row=4,column=3,sticky=N+S+E+W)
Button(root,text="(",command=lambda:get_operation("(")).grid(row=4,column=4,sticky=N+S+E+W)
Button(root,text=")",command=lambda:get_operation(")")).grid(row=4,column=5,sticky=N+S+E+W)
    #ROW 5
Button(root,text="AC",command=clear_all).grid(row=5,column=0,sticky=N+S+E+W)
Button(root,text="0",command=lambda:get_input(0)).grid(row=5,column=1,sticky=N+S+E+W)
Button(root,text=".",command=lambda:get_input(".")).grid(row=5,column=2,sticky=N+S+E+W)
Button(root,text="/",command=lambda:get_operation("/")).grid(row=5,column=3,sticky=N+S+E+W)
Button(root,text="exp",command=lambda:get_operation("**")).grid(row=5,column=4,sticky=N+S+E+W)
Button(root,text="^2",command=lambda:get_operation("**2")).grid(row=5,column=5,sticky=N+S+E+W)
    #ROW 6
# Equals button (spans all columns)
Button(root,text="^3",command=lambda:get_operation("**3")).grid(row=6,column=5,sticky=N+S+E+W)
Button(root,text="=",command=calculate).grid(row=6,columnspan=5,sticky=N+S+E+W)

#Start the GUI
root.mainloop()







       
             
