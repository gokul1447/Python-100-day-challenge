import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
def cal():
    text=f"is equal to {float(input1.get())*1.609 :.2f} Km"
    label.config(text=text)
radio_state = tkinter.IntVar()
button1= tkinter.Radiobutton(text="Miles to KM",value=1,variable=radio_state)
button2= tkinter.Radiobutton(text="KM to Miles",value=2,variable=radio_state)

button = tkinter.Button(text="Calculate",command=cal)

input1 = tkinter.Entry()
label = tkinter.Label(text="is equal to  0  Km")


input1.grid(column=1,row=2)
button.grid(column=1,row=4)
label.grid(row=3,column=1)
button1.grid(column=0,row=0)
button2.grid(column=0,row=1)

window.mainloop()