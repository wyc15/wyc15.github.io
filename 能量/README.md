# 能量

能量是一个拍手游戏，这是它的电脑版

[回到主站](../)

## 能量 v1

- 能量v1.0，[源代码下载](能量v1/能量v1.0/能量v1.0.py)，初始版本

## 源代码

版本：v1.0

更新时间：2026年3月29日

```python
from random import *
from time import sleep

atk={
    "单枪":1,
    "双枪":2,
    "毁灭":3,
    "雷霆":10
}
dfs={
    "防御":{"df":["单枪"],"cos":0},
    "盾反":{"df":["单枪","双枪","毁灭"],"cos":1},
    "避雷针":{"df":["雷霆"],"cos":5},
}
atklist=["单枪","双枪","毁灭","雷霆"]
dfslist=["防御","盾反","避雷针"]

def output():
    global usn,ain
    outl=["能量"]
    if t==1: #t为本回合轮数
        return "能量"
    else:
        if ain>=10:
            z1=4
        elif ain>=3:
            z1=3
        else:
            z1=ain
        if usn>=10 and ain>=5:
            z2=3
        elif usn>=2 and ain>=1:
            z2=2
        elif usn>=1:
            z2=1
        else:
            z2=0
        for i in range(z1):
            outl.append(atklist[i])
        for i in range(z2):
            outl.append(dfslist[i])
        chs=choice(outl)
        #return outl
        return chs
def check():
    if user=="能量":
        return 0
    elif user in atklist:
        if atk[user]>usn:
            return 1
        else:
            return 0
    elif user in dfslist:
        if dfs[user]["cos"]>usn:
            return 1
        else:
            return 0
    else:
        return -1
def judge():
    global usn,ain
    if user in atklist:
        usn-=atk[user]
        if ai in atklist:
            ain-=atk[ai]
            if atk[user]!=atk[ai]:
                return atk[user]-atk[ai]
            else:
                return 0
        elif ai in dfslist:
            ain-=dfs[ai]["cos"]
            if user in dfs[ai]["df"]:
                if ai=="盾反":
                    return -atk[user]
                else:
                    return 0
            else:
                return atk[user]
        else:
            ain+=1
            return atk[user]
    elif user in dfslist:
        usn-=dfs[user]["cos"]
        if ai in atklist:
            ain-=atk[ai]
            if ai in dfs[user]["df"]:
                if user=="盾反":
                    return atk[ai]
                else:
                    return 0
            else:
                return -atk[ai]
        elif ai in dfslist:
            ain-=dfs[ai]["cos"]
            return 0
        else:
            ain+=1
            return 0
    else:
        usn+=1
        if ai in atklist:
            ain-=atk[ai]
            return -atk[ai]
        elif ai in dfslist:
            ain-=dfs[ai]["cos"]
            return 0
        else:
            ain+=1
            return 0

#快捷输入
fastinput={
    "能量":"a",
    "单枪":"1",
    "双枪":"2",
    "毁灭":"3",
    "雷霆":"4",
    "防御":"q",
    "盾反":"w",
    "避雷针":"e"
}
usb=11
aib=11
usn=0
ain=0
print("欢迎来玩能量人机对战！\n")
sleep(1)
print("能量:a")
print("单枪:1")
print("双枪:2")
print("毁灭:3")
print("雷霆:4")
print("防御:q")
print("盾反:w")
print("避雷针:e")
sleep(1)
print("每人11点生命值，游戏开始！")
print("\n")
sleep(1)
t=0
while True:
    t+=1
    print("请在下一行输入招式：")
    user=input()
    #快捷输入转译
    for i in fastinput:
        if user==fastinput[i]:
            user=i
            break
    ch=check()
    if ch == 1:
        print("你没有" + user + "！请重新输入")
        sleep(0.3)
        continue
    elif ch == -1:
        print("你输入的内容不属于本游戏招式！请重新输入")
        sleep(0.3)
        continue
    ai=output()
    print(ai)
    sleep(0.3)
    jg=judge()
    #print(usn, ain)
    if jg==0:
        continue
    elif jg<0:
        usb+=jg
    else:
        aib-=jg
    sleep(0.3)
    if usb<=0:
        print("\n不好意思，你输了，下次走运！")
        print("AI还剩余" + str(aib) + "点生命值\n")
        break
    elif aib<=0:
        print("\n恭喜你，你赢了！")
        print("你还剩余" + str(usb) + "点生命值\n")
        break
    else:
        print("\n你剩余"+str(usb)+"点生命值")
        print("AI剩余"+str(aib)+"点生命值\n")

sleep(1)
input("关闭窗口或按回车键退出...")
```

## 软件下载

Python编译器：[IDLE](https://www.python.org/downloads/)，[Pycharm](https://www.jetbrains.com/pycharm/)
