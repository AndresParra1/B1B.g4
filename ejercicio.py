
import math
import cmath
import numpy as np
x1=0.4
y1=1.3
z1=x1+y1
print(z1)

h1=math.cos(x1)
print(h1)

g1=cmath.exp(1j*2*math.pi*x1)
print(g1)

x2=np.array([1,5,7,8,9])
y2=np.array([3,8,2,6,8])
z2=x2+y2
print(z2)

h2=np.cos(x2)
print(h2)

g2=np.exp(1j*2*math.pi*x2)
print(g2)
