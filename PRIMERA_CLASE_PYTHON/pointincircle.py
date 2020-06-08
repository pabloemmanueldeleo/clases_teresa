import random
import math
import matplotlib.pyplot as plt


def circle():
    x = []
    y = []
    for i in range(0,100):
        angle = random.uniform(0,1)*(math.pi*2)
        x.append(math.cos(angle));
        y.append(math.sin(angle));
    plt.scatter(x,y)
    plt.show()
circle()