# def func():
#     print("这是一个方法还是一个类？")
# func()
#
#
# def myadd(a=1,b=100):
#     result = 0
#     i = a
#     while i <= b:    # 默认值为1+2+3+……+100
#         result += i
#         i += 1
#     return result
# print(myadd(1,500))
import threading

import time

balance=0
f = open("w.txt", "w+",encoding='utf-8')
def mythread(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
def mythread1(n):
    global balance
    balance = balance - n
def run_thread(n):
    for i in range(500):
        mythread(n)
        mythread1(n)
        print(n,i,balance)
        we=str(i)+"--"+str(n)+"--"+str(balance)
        f.write(we)
        f.write('\n')
t1 = threading.Thread(target=run_thread, args=(1,))
t2 = threading.Thread(target=run_thread, args=(2,))
t3 = threading.Thread(target=run_thread, args=(3,))
t4 = threading.Thread(target=run_thread, args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()