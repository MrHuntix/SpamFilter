import spamDetection as s
from tkinter import *
from tkinter import filedialog



win = Tk()

def fileopen():
    file=filedialog.askopenfilename(parent=win,title="choose a file")
    s=""
    try:
        textread= [line for line in open(file,"r").readlines()]
        for i in textread:
            s=s+i
        t1.insert("1.0",s)
    except :
        pass

def review():
    f=t1.get("1.0",END)
    #print(mailContent)
    a,b=s.spamOrHam(f)
    t2.insert("1.0",a)
    
def clear():
    print("clear is pressed")
    t2.delete("1.0",END)
    t1.delete("1.0",END)
    
browse = Button(win, text="Browse",command = fileopen)
t1 = Text(win, width=150, height=30)
submit= Button(win, text='Submit', command = review)
clear=Button(win,text='Clear', command= clear)
t2 = Text(win, width=150, height=5)

t1.grid(row=0,column=0,columnspan=50)
browse.grid(row=7,column=0,columnspan=8)
submit.grid(row=7,column=10,columnspan=8)
clear.grid(row=7,column=20,columnspan=8)
t2.grid(row=10,column=0,columnspan=50)
win.mainloop()
