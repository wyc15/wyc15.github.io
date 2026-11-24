import tkinter as tk
from functools import partial
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
scr=-1

def start(score):
    frame0.destroy()
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
    global scr
    scr=score

def restore():
    if uss>=scr-1 and uss-ais>0:
        ussl.config(fg="red",text=str(uss))
        aisl.config(fg="black",text=str(ais))
    elif ais>=scr-1 and ais-uss>0:
        ussl.config(fg="black", text=str(uss))
        aisl.config(fg="red", text=str(ais))
    else:
        ussl.config(fg="black",text=str(uss))
        aisl.config(fg="black",text=str(ais))
    usz.config(text="--")
    aiz.config(text="--")
    for i in dfsbtn:
        i.config(state="normal")
    if uss >= scr and uss - ais >= 2:
        usz.config(text="")
        aiz.config(text="")
        aisl.config(fg="gray")
        resbd.config(fg="orange",text="恭喜你胜利了")
    elif ais >= scr and ais - uss >= 2:
        usz.config(text="")
        aiz.config(text="")
        ussl.config(fg="gray")
        resbd.config(fg="gray",text="你虽败犹荣")

def on_click(user):
    global usy,aiy,t,uss,ais
    t+=1
    ai = output()
    jg = judge(user, ai)
    for i in range(5):
        if i > usy - 1:
            atkbtn[i].config(state="disabled")
        else:
            atkbtn[i].config(state="normal")
    root.after(50,lambda:show_moves(user,ai,jg))
    usz.config(text="")
    aiz.config(text="")

def show_moves(user,ai,jg):
    global usy,aiy,t,uss,ais
    usz.config(text=str(user))
    aiz.config(text=str(ai))
    if jg != 0:
        for i in atkbtn:
            i.config(state="disabled")
        for i in dfsbtn:
            i.config(state="disabled")
        if jg == 1:
            uss += 1
            usy = 0
            aiy = 0
        elif jg == -1:
            ais += 1
            usy = 0
            aiy = 0
        root.after(1000, restore)

fz=24
px=5
py=15

frame0=tk.Frame(root,bg="white")

tl=tk.Label(
    frame0,
    text="欢迎来到元气电脑版",
    font=("微软雅黑",48),
    fg="black",
    bg="white"
)

subtl=tk.Label(
    frame0,
    text="请选择分数制并开始游戏",
    font=("微软雅黑",32),
    fg="black",
    bg="white"
)

btnbu=tk.Button(
    frame0,
    text="3分赛",
    command=partial(start,3),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)

btnbl=tk.Button(
    frame0,
    text="7分赛",
    command=partial(start,7),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)

btnra=tk.Button(
    frame0,
    text="11分赛",
    command=partial(start,11),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)

btncl=tk.Button(
    frame0,
    text="21分赛",
    command=partial(start,21),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)

tl.place(x=400,y=100,anchor="center")
subtl.place(x=400,y=200,anchor="center")
btnbu.place(x=110,y=290,width=120,height=90)
btnbl.place(x=260,y=290,width=120,height=90)
btnra.place(x=410,y=290,width=120,height=90)
btncl.place(x=560,y=290,width=120,height=90)

frame0.place(x=0,y=0,relwidth=1,relheight=1)

frame1=tk.Frame(root,bg="white")

fz=32

ussl=tk.Label(
    frame1,
    text="0",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
aisl=tk.Label(
    frame1,
    text="0",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
usz=tk.Label(
    frame1,
    text="--",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)
aiz=tk.Label(
    frame1,
    text="--",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)

resbd=tk.Label(
    frame1,
    text="",
    font=("微软雅黑",fz),
    fg="black",
    bg="white"
)

btna=tk.Button(
    frame1,
    text="元气",
    command=partial(on_click,"元气"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn1=tk.Button(
    frame1,
    text="单龙",
    command=partial(on_click,"单龙"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn2=tk.Button(
    frame1,
    text="双龙",
    command=partial(on_click,"双龙"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn3=tk.Button(
    frame1,
    text="魔笛",
    command=partial(on_click,"魔笛"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn4=tk.Button(
    frame1,
    text="暗杀",
    command=partial(on_click,"暗杀"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btn5=tk.Button(
    frame1,
    text="毁灭",
    command=partial(on_click,"毁灭"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnq=tk.Button(
    frame1,
    text="防御",
    command=partial(on_click,"防御"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnw=tk.Button(
    frame1,
    text="捂耳",
    command=partial(on_click,"捂耳"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btne=tk.Button(
    frame1,
    text="护盾",
    command=partial(on_click,"护盾"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)
btnr=tk.Button(
    frame1,
    text="抱头",
    command=partial(on_click,"抱头"),
    font=("微软雅黑",fz),
    padx=px,
    pady=py
)

atkbtn=[btn1,btn2,btn3,btn4,btn5]
dfsbtn=[btnq,btnw,btne,btnr,btna]

for i in atkbtn:
    i.config(state="disabled")

ussl.place(x=50,y=60,anchor="center")
aisl.place(x=750,y=60,anchor="center")
usz.place(x=300,y=60,anchor="center")
aiz.place(x=500,y=60,anchor="center")
resbd.place(x=400,y=60,anchor="center")
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

def on_key(event):
    if not frame1.winfo_ismapped():
        return
    keymap={
        "a":btna,"q":btnq,"w":btnw,"e":btne,"r":btnr,
        "1":btn1,"2":btn2,"3":btn3,"4":btn4,"5":btn5
    }
    key=event.char.lower()
    btn=keymap.get(key)
    if btn is not None:
        btn.invoke()

root.bind("<Key>",on_key)

usy=0
aiy=0
uss=0
ais=0
t=0

root.mainloop()
