import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import json
import numpy as np

def loadPos():
    with open('pos.json', 'r') as fp:
        data = json.load(fp)
        return data

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# plt.axis('off')
# ax1[1,1,1].axis("off")
fig, ax = plt.subplots(1, 1)


def animate(i):
    data = loadPos()
    print(f"datais {data}")
    xar = []
    yar = []
    pxar = []
    pyar = [] 
    circlex = []
    circley = []
    for pos in data["organ"].values():
        # angle = np.linspace( 0 , 2 * np.pi , 150 ) 
        # radius = 25
        # x = radius * np.cos( angle ) 
        # y = radius * np.sin( angle )
        xar.append(pos[0])
        yar.append(pos[1])
        permx = pos[0]
        permy = pos[1]
    for pos in data["plant"].values():
        pxar.append(pos[0])
        pyar.append(pos[1])
    ax.clear()
    ax.autoscale(False)
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)
    ax.scatter(xar,yar, c="blue")
    ax.scatter(pxar, pyar, c="green")
    #ax.scatter(permx,permy, c="red")
    if "garry" in data["organ"].keys():
        garry = data["organ"] ["garry"]
        ax.scatter(garry[0], garry[1], c="red")
    ax.scatter( permx , permy , s=10000 ,  facecolors='none', edgecolors='blue' )
    print(circley,circlex)
    #ax.plot(circlex[0],circley[0])
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()