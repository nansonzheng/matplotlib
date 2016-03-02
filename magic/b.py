import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans

fig = plt.figure()

offset = mtrans.Affine2D().translate(-20, 18)

plt.plot(range(30))

plt.scatter([20], [10], transform=offset + plt.gca().transData)

plt.legend(['foo'], loc='best')


fig.savefig('./not_covering_scatter_transform.png')
plt.show()
