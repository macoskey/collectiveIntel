# test script - first go-around
# J. Macoskey
# 2/20/17

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import butter, lfilter, freqz
from scipy.optimize import leastsq, minimize
from math import pi

x = 1
if x == 1:
	print 'x is 1'
	print 'still in the block'
print 'done with block'

l1 = np.arange(1,9,1)
print l1
print [v*10 for v in l1 if v >4]
timesten = dict([(v,v*10) for v in l1])
print timesten
#~ plt.plot(l1,l1,'o',color=[1,1,0.5],markersize=90)
#~ plt.show()

