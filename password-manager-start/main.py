from tkinter import *
import tkinter.messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def gen():
   
    pass_box.insert(0,"Gokul@1447")



def save():
    name=name_box.get()
    email=email_box.get()
    password=pass_box.get()
    

    with open("C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/data.txt","r+") as file:
        old=file.read()
        file.seek(0)
        file.write(f"name:{name} | email:{email} | password:{password}\n"+old)
    name_box.delete(first=0,last="end")
    pass_box.delete(0,"end")
    tkinter.messagebox.showinfo("Message","Info saved")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/logo.png")
canvas.create_image(100,100,image=img)


website_label=Label(text="Website :")
email_label=Label(text="Email/Username :")
pass_label=Label(text="Password :")

name_box=Entry(width=39,)
email_box=Entry(width=39)
pass_box=Entry(width=21,)

email_box.insert(0,"gokulchittepurath3@gmail.com")

genpass_button=Button(text="Generate Password",command=gen)
add_button=Button(text="Add",width=34,command=save)



canvas.grid(column=1 , row=0 )
website_label.grid(column= 0, row=1 ,)
email_label.grid(column=0 , row=2,)
pass_label.grid(column=0 , row=3 )

name_box.grid(row=1,column=1,columnspan=2 )
email_box.grid(column=1,row=2,columnspan=2 )
pass_box.grid(column=1,row=3)

genpass_button.grid(column= 2, row=3 )
add_button.grid(column= 1, row= 4,columnspan=2,pady=10)



window.mainloop()