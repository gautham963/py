import matplotlib.pyplot as plt

import time as t
x =[1,2,3,4,5]
y=[]
print("Learn to type faster")
f = "faster"
for i in range(0,5):
    time_now = t.time()
    word = str(input("Type the word (faster): "))
    if (f != word):
        print("INVALID word")
    else:
        time_now1 = t.time()
        Print_time = time_now1-time_now
    
        print("Time taken to type: ",Print_time)
        y.append(Print_time)
    continue
plt.xlabel("attempts")
plt.ylabel("Speed")
plt.plot(x,y)
plt.show()

