from tkinter import *
import requests
import re
root = Tk()
root.title("接口请求")

url = ""
headers = {}
cookies = {}
paramsl = {}
proxies = {}

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()

Label(root,text="URL").grid(row=0,column=0, sticky=W+E)

e1 = Entry(root,textvariable=v1,borderwidth=3,insertbackground = 'blue',width = 50)\
    .grid(row=0,column=1,columnspan=8,padx=10,pady=5)


##返回状态框
e2 = Entry(root,borderwidth=3,textvariable=v2,width = 5,state = 'readonly')\
    .grid(row=7,column=7,padx=10,pady=5)


##cookies框
Label(root,text="cookies").grid(row=4,column=1, sticky=E)
e3 = Entry(root,borderwidth=3,textvariable=v3,width = 20)\
    .grid(row=4,column=2,columnspan=4,padx=10,pady=5,sticky=W)

#header框
Label(root,text="headers").grid(row=3,column=1, sticky=E)
e4 = Entry(root,borderwidth=3,textvariable=v4,width = 20)\
    .grid(row=3,column=2,columnspan=4,padx=10,pady=5,sticky=W)
#params框
Label(root,text="params").grid(row=2,column=1, sticky=E)
e5 = Entry(root,borderwidth=3,textvariable=v5,width = 20)\
    .grid(row=2,column=2,columnspan=4,padx=10,pady=5,sticky=W)
#params框
Label(root,text="proxies").grid(row=6,column=1, sticky=E)
e6 = Entry(root,borderwidth=3,textvariable=v6,width = 20)\
    .grid(row=6,column=2,columnspan=4,padx=10,pady=5,sticky=W)



Label(root,text="Response").grid(row=7,column=0,sticky=W)
t = Text(root,height=30, width=60)
t.grid(row=8,column=0, columnspan=8,padx=10,pady=5)



def cooke():
    t.delete("1.0", END)
    result = str(v1.get())
    paramsj = str(v5.get())
    headerj = str(v4.get())
    cookiej = str(v3.get())
    proxiej = str(v6.get())
    headern = "{" + headerj + "}"
    cookien = "{" + cookiej + "}"
    paramsn = "{" + paramsj + "}"
    proxien = "{" + proxiej + "}"
    paramsl = eval(paramsn)
    headerl = eval(headern)
    cookiel = eval(cookien)
    proxiel = eval(proxien)
    print(paramsl)
    url = result
    global reqall
    if abc is "post":
        reqall = requests.post(url, params=paramsl, headers=headerl, cookies=cookiel, proxies=proxiel)
    else:
        reqall = requests.get(url, params=paramsl, headers=headerl, cookies=cookiel, proxies=proxiel)
    cookie_all = str(reqall.cookies)
    t.delete("1.0", END)
    t.insert(END, cookie_all)


Button(root,text="Cookies",width=10,command=cooke)\
    .grid(row=7,column=1,columnspan=2,sticky=W,padx=10,pady=5)

def heard():
    t.delete("1.0", END)
    result = str(v1.get())
    paramsj = str(v5.get())
    headerj = str(v4.get())
    cookiej = str(v3.get())
    proxiej = str(v6.get())
    headern = "{" + headerj + "}"
    cookien = "{" + cookiej + "}"
    paramsn = "{" + paramsj + "}"
    proxien = "{" + proxiej + "}"
    paramsl = eval(paramsn)
    headerl = eval(headern)
    cookiel = eval(cookien)
    proxiel = eval(proxien)
    print(paramsl)
    url = result
    global reqall
    if abc is "post":
        reqall = requests.post(url, params=paramsl, headers=headerl, cookies=cookiel, proxies=proxiel)
    else:
        reqall = requests.get(url, params=paramsl, headers=headerl, cookies=cookiel, proxies=proxiel)
    heard_all = str(reqall.headers)
    t.delete("1.0", END)
    t.insert(END, heard_all)

Button(root,text="Headers",width=10,command=heard)\
    .grid(row=7,column=3,sticky=W,padx=10,pady=5)


#################"提交comment
def show():
    t.delete("1.0", END)
    result = str(v1.get())
    paramsj = str(v5.get())
    headerj = str(v4.get())
    cookiej = str(v3.get())
    proxiej = str(v6.get())
    headern = "{" + headerj + "}"
    cookien = "{" + cookiej + "}"
    paramsn = "{" + paramsj + "}"
    proxien = "{" + proxiej + "}"
    paramsl = eval(paramsn)
    headerl = eval(headern)
    cookiel = eval(cookien)
    proxiel = eval(proxien)
    url = result
    global reqall
    if abc is "post":
        reqall = requests.post(url,params=paramsl,headers=headerl,cookies=cookiel,proxies=proxiel)
    else :
        reqall = requests.get(url,params=paramsl,headers=headerl,cookies=cookiel,proxies=proxiel)

    reqall1 = str(reqall)
    matchObj = re.match(r"<Response \[(.*?)\]>", reqall1)
    v2.set(matchObj.group(1))
    t.insert(END,reqall.text)


Button(root,text="提交",width=5,command=show)\
    .grid(row=2,column=7,padx=5,pady=5)

#############post or get
group = LabelFrame(root,text="请求形式",padx=1,pady=1)
group.grid(row=1,column=0,rowspan=3,sticky=E)
v = IntVar()
v.set(0)
abc = ""
def r1():
    abc = "get"

def r2():
    abc = "post"

i = 0
for r in [r1]:
    Radiobutton(group,variable=v,text='get',value=i,command=r).grid(row=2,column=0,sticky=W+E,padx=5,pady=5)
    i += 1
for r in [r2]:
    Radiobutton(group, variable=v, text='post', value=i, command=r).grid(row=3,column=0,sticky=W+E,padx=5,pady=5)
    i += 1



root.mainloop()

#'showapi_appid':'51838','showapi_sign':'082607f3423847949e1205234656e295'
#{"http": "http://112.114.99.20:8118"}


