from tkinter import *
import tkinter.messagebox
import json
import datetime
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def gen():
   
    pass_box.insert(0,"Gokul@1447")



def save():
    name=name_box.get()
    email=email_box.get()
    password=pass_box.get()
    time=datetime.datetime.now().strftime("%d-%m-%Y %H.%M %p")
   
    
    data_set= {name:{"email":email , "password":password , "time": time}}
    
    try:
        with open("C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/data.json","r") as file:
            # old=file.read()
            # file.seek(0)
            # file.write(f"name:{name} | email:{email} | password:{password}\n"+old)
            data=json.load(file)
         
            data.update(data_set)
            
            
        
    except:
         with open("C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/data.json","w") as file:
            
            json.dump(data_set,file,indent=2)
    else:
        with open("C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/data.json","w") as file:
            
            json.dump(data,file,indent=2)

            
    name_box.delete(first=0,last="end")
    pass_box.delete(0,"end")
    tkinter.messagebox.showinfo("Message","Info saved")
def search():
    data_s=name_box.get()

    with open("C:/Programming/100 days python/Python-100-day-challenge/password-manager-start/data.json","r") as file:
        
        
        
        data=json.load(file)
        entry=data.get(data_s)
       
            
        if entry:tkinter.messagebox.showinfo("Deatails",f"email:{data[data_s]["email"]} , password:{data[data_s]["password"]}")
        else: tkinter.messagebox.showwarning("Warning", f"{data_s} is not found")

        

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

name_box=Entry(width=21,)
email_box=Entry(width=39)
pass_box=Entry(width=21,)

email_box.insert(0,"gokulchittepurath3@gmail.com")

genpass_button=Button(text="Generate Password",command=gen)
add_button=Button(text="Add",width=34,command=save)
search_button=Button(text="Search",command=search )



canvas.grid(column=1 , row=0 )
website_label.grid(column= 0, row=1 ,)
email_label.grid(column=0 , row=2,)
pass_label.grid(column=0 , row=3 )

name_box.grid(row=1,column=1)
email_box.grid(column=1,row=2,columnspan=2 )
pass_box.grid(column=1,row=3)

genpass_button.grid(column= 2, row=3 )
add_button.grid(column= 1, row= 4,columnspan=2,pady=10)
search_button.grid(row=1,column=2)



window.mainloop()