from tkinter import Button, Entry, Frame, Label, Tk


class FrSuma(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fSuma(self):
        n1=self.txtNum1.get()
        n2=self.txtNum2.get()
        r=float(n1)+float(n2)
        self.txtNum3.delete(0,'end')
        self.txtNum3.insert(0,r)    

    def create_widgets(self):
        self.lblNum1 = Label(self,text="Primer Número: ",bg="yellow")
        self.txtNum1=Entry(self,bg="pink")
        self.lblNum2 = Label(self,text="Segundo Número: ",bg="yellow")
        self.txtNum2=Entry(self,bg="pink")
        self.btn1=Button(self,text="Sumar", command=self.fSuma)
        self.lblNum3 = Label(self,text="Resultado: ",bg="yellow")
        self.txtNum3=Entry(self,bg="cyan")
        self.lblNum1.place(x=10,y=10,width=100, height=30)
        self.txtNum1.place(x=120,y=10,width=100, height=30)
        self.lblNum2.place(x=10,y=50,width=100, height=30)
        self.txtNum2.place(x=120,y=50,width=100, height=30)
        self.btn1.place(x=230,y=50,width=80, height=30)
        self.lblNum3.place(x=10,y=120,width=100, height=30)
        self.txtNum3.place(x=120,y=120,width=100, height=30)



root = Tk()
root.wm_title("Suma de numeros")
app = FrSuma(root) 
app.mainloop()
