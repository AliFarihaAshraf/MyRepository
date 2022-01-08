from tkinter import *
class Login:
    def __init__(self,root):
        self.root=root
        self.f1=Frame(self.root,width=400,height=400)
        self.f1.pack(fill="both",expand=True)
        self.b1=Button(self.f1,text="Login")
        self.b1.grid(row=0,column=0)
        self.b2=Button(self.f1,text="New user",command=self.btn_click)
        self.b2.grid(row=0, column=1)

    def btn_click(self):
        self.f1.destroy()
        ob2=Register(self.root)

class Register:
    def __init__(self,root):
        self.root = root
        self.f1=Frame(self.root,width=400,height=400)
        self.f1.pack(fill="both",expand=True)
        self.e1=Entry(self.f1,width=20)
        self.e1.grid(row=0,column=0)
        self.b1=Button(self.f1,text="Register")
        self.b1.grid(row=0, column=1)
        self.b2=Button(self.f1, text="Back", command=self.btn_click_1)
        self.b2.grid(row=0,column=2)

    def btn_click_1(self):
        self.f1.destroy()
        ob2=Login(self.root)

root=Tk()
root.title("This is 1st frame")
root.geometry("400x400")

ob1=Login(root)
#ob2=Register(root)
root.mainloop()
