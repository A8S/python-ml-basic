
import numpy as np

from matplotlib import pyplot as plt


X = np.array([
    [-2,4,-1],
    [4,1,-1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
])

y = np.array([-1,-1,1,1,1])

for d, sample in enumerate(X):

    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=1)

    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=1)

# Print a possible hyperplane, that is seperating the two classes.

plt.plot([-2,6],[6,0.5])
plt.show()