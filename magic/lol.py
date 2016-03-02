import matplotlib.transforms as mtrans
offset = mtrans.Affine2D().translate(-20, 17)

import matplotlib.pyplot as plt
plt.plot(range(30))
plt.scatter([20], [10], transform=offset + plt.gca().transData)

plt.legend(['foo','foo','foo'],loc='best')

plt.show()
