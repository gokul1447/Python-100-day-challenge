from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    count_do(5*60)
def end_time():
    count_no(0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_do(count):
    window.after(1000,count_do,count-1)  
    if count>0:
        canva.itemconfig(count_text,text=f"{int(count/60)}:{count%60}")
# def count_no(count):
#     window.after(1000,count_no,count-1)
#     canva.itemconfig(count_text,text="00:00")
            

            


   


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canva = Canvas(width=200,height=224,highlightthickness=0,bg=YELLOW)
tom_img=PhotoImage(file="C:/Programming/100 days python/pomodoro-start/tomato.png")
canva.create_image(100,112,image=tom_img)
count_text=canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

label = Label(text="Timer",fg=GREEN,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,35,"bold"))
label1 = Label(text="✔",fg=GREEN)
button1=Button(text="start",highlightthickness=0,command=start_time)
button2=Button(text="reset",highlightthickness=0,command=end_time)

label.grid(column=1,row=0)
canva.grid(column=1,row=1)
button1.grid(column=0,row=2)
button2.grid(column=2,row=2)
label1.grid(column=1,row=3)







window.mainloop()
