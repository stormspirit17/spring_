# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 03:13:28 2016

@author: LENOVO
"""

import numpy
import time
a = numpy.random.uniform(low=-1000.0, high=1000.0, size=(1500, 1500))
x = numpy.random.uniform(low=-1000.0, high=1000.0, size=1500)
start = time.time()
lol = numpy.linalg.solve(a, x)
stop = time.time()
#numpy.set_printoptions(threshold=numpy.nan)
print('Done in', stop-start, 'seconds')
print(lol)
