import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



timeadd = 0
time1 = []
Random=[]
plt.ion()
cnt=0

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ax1.clear()
    ax1.plot(time1, Random)

ani = animation.FuncAnimation (fig, animate, interval=500)
plt.show()

while True:
    RandomNumber = random.randrange(0, 40)
    time.sleep(0.5)
    timeadd += 0.5
    time1.append(timeadd)
    ran = float(RandomNumber)
    Random.append(ran)
    plt.pause(0.000001)
    cnt=cnt+1
    print(f"{Random}, {time1}")
    if(cnt>500):
        Random.pop(0)
        time1.pop(0)

