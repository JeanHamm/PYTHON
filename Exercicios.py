import threading
import time

ls = []

def contadore1(n):
    for i in range(1, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.4)

def contadore2(n):
    for i in range(6, n+1):
        print(i)
        ls.append(i)
        time.sleep(3)

x = threading.Thread(target=contadore1, args=(5,))
x.start()

y = threading.Thread(target=contadore2, args=(10,))
y.start()


print(ls)