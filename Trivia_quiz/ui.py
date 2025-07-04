from tkinter import *
from PIL import Image,ImageTk
from data import Datas
import html
class Ui:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("600x900")
        self.score=0

        self.data=Datas()
        
        bg_img=Image.open("bg.png").resize((600, 900))
        bg_photo=ImageTk.PhotoImage(bg_img)
        self.bg_photo=bg_photo

        self.canvas = Canvas(self.window, width=600, height=900)
        self.canvas.create_image(0,0,image=bg_photo,anchor="nw")
        self.canvas.grid(column=0,row=0)

        self.canvas1=Canvas(self.window,width=480,height=650)
      
        self.qns=self.canvas1.create_text(240,225,text="hello",font=("Helvetica", 15, "italic"),width=400,anchor="center",justify="center")
        self.canvas1.place(x=60,y=150)


        self.change_qn()
      

        def ans_false():
            if self.qnss[1]=="False":
                self.score+=1
                self.canvas1.config(bg="white")
                self.canvas.itemconfig(self.label_score,text=f"Score : {self.score}")
                
                

                print(self.qnss)
                self.change_qn()
            else:
                self.canvas1.config(bg="red")
                self.score=0

        def ans_true():
            if self.qnss[1]=="True":
                self.canvas1.config(bg="white")
                self.score+=1
                self.canvas.itemconfig(self.label_score,text=f"Score : {self.score}")
                print(self.qnss)
                self.change_qn()
            else:
                self.canvas1.config(bg="red")
                self.score=0
         
     
        
      

        

        self.label_score=self.canvas.create_text(495,80,text="Score : 0",font=("Helvetica", 18, "bold"),fill="white")

        true_img=Image.open("true.png").resize((80,80)) 
        true_photo=ImageTk.PhotoImage(true_img)
        self.button_true=Button(image=true_photo,command=ans_true)
    
        false_img=Image.open("false.jpeg").resize((80,80)) 
        false_photo=ImageTk.PhotoImage(false_img)
        self.button_false=Button(image=false_photo,command=ans_false)

              
        
        self.button_true.place(x=400, y=670) 
        self.button_false.place(x=120,y=670)
        
        self.window.mainloop()

    def change_qn(self):
        
        self.qnss=self.data.getQn()

        
        self.canvas1.itemconfig(self.qns,text=html.unescape(self.qnss[0]))

