import matplotlib.pyplot as plt
import numpy as np

grid = np.random.random((10,10))

#~ fig, (ax1) = plt.subplots(nrows=1, figsize=(4,4))
ax.imshow(grid, extent=[0,100,0,1])
ax.set_title('Default')

#~ ax2.imshow(grid, extent=[0,100,0,1], aspect='auto')
#~ ax2.set_title('Auto-scaled Aspect')

#~ ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
#~ ax3.set_title('Manually Set Aspect')

plt.tight_layout()
plt.show()
