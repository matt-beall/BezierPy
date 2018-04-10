from BezierRecursive import *
import numpy as np
import matplotlib.pyplot as plt
import time

import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
from math import pi, sin, cos, sqrt

def point_dist(p1, p2):
    distX = p2[0] - p1[0]
    distY = p2[1] - p1[1]
    dist = sqrt(distX*distX + distY*distY)
    return dist

def plotBezier(bezierPoints, minX, minY, maxX, maxY, pointsStyle):

    numPoints = 1000

    basisArray = [i/numPoints for i in range(numPoints)]

    allPoints = []

    prevP = getBezierPoint(bezierPoints, 0)
    distSum = 0
    for basis in basisArray:
        thisP = getBezierPoint(bezierPoints, basis)
        allPoints.append(thisP)
        distSum += point_dist(prevP, thisP)
        prevP = thisP
    
    print("Length: " + str(distSum))

    x = np.array([p[0] for p in allPoints])
    y = np.array([p[1] for p in allPoints])

    xb = np.array([p[0] for p in bezierPoints])
    yb = np.array([p[1] for p in bezierPoints])

    plt.plot(x,y, 'b-')
    plt.axis([minX-1, maxX+1, minY-1, maxY+1])
    plt.grid(True)
    plt.plot(xb,yb, pointsStyle)


    circleBasisArray = [(pi/2)*(val/1000) for val in range(numPoints)]
    thesePoints = []

    for basis in circleBasisArray:
        thisX = cos(basis)
        thisY = sin(basis)
        thesePoints.append([thisX, thisY])

    cx = np.array([p[0] for p in thesePoints])
    cy = np.array([p[1] for p in thesePoints])

    # plt.plot(cx, cy, 'g-')



# fig = plt.figure()

# x1 = 0.0
# y1 = 0.0
# x2 = 1.
# y2 = 1.0
# x3 = 2.
# y3 = -1.
# x4 = 3.
# y4 = 0.0

circleFactor = .5714285714285714
# circleFactor = .551915024494


#Tear Drop from Henry
# x1 = 1.5
# y1 = 0.5

# x2 = 2427.0
# y2 = 2195.0

# x3 = -1617.0
# y3 = 2203

# x4 = 827.5
# y4 = 1.5

#Tear Drop 2 from Henry
# x1 = 1.5
# y1 = 0.5

# x2 = 2403.0
# y2 = 3671.0

# x3 = -1597.0
# y3 = 199

# x4 = 827.5
# y4 = 1.5

# x1 = x1 / 72.0
# y1 = y1 / 72.0

# x2 = x2 / 72.0
# y2 = y2 / 72.0

# x3 = x3 / 72.0
# y3 = y3 / 72.0

# x4 = x4 / 72.0
# y4 = y4 / 72.0

diag = sqrt(pow(12,2) + pow(36,2))

# diagLength = 28.0
diagLength = diag
# diagLength = 36.0

x1 = 0.0
y1 = 0.0

x2 = diagLength*3
y2 = 0.05

x3 = -2.0*diagLength
y3 = 0.05

x4 = diagLength
y4 = 0.0


bezPoints = [[x1, y1],
            [x2, y2],
            [x3, y3],
            [x4, y4]]

# bezierPoints = [[30.0, 0.0],
#                 [14.0, 0.0],
#                 [10.0, 10.0],
#                 [0.0, 10.0],
#                 [0.0, 0.0]]

minX = min([p[0] for p in bezPoints])
minY = min([p[1] for p in bezPoints])

maxX = max([p[0] for p in bezPoints])
maxY = max([p[1] for p in bezPoints])

# plt.axis([minX-1, maxX+1, minY-1, maxY+1])


# plt.show()


# plt.figure()

basis = 0.5

x12 = x1 + (x2 - x1)*basis
y12 = y1 + (y2 - y1)*basis
x23 = x2 + (x3 - x2)*basis
y23 = y2 + (y3 - y2)*basis
x34 = x3 + (x4 - x3)*basis
y34 = y3 + (y4 - y3)*basis
x123 = x12 + (x23 - x12)*basis
y123 = y12 + (y23 - y12)*basis
x234 = x23 + (x34 - x23)*basis
y234 = y23 + (y34 - y23)*basis
x1234 = x123 + (x234 - x123)*basis
y1234 = y123 + (y234 - y123)*basis


bezPoints2 = [[x1, y1],
             [x12, y12],
             [x123, y123],
             [x1234, y1234]]

bezPoints3 = [[x1234, y1234],
              [x234, y234],
              [x34, y34],
              [x4, y4]]

xPoints1 = [x1, x12, x123, x1234, x234, x34, x4]
yPoints1 = [y1, y12, y123, y1234, y234, y34, y4]

fig1 = plt.figure()
plotBezier(bezPoints, minX, minY, maxX, maxY, 'rs')
plt.plot(xPoints1, yPoints1, 'g+', markeredgewidth = 2.0, markersize = 8.0)


fig, ax = plt.subplots()
plotBezier(bezPoints, minX, minY, maxX, maxY, 'rs')
p1, = ax.plot(xPoints1, yPoints1, 'g+', markeredgewidth = 2.0, markersize = 8.0)


aniResolution = 1000.0

resolution = aniResolution / 2.0

def animate(i):
    if(i < resolution):
        newBasis = i / resolution
    else:
        newBasis = (aniResolution - i) / resolution


    x12 = x1 + (x2 - x1)*newBasis
    y12 = y1 + (y2 - y1)*newBasis
    x23 = x2 + (x3 - x2)*newBasis
    y23 = y2 + (y3 - y2)*newBasis
    x34 = x3 + (x4 - x3)*newBasis
    y34 = y3 + (y4 - y3)*newBasis
    x123 = x12 + (x23 - x12)*newBasis
    y123 = y12 + (y23 - y12)*newBasis
    x234 = x23 + (x34 - x23)*newBasis
    y234 = y23 + (y34 - y23)*newBasis
    x1234 = x123 + (x234 - x123)*newBasis
    y1234 = y123 + (y234 - y123)*newBasis

    newX1 = [x1, x12, x123, x1234, x234, x34, x4]
    newY1 = [y1, y12, y123, y1234, y234, y34, y4]

    p1.set_xdata(newX1)
    p1.set_ydata(newY1)

    return p1,


def init():
    newBasis = 0

    x12 = x1 + (x2 - x1)*newBasis
    y12 = y1 + (y2 - y1)*newBasis
    x23 = x2 + (x3 - x2)*newBasis
    y23 = y2 + (y3 - y2)*newBasis
    x34 = x3 + (x4 - x3)*newBasis
    y34 = y3 + (y4 - y3)*newBasis
    x123 = x12 + (x23 - x12)*newBasis
    y123 = y12 + (y23 - y12)*newBasis
    x234 = x23 + (x34 - x23)*newBasis
    y234 = y23 + (y34 - y23)*newBasis
    x1234 = x123 + (x234 - x123)*newBasis
    y1234 = y123 + (y234 - y123)*newBasis

    newX1 = [x1, x12, x123, x1234, x234, x34, x4]
    newY1 = [y1, y12, y123, y1234, y234, y34, y4]

    p1.set_xdata(newX1)
    p1.set_ydata(newY1)

    return p1,

ani = animation.FuncAnimation(fig, animate, np.arange(1, aniResolution),init_func = None, interval = 25, blit = True)
plt.show()

