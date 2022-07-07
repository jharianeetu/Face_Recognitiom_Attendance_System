from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from chatbot import ChatBot



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #first image
        img=Image.open(r"college_images\Stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #back ground image
        img3=Image.open(r"college_images\wp2551980.jpg")
        img3=img3.resize((1530,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=610)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #=============time===========
        def time():
                string = strftime('%H:%M:%S %p')
                Ibl.config(text=string)
                Ibl.after(1000, time)

        Ibl = Label(title_lbl, font =('time new roman' ,14, 'bold'),background='white',foreground='blue')
        Ibl.place(x=0,y=0,width=110,height=50)
        time()        


        #student button
        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((201,201),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=70,width=201,height=201)
   
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=270,width=201,height=40)

        
        #detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((201,201),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=70,width=201,height=201)
   
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=270,width=201,height=40)


        #attendance button
        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((201,201),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=70,width=201,height=201)
   
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=270,width=201,height=40)



        #chat button
        img_chat=Image.open(r"college_images\chat.jpg")
        img_chat=img_chat.resize((201,201),Image.ANTIALIAS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)

        bChat=Button(bg_img,image=self.photoimg_chat,cursor="hand2",command=self.chatbot)
        bChat.place(x=1100,y=70,width=201,height=201)
   
        b1_Chat=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_Chat.place(x=1100,y=270,width=201,height=40)


        #train button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((201,201),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=330,width=201,height=201)
   
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=530,width=201,height=40)


       
        #Photos button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((201,201),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=330,width=201,height=201)
   
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=530,width=201,height=40)



        #Developer button
        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((201,201),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=330,width=201,height=201)
   
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=530,width=201,height=40)


      
        #Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((201,201),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b1.place(x=1100,y=330,width=201,height=201)
   
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=530,width=201,height=40)

    def open_img(self):
        os.startfile("data")

    def IExit(self):
            self.IExit=tkinter.messagebox.askyesno("Face Recognitin","Are you sure exit this project",parent=self.root)
            if  self.IExit >0:
                self.root.destroy()
            else:
                return           

    #====================functions buttons==================

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)        
  
    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window) 

         

    def chatbot(self):
            self.new_window=Toplevel(self.root)
            self.app=ChatBot(self.new_window)              

            


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()