# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# Defining a class 
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Secure Identity Verification System Using AI & Biometrics")

        #Title label of the project
        title_label = Label(self.root,text="DEVELOPER",font=("Times new roman",35,"bold"),bg="sky blue",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Top Image
        image_top =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\college.jpeg")
        image_top = image_top.resize((1530,760))
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        first_label = Label(self.root,image=self.photoimage_top)
        first_label.place(x=0,y=50,width=1530,height=760)

        #Making a Frame
        main_frame = Frame(first_label,bd=2,bg="sky blue")
        main_frame.place(x=0,y=0,width=1530,height=730)

        info_label = Label(main_frame,text="GROUP : A3_GP_03",font=("Times new roman",27,"bold"),bg="White",fg="black")
        info_label.place(x=0,y=0,width=1530,height=45)

        info1_label = Label(main_frame,text="PROJECT TOPIC: SECURE IDENTITY VERIFICATION USING AI & BIOMETRICS",font=("Times new roman",27,"bold"),bg="White",fg="black")
        info1_label.place(x=0,y=45,width=1530,height=45)

        info3_label = Label(main_frame,text="DEPARTMENT: ARTIFICIAL INTELLIGENCE \n AND DATA SCIENCE",font=("Times new roman",25,"bold"),bg="White",fg="black")
        info3_label.place(x=0,y=95,width=760,height=150)

        info4_label = Label(main_frame,text="TERNA ENGINEERING COLLEGE, NERUL",font=("Times new roman",25,"bold"),bg="White",fg="black")
        info4_label.place(x=765,y=95,width=760,height=150)

        #Making a Frame
        main_frame1 = Frame(first_label,bd=2,bg="light blue")
        main_frame1.place(x=0,y=250,width=760,height=470)
        
        info5_label = Label(main_frame1,text="DEVELOPED BY ",font=("Times new roman",25,"bold"),bg="White",fg="black")
        info5_label.place(x=0,y=0,width=760,height=45)

        info5_label = Label(main_frame1,text="DOCTOR UMERKHAN JUNAIDKHAN (TU8S2425008) \n\n ESAF SHANUM SHAKIL (TU8S2425004) \n\n SHIRSAT BHOOMI SANTOSH (TU8S2425010)  ",
                            font=("Times new roman",22,"bold"),bg="White",fg="black")
        info5_label.place(x=0,y=45,width=760,height=180)

        info5_label = Label(main_frame1,text="PROJECT GUIDE : PROF. SNEHAL MANE",font=("Times new roman",20,"bold"),bg="white",fg="black")
        info5_label.place(x=0,y=230,width=760,height=45)

        image =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT TE 5TH SEM\Images\Terna Engineering College - [TEC], Navi Mumbai.jpg")
        image = image.resize((760,250))
        self.photoimage = ImageTk.PhotoImage(image)

        first_lbl = Label(main_frame1,image=self.photoimage)
        first_lbl.place(x=0,y=280,width=760,height=250)

        #Making a Frame
        main_frame2 = Frame(first_label,bd=2,bg="light blue")
        main_frame2.place(x=765,y=250,width=760,height=470)

        image1 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT TE 5TH SEM\Images\AI-Powered Identity Verification Interface.png")
        image1 = image1.resize((760,470))
        self.photoimage1 = ImageTk.PhotoImage(image1)

        second_lbl = Label(main_frame2,image=self.photoimage1)
        second_lbl.place(x=0,y=0,width=760,height=470)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()            