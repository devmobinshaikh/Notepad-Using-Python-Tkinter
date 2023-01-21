from tkinter import*
from functools import partial
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile,asksaveasfilename
import tkinter.font as font

def new():
    global file8
    root.title("untitled -Notepad")
    file=None
    text.delete(1.0,END)

def opens():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()
def save():
    global file
    if file==None:
        file = asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
             file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
            print("file Saved!")

    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def stop():
    root.destroy()


def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))

def aboutme():
    showinfo("Notepad","This Notepad is developed by Mobin Shaikh")

def size1():
     top=Toplevel(root,bg="pink")
     top.geometry("300x300")
     v = DoubleVar()
     def submitsize():
         sel =sp.get()
         print(sel)
         Font_tuple = ("Comic Sans MS", sel, "bold")
         text.configure(font=Font_tuple)
         top.destroy()

         # text['font'] = myFont
         # text.update()

     topmsg=Label(top,text="Select Changes ",font=("lucida",'24','bold'),bg="red").pack(padx=10,pady=10)
     fsize=Label(top,text="FontSize",font=("lucida",'12','bold')).place(x=20,y=70)

     sp=Spinbox(top,from_=1,to=56,font=("lucida",'12','bold'),width=8)
     sp.place(x=120,y=71)
     b1=Button(top,text="Save",font=("lucida",'17','bold'),command=submitsize).place(x=120,y=200)
     root.mainloop()








#mainloop

root=Tk()
root.geometry("600x500")
root.title("untitled1-notepad")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=opens)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Exit",command=stop)


edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)

edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="paste",command=paste)

format=Menu(menubar,tearoff=0)
format.add_command(label="Size",command=size1)
menubar.add_cascade(label="Format",menu=format)

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)

helpmenu.add_command(label="about me",command=aboutme)
root.config(menu=menubar)



#add the textarea and scrollbar
Yscroll=Scrollbar(root)
Xscroll=Scrollbar(root,orient='horizontal')

Yscroll.pack(side=RIGHT,fill=Y)
#Xscroll.pack(side=BOTTOM,fill=X)
file=None
text=Text(root,font=("lucida,20,bold"),yscrollcommand=Yscroll.set,xscrollcommand=Xscroll.set)
text.pack(expand=True,fill="both")


root.mainloop()