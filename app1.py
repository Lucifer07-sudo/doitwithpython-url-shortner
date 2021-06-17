from tkinter import * 
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners
import pyperclip



class url_shortner:

       
        def create(self):
                if self.url.get() == "":
                        messagebox.showerror("Error","Paste an URL stupid!")
                else:
                        self.urls = self.url.get()
                        self.s = pyshorteners.Shortener()
                        self.short_url = self.s.tinyurl.short(self.urls)
                        
                        self.output = Entry(self.root,font=('verdana',10,'bold'),bg="cyan",fg="black",width=30,relief=GROOVE,borderwidth=2,border=2)
                        self.output.insert(END,self.short_url)
                        self.output.place(x=80,y=120)
        def copy(self):
                if self.url.get()=="":
                        messagebox.showerror("Enter URL you stupid human!")
                else:
                        self.copy_url=self.output.get()
                        pyperclip.copy(self.copy_url)

                        
                        



        
        
        
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('500x200')
                self.root.maxsize(500,200)
                self.root.minsize(500,200)
                self.root.title('Url Shortner')
                self.root['bg'] = "black"

                self.title = Label(self.root,text="URL Shortner by @doiwithpython",font=('verdana',13,'bold'),bg="black",fg="green")
                self.title.place(x=80,y=5)

                self.date = Label(self.root,text=datetime.now().strftime("%d-%m-%Y"),bg="black",fg="red",font=('verdana',8,'bold'))
                self.date.place(x=410,y=5)



                Label(self.root,text="Paste Your Url Here ..",font=('verdana',10,'bold'),bg="black",fg="green").place(x=50,y=50)

                self.url = Entry(self.root,width=50,bg="cyan",relief=GROOVE,borderwidth=2,border=2)
                self.url.place(x=50,y=80)

                self.button = Button(self.root,relief=GROOVE,text="Create",font=('verdana',8,'bold'),bg="cyan",fg="black",command=self.create)
                self.button.place(x=360,y=78)

                self.button = Button(self.root,relief=GROOVE,text="Copy",font=('verdana',8,'bold'),bg="cyan",fg="black",command=self.copy)
                self.button.place(x=430,y=78)

                self.root.mainloop()


if __name__ == '__main__':
        url_shortner()


        