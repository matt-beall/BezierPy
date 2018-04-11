from BezierRecursive import *
import numpy as np
import matplotlib.pyplot as plt
import time

import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

def plotBezier(bezierPoints, minX, minY, maxX, maxY, pointsStyle):

    numPoints = 1000

    basisArray = [i/numPoints for i in range(numPoints)]

    allPoints = []

    for basis in basisArray:
        thisP = getBezierPoint(bezierPoints, basis)
        allPoints.append(thisP)
    

    x = np.array([p[0] for p in allPoints])
    y = np.array([p[1] for p in allPoints])

    xb = np.array([p[0] for p in bezierPoints])
    yb = np.array([p[1] for p in bezierPoints])

    plt.plot(x,y, 'b-')
    plt.axis([minX-1, maxX+1, minY-1, maxY+1])
    plt.grid(True)
    plt.plot(xb,yb, pointsStyle)

def main():

    # x1 = 0.0
    # y1 = 0.0
    # x2 = 1.0
    # y2 = 2.0
    # x3 = 3.0
    # y3 = 0.0
    # x4 = 4.0
    # y4 = 0.0


    x1 = 1.5
    y1 = 0.5

    x2 = 3.1
    y2 = 1215.0
    x3 = 575.0
    y3 = 3075.0
    x4 = 827.0
    y4 = 1.5

    # x1 = 0.0
    # y1 = 36.0981
    # x2 = 0.0
    # y2 = 16.0874
    # x3 = 16.2695
    # y3 = 0.0
    # x4 = 36.0933
    # y4 = 0.0

    x1 = x1 / 72.0
    y1 = y1 / 72.0
    x2 = x2 / 72.0
    y2 = y2 / 72.0
    x3 = x3 / 72.0
    y3 = y3 / 72.0
    x4 = x4 / 72.0
    y4 = y4 / 72.0


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

    plotBezier(bezPoints, minX, minY, maxX, maxY, 'rs')

    bezPoints2 = bezPoints
    bezPoints3 = bezPoints

#    [bezPoints2, bezPoints3] = bezierBasisSplit(bezPoints, basis)

    bezLeft = bezPoints
    bezRight = bezPoints

    bisectPoints = []
    newP = [0,0]

    nodeDist = getBezierNodeDistance(bezLeft)
    integrateDist = integrateBezier(bezLeft)
    print("Init: ", nodeDist, "    ", integrateDist)

    print("Start from left")
    i = 0
    while nodeDist > 0.033:
        newP = getBezierPoint(bezLeft, 0.5)
        bisectPoints.append(newP)
        [bezLeft, bezRight] = bezierBasisSplit(bezLeft, 0.5)
        nodeDist = getBezierNodeDistance(bezLeft)
        integrateDist = integrateBezier(bezLeft)
        i += 1
        print(i, nodeDist,"    ", integrateDist)



    bisectX = np.array([p[0] for p in bisectPoints])
    bisectY = np.array([p[1] for p in bisectPoints])

    print("Start from right")

    bezLeft = bezPoints
    bezRight = bezPoints

    bisectPoints2 = []

    nodeDist = getBezierNodeDistance(bezRight)
    integrateDist = integrateBezier(bezRight)
    i = 0
    while nodeDist > 0.033:
        newP = getBezierPoint(bezRight, 0.5)
        bisectPoints2.append(newP)
        [bezLeft, bezRight] = bezierBasisSplit(bezRight, 0.5)
        nodeDist = getBezierNodeDistance(bezRight)
        integrateDist = integrateBezier(bezRight)
        i += 1
        print(i, nodeDist,"    ", integrateDist)

    bisectX2 = np.array([p[0] for p in bisectPoints2])
    bisectY2 = np.array([p[1] for p in bisectPoints2])

    plt.plot(bisectX,bisectY, 'go')
    plt.plot(bisectX2, bisectY2, 'mo')
    # print(integrateBezier(bezPoints))
    # print(integrateBezier(bezPoints2))
    # print(integrateBezier(bezPoints3))

    # plotBezier(bezPoints2, minX, minY, maxX, maxY, 'go')
    # plotBezier(bezPoints3, minX, minY, maxX, maxY, 'go')

    plt.show()

if __name__ == '__main__':
    main()

