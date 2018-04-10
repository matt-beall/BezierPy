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


    x1 = 0.0
    y1 = 36.0981
    x2 = 0.0
    y2 = 16.0874
    x3 = 16.2695
    y3 = 0.0
    x4 = 36.0933
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

    plotBezier(bezPoints, minX, minY, maxX, maxY, 'rs')

    # plt.show()


    # plt.figure()


    basis = 0.75

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

    print(x1) 
    print(y1)
    print(x12) 
    print(y12)
    print(x123) 
    print(y123)
    print(x1234) 
    print(y1234)


    plotBezier(bezPoints2, minX, minY, maxX, maxY, 'go')
    plotBezier(bezPoints3, minX, minY, maxX, maxY, 'go')

    plt.show()

if __name__ == '__main__':
    main()

