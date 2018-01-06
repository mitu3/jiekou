from tkinter import *
import re
root = Tk()
root.title("生成字典")
v1 = StringVar()
v2 = StringVar()

Label(root,text="Key").grid(row=2,column=0)
Label(root,text="Value").grid(row=2,column=4)
e1 = Entry(root,borderwidth=3,textvariable=v1,width = 23)\
    .grid(row=3,column=0,columnspan=4,padx=10,pady=5)

e2 = Entry(root,borderwidth=3,textvariable=v2,width = 23)\
    .grid(row=3,column=4,columnspan=7,padx=10,pady=5)




def add():
    med = ""
    key = str(v1.get())
    value = str(v2.get())
    med = str(t.get("0.0","end"))
    result1 = "\""+key+"\""+":"+"\""+value+"\""
    result2 = ","+"\"" + key + "\"" + ":" + "\"" + value + "\""
    if med is " ":
        t.insert(END, result1)
    else:
        t.insert(END,result2)


def clear():
    t.delete("1.0", END)
    t2.delete("1.0", END)


Button(root,text="Clear",width=9,command=clear)\
    .grid(row=6,column=2,columnspan=2,padx=10,pady=5)



Button(root,text="Add",width=9,command=add)\
    .grid(row=6,column=3,columnspan=4,padx=8,pady=5)


def conversion():
    med = str(t.get("0.0", "end"))
    str_med = "{"+med[1:]+"}"
    str_all = eval(str_med)
    t2.delete("1.0", END)
    t2.insert(END, str_all)

Button(root,text="Conversion",width=9,command=conversion)\
    .grid(row=6,column=6,columnspan=8,padx=8,pady=5)


#{"http": "http://112.114.99.20:8118"}

Label(root,text="Result").grid(row=6,column=0,columnspan=1)
t = Text(root,height=5, width=50)
t.grid(row=7,column=0, columnspan=8,padx=10,pady=5)

Label(root,text="Fnal Result").grid(row=8,column=0,columnspan=1)
t2 = Text(root,height=10, width=50)
t2.grid(row=9,column=0, columnspan=8,padx=8,pady=5)



root.mainloop()