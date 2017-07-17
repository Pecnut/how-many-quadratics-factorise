from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt
from pylab import rcParams
rcParams.update({'figure.autolayout': True})
rcParams.update({'font.family': 'Arial'})
rcParams['figure.figsize'] = 6,4

def is_square(apositiveint):
  # From https://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
  if apositiveint in [0,1]:
      return True
  else:
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def D(n):
    return sum([int(n/a) for a in range(1,int(n)+1)])

N = 100
quadratics_factorise = [0 for i in range(1,N+1)]

bc_square = []
for n in range(1,N+1):
    for b,c in zip([n-1]*n,range(n)) + zip(range(n-1),[n-1]*(n-1)):
        if b**2-4*c >= 0:
            if is_square(b**2-4*c):
                bc_square.append((b,c))
    quadratics_factorise[n-1] = len(bc_square)/n**2

plt.plot(quadratics_factorise,'C0-',label='actual probability (brute force)')

plt.plot(np.arange(1,N,1),
        [(n + 0.5*(D(n) + int(sqrt(n))))/(n+1)**2
        for n in np.arange(1,N)]
        ,'C1-',label='$P(n)=\left(n+\\frac{D(n)}{2}+\\frac{\\lfloor\sqrt{n}\\rfloor}{2}\\right)/(n+1)^2$')

plt.plot(np.arange(0,N,0.1),[(x*np.log(x) + x*2.14)/(2*(x+1)**2) for x in np.arange(0,N,0.1)],'C2-',label='long-term behaviour')

plt.xlabel('$n$')
plt.ylabel('probability of factorising, for $0\leq b, c \leq n$')
plt.ylim([0,1])
plt.legend()
plt.grid()
plt.show()
