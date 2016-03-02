import matplotlib.pyplot as plt
fig = plt.figure()

colors = ['b','g','r']



for n in range(3):
    plt.scatter([n,],[n,],color=colors[n])

plt.legend(['foo','foo','foo'],loc='best')
plt.gca().set_xlim(-0.5, 2.2)
plt.gca().set_ylim(-0.5, 2.2)



fig.savefig('./not_covering_scatter.png')
plt.show()
