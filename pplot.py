import matplotlib.pyplot as plt
import numpy as np

#simple line
"""
plt.plot(range(10))
plt.show()
"""


#boxplot
#credit:http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibLinePlots.html
"""
fig = plt.figure()
ax = fig.add_subplot(111)

x1 = np.random.normal(0,1,50)
x2 = np.random.normal(1,1,50)
x3 = np.random.normal(2,1,50)

ax.boxplot([x1,x2,x3])
plt.show()
"""

