# helmed: Nanson Zheng
# https://github.com/matplotlib/matplotlib/issues/1235
#
# description:
# The legend box, when using loc='best' (automatically determine best
# location), will sometimes choose a placement that cover up plotted points.

import matplotlib.pyplot as plt

colors = ['b','g','r']

# Plots 3 points. Note the number of visible points during execution
for n in range(3):
    plt.scatter([n,],[n,],color=colors[n])

# Comment out next line to disable legend
plt.legend(['foo','foo','foo'],loc='best')
plt.gca().set_xlim(-0.5, 2.2)
plt.gca().set_ylim(-0.5, 2.2)

plt.show()
