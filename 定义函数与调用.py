'''
等比数列
注意察看end=的使用方法。
'''
def f(x):
    a=1
    while a<x:
        print(a,end="\n")
        a=2*a

num = int(input("请输入一个数字 "))
f(num)