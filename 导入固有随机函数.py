
import random                           #导入random函数
num=random.randint(0,10)                #产生0-10之间的随机数
print("猜猜是0~10哪个数字？")

while(1):

    temp = input ()
    gess= int(temp)

    if gess==num:
        print("对啦")
        break 
    else:
        print("\n错了,再试试？")

print ("结束了不玩了")
