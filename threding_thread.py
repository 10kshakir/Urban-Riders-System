import threading

def mul(num):
      print(num*2)

def square(num):
      print(num*num)

thre_1= threading.Thread(target=mul,args=(10,))
thre_2= threading.Thread(target=square,args=(10,))

thre_1.start()
thre_2.start()