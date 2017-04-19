# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:30:08 2017

@author: jbrugger
"""


import matplotlib.pyplot as plt
 
fig = plt.figure()
ax = fig.add_subplot(111)

#plotdata = [{"West" : [1,2,3,4,5]}, {"East" : [6,7,8,9,10]}]
plotdata = [[1,2,3,4,5], [6,7,8,9,10]]
    
ax.boxplot(plotdata)
plt.show()


