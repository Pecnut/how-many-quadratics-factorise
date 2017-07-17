from matplotlib import pyplot as plt
from pylab import rcParams
from matplotlib.patches import Rectangle
import numpy as np
rcParams.update({'figure.autolayout': True})
rcParams.update({'font.family': 'Arial'})
rcParams['figure.figsize'] = 4,4


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

n = 21

bc_square = []
bc_notsquare = []
for b in range(n):
    for c in range(n):
        if b**2-4*c >= 0:
            if is_square(b**2-4*c):
                bc_square.append((b,c))
            else:
                bc_notsquare.append((b,c))
        else:
            bc_notsquare.append((b,c))

#cmap = plt.cm.hot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

plt.xticks(np.arange(0, n+1, 2))
plt.yticks(np.arange(0, n+1, 2))

ax.grid(linestyle=":")

for b, c in bc_square:
    ax.add_artist(Rectangle(xy=(b, c),
                  color='C0',        # I did c**2 to get nice colors from your numbers
                  width=1, height=1))      # Gives a square of area h*h

for alpha in range(30):
    plt.plot(np.arange(0,100,50),[alpha*b-alpha**2 for b in np.arange(0,100,50)],'-',color='C1')
'''
ax.annotate('$\\alpha=$0',xy=(12,0),  xytext=(12,3),arrowprops=dict(fc='C1',ec='C1',arrowstyle="->"))
ax.annotate('$\\alpha=$1',xy=(11,10), xytext=(14,9),arrowprops=dict(fc='C1',ec='C1',arrowstyle="->"))
ax.annotate('$\\alpha=$2',xy=(11,18), xytext=(14,17),arrowprops=dict(fc='C1',ec='C1',arrowstyle="->"))
ax.annotate('$\\alpha=$3',xy=(9,18),  xytext=(4,17),arrowprops=dict(fc='C1',ec='C1',arrowstyle="->"))
'''
'''
for alpha in range(3,4):
    plt.plot(np.arange(0,100,50),[alpha*b-alpha**2 for b in np.arange(0,100,50)],'-',color='C1')
plt.xticks([3,4,5,6, 7, 8, 9,9.66],['$\\alpha$','','','','','','','$n/\\alpha + \\alpha$'])
plt.yticks([0,3,6,9,12,15,18,  20],['0','','','','','','','$n$'])
'''
plt.plot(np.arange(0,100,0.01),[b**2/4. for b in np.arange(0,100,0.01)],'-',color='C3')

plt.xlim([0,n])
plt.ylim([0,n])
plt.xlabel('$b$')
plt.ylabel('$c$',rotation=0)
plt.show()
