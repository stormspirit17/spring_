# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 03:05:39 2016

@author: Igor
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy
gr = numpy.array(Image.open('1kek.jpg'))

fig = plt.figure()

ax = plt.subplot(111)
im = plt.imshow(numpy.flipud(plt.imread('1kek.jpg')), 
    origin='lower', 
    extent=[29, 45.8, 79265.4, 125918.6])

plt.axis('normal')
t = 407
tt = 307.6
nu = (0.000038*103457)/(8.31*0.5*(t+tt))
v = 0.000032
plist = []
vlist = []
while v < 0.000044:
    p = nu*8.31*t/v
    plist.append(p)
    vlist.append(v*1000000)
    v += 0.0000005
plt.plot(vlist, plist)

vv = 0.000032
pplist = []
vvlist = []
while vv < 0.000044:
    pp = nu*8.31*tt/vv
    pplist.append(pp)
    vvlist.append(vv*1000000)
    vv += 0.0000005
plt.plot(vvlist, pplist)

ppl = []
vvl = []
pr = 105770
vo = 32
while pr < 139920:
    vvl.append(vo)
    ppl.append(pr)
    pr += 10

plt.plot(vvl, ppl)

pol = []
vol = []
pressure = 76921
volume = 44
while pressure < 101781:
    vol.append(volume)
    pol.append(pressure)
    pressure += 10
    
plt.plot(vol, pol)
plt.xticks([30, 32, 35, 40, 44, 45])
plt.yticks([80000, 90000, 98792, 100000, 110000, 120000, 125918.6])
#ax = plt.subplot2grid((1,1),(0,0), rowspan=0, colspan=1)
#ax = plt.axes()
#pos1 = ax.get_position()
#pos2 = [pos1.x0 + 5, pos1.y0 + 5,  pos1.width / 1.0, pos1.height / 1.0] 
#ax.set_position(pos2)
#plt.imshow(gr)
#ax = fig.add_axes([0.2,0.2, 0.6, 0.6], axisbg='none')
#ax.plot([1,2,3], [3,6,1])

plt.show()
