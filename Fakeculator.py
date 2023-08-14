from tkinter import *

base=Tk()

base.title("Fakeculator")
base.configure(background="#DFCCFB")
base.geometry("470x780")
base.resizable(0,0)


def click(buttons):
    entry.insert(END,buttons)

def equal():
        y=str(eval(entry.get()))
        entry.delete(0,END)
        entry.insert(0,y)


def clear():
    entry.delete(0,END)

label=Label(base,text="Fakeculator V.0.1",font="bold")
frame=Frame(base,bg="#BEADFA",padx=50,pady=20)
entry=Entry(master=frame,relief=FLAT,borderwidth=20,width=30,bg="white",fg="black",font="bold")

button1=Button(base,text="1",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(1))
button2=Button(base,text="2",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(2))
button3=Button(base,text="3",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(3))
button4=Button(base,text="4",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(4))
button5=Button(base,text="5",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(5))
button6=Button(base,text="6",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(6))
button7=Button(base,text="7",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(7))
button8=Button(base,text="8",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(8))
button9=Button(base,text="9",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(9))
button0=Button(base,text="0",fg="black",font="bold",bg="#D0BFFF",padx=60,pady=30,command=lambda:click(0))

b_add     =Button(base,text="+",fg="black",font="bold",bg="#9F91CC",padx=60,pady=30,command=lambda:click("+"))
b_sub     =Button(base,text="-",fg="black",font=("bold",12),bg="#9F91CC",padx=63,pady=30,command=lambda:click("-"))
b_multiply=Button(base,text="x",fg="black",font="bold",bg="#9F91CC",padx=61,pady=30,command=lambda:click("*"))
b_division=Button(base,text="/",fg="black",font="bold",bg="#9F91CC",padx=63,pady=30,command=lambda:click("/"))
b_modulus =Button(base,text="%",fg="black",font="bold",bg="#9F91CC",padx=58,pady=30,command=lambda:click("%"))

b_clear=Button(base,text="AC",fg="black",font=("bold"),bg="#6F61C0",padx=53,pady=42,command=lambda:clear())
b_equal=Button(base,text="=",fg="white",font=("bold",20),bg="#614BC3",padx=130,pady=30,command=lambda:equal())

label.grid(row=0,column=1,pady=2,padx=3)

frame.grid(row=1,column=0,columnspan=3,padx=15,pady=15)
entry.grid(row=1,column=0,columnspan=3,padx=15,pady=15)

button7.grid(row=2,column=0,pady=2,padx=1)
button8.grid(row=2,column=1,pady=2,padx=1)
button9.grid(row=2,column=2,pady=2,padx=1)

button4.grid(row=3,column=0,pady=2,padx=1)
button5.grid(row=3,column=1,pady=2,padx=1)
button6.grid(row=3,column=2,pady=2,padx=1)

button1.grid(row=4,column=0,pady=2,padx=1)
button2.grid(row=4,column=1,pady=2,padx=1)
button3.grid(row=4,column=2,pady=2,padx=1)

button0.grid(row=5,column=0,pady=2,padx=1)
b_add.grid(row=5,column=1,pady=2,padx=1)
b_sub.grid(row=5,column=2,pady=2,padx=1)

b_multiply.grid(row=6,column=0,pady=2,padx=1)
b_division.grid(row=6,column=1,pady=2,padx=1)
b_modulus.grid(row=6,column=2,pady=2,padx=1)


b_clear.grid(row=7,column=0,pady=2,padx=1)
b_equal.grid(row=7,column=1,columnspan=2,pady=1,padx=1)


base.mainloop()















