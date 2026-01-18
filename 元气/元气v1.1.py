from random import *
from time import sleep

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
def check():
    if user=="元气":
        return 0
    elif user in atklist:
        if atk[user]>usy:
            return 1
        else:
            return 0
    elif user in dfslist:
        return 0
    else:
        return -1
def judge():
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
uss=0
ais=0
print("欢迎来玩元气人机对战！")
sleep(1)
print("快捷输入（可选）：")
print("元气：a")
print("单龙：1")
print("双龙：2")
print("魔笛：3")
print("暗杀：4")
print("毁灭：5")
print("防御：q")
print("捂耳：w")
print("护盾：e")
print("抱头：r")
print("\n")
sleep(1)
while True:
    usy=0 #用户元气数变量
    aiy=0 #AI元气数变量
    t=0 #本轮已进行回合数
    while True:
        t+=1
        print("请在下一行输入招式：")
        user=input() #用户输入内容
        #转译
        if user=="a":
            user="元气"
        elif user=="1":
            user="单龙"
        elif user=="2":
            user="双龙"
        elif user=="3":
            user="魔笛"
        elif user=="4":
            user="暗杀"
        elif user=="5":
            user="毁灭"
        elif user=="q":
            user="防御"
        elif user=="w":
            user="捂耳"
        elif user=="e":
            user="护盾"
        elif user=="r":
            user="抱头"
        ch=check()
        if ch==1:
            print("你没有"+user+"！请重新输入")
            sleep(1)
            continue
        elif ch==-1:
            print("你输入的内容不属于本游戏招式！请重新输入")
            sleep(1)
            continue
        ai=output()
        print(ai)
        sleep(1)
        jg=judge()
        if jg==1:
            uss+=1
            break
        elif jg==-1:
            ais+=1
            break
    print(str(uss)+" : "+str(ais))
    sleep(1)
    if uss>=11 and uss-ais>=2:
        print("恭喜你，你赢了！")
        break
    elif ais>=11 and ais-uss>=2:
        print("不好意思，你输了，下次走运！")
        break
sleep(1)
input("输入任意内容退出...")

