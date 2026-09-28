import tkinter as tk
from tkinter import messagebox
from functools import partial
from sys import exit
from random import *

root=tk.Tk()
root.title("元气电脑版")
root.geometry("800x500")
root.configure(background="white")
root.minsize(800,500)
root.maxsize(800,500)

atk={
    "单龙":1,
    "双龙":2,
    "魔笛":3,
    "暗杀":4,
    "毁灭":5
}
dfs={
    "防御":[1,2],
    "捂耳":3,
    "护盾":4,
    "抱头":5
}

atklist=["单龙","双龙","魔笛","暗杀","毁灭"]
dfslist=["防御","捂耳","护盾","抱头"]

def on_click(user):
    global usy,aiy,t,uss,ais
    t+=1
    ai=output()
    usz.config(text=str(user))
    aiz.config(text=str(ai))
    jg=judge(user,ai)
    if jg==1:
        uss+=1
        usy=0
        aiy=0
    elif jg==-1:
        ais+=1
        usy=0
        aiy=0
    ussl.config(text=str(uss))
    aisl.config(text=str(ais))
    for i in range(5):
        if i>usy-1:
            atkbtn[i].config(state="disabled")
        else:
            atkbtn[i].config(state="normal")
    if uss >= 11 and uss - ais >= 2:
        messagebox.showinfo("游戏结束","恭喜你，你赢了！")
        exit(0)
    elif ais >= 11 and ais - uss >= 2:
        messagebox.showinfo("游戏结束", "不好意思，你输了，下次走运！")
        exit(0)

fz=48
ussl=tk.Label(
    root,
    text="0",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
aisl=tk.Label(
    root,
    text="0",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
usz=tk.Label(
    root,
    text="",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
aiz=tk.Label(
    root,
    text="",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)

px=5
py=15
fz=32
btna=tk.Button(
    root,
    text="元气",
    command=partial(on_click,"元气"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn1=tk.Button(
    root,
    text="单龙",
    command=partial(on_click,"单龙"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn2=tk.Button(
    root,
    text="双龙",
    command=partial(on_click,"双龙"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn3=tk.Button(
    root,
    text="魔笛",
    command=partial(on_click,"魔笛"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn4=tk.Button(
    root,
    text="暗杀",
    command=partial(on_click,"暗杀"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn5=tk.Button(
    root,
    text="毁灭",
    command=partial(on_click,"毁灭"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnq=tk.Button(
    root,
    text="防御",
    command=partial(on_click,"防御"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnw=tk.Button(
    root,
    text="捂耳",
    command=partial(on_click,"捂耳"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btne=tk.Button(
    root,
    text="护盾",
    command=partial(on_click,"护盾"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnr=tk.Button(
    root,
    text="抱头",
    command=partial(on_click,"抱头"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
atkbtn=[btn1,btn2,btn3,btn4,btn5]
for i in atkbtn:
    i.config(state="disabled")

def output():
    global usy,aiy
    outl=["元气"]
    if t==1:
        return "元气"
    else:
        if aiy>5:
            z1=5
        else:
            z1=aiy
        if usy>5:
            z2=4
        elif usy>=2:
            z2=usy-1
        else:
            z2=usy
        for i in range(z1):
            outl.append(atklist[i])
        for i in range(z2):
            outl.append(dfslist[i])
        chs=choice(outl)
        return chs

def judge(user,ai):
    global usy,aiy
    if user in atklist:
        usy-=atk[user]
        if ai in atklist:
            aiy-=atk[ai]
            if atk[user]>atk[ai]:
                return 1
            elif atk[user]<atk[ai]:
                return -1
            else:
                return 0
        elif ai in dfslist:
            if atk[user]==dfs[ai]:
                return 0
            else:
                if ai=="防御":
                    if user=="单龙" or user=="双龙":
                        return 0
                    else:
                        return 1
                else:
                    return 1
        else:
            aiy+=1
            return 1
    elif user in dfslist:
        if ai in atklist:
            aiy-=atk[ai]
            if atk[ai]==dfs[user]:
                return 0
            else:
                if user=="防御":
                    if ai=="单龙" or ai=="双龙":
                        return 0
                    else:
                        return -1
                else:
                    return -1
        elif ai in dfslist:
            return 0
        else:
            aiy+=1
            return 0
    else:
        usy+=1
        if ai in atklist:
            return -1
        elif ai in dfslist:
            return 0
        else:
            aiy+=1
            return 0

usy=0
aiy=0
uss=0
ais=0
t=0
ussl.place(x=50,y=60,anchor="center")
aisl.place(x=750,y=60,anchor="center")
usz.place(x=300,y=60,anchor="center")
aiz.place(x=500,y=60,anchor="center")
btna.place(x=30,y=120)
btnq.place(x=180,y=120)
btnw.place(x=330,y=120)
btne.place(x=480,y=120)
btnr.place(x=630,y=120)
btn1.place(x=30,y=290)
btn2.place(x=180,y=290)
btn3.place(x=330,y=290)
btn4.place(x=480,y=290)
btn5.place(x=630,y=290)

messagebox.showinfo("欢迎","欢迎来玩元气电脑版！点击确定开始游戏")

root.mainloop()
