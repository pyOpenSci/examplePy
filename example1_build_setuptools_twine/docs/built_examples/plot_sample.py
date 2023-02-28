# -*- coding: utf-8 -*-
r"""
Matplotlib example
===============

This is taken from the sphinx gallery documentation :)
"""


from __future__ import division, absolute_import, print_function


import numpy as np
import matplotlib.pyplot as plt

# Enforce the use of default set style

# Create data
x = np.array([3,5,2,4])
y = np.arange(4)

# Plot the average over replicates
f, ax = plt.subplots()
ax.plot(x, y)
ax.set_yticks([0,1,2,3])
ax.set_yticklabels(['A','B','C','D'])
plt.show()
