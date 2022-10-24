from operator import index
import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
x_values=[]
y_values=[]

index=count()


# index = count()

def animate(i):
     x_values.append(next(index))
     #sequential
     y_values.append(random.randint(0, 5))
     #random
     plt.cla()
     plt.plot(x_values, y_values)

ani=FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']
