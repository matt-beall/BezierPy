
from math import sqrt, pow

def point_dist(p1, p2):
    distX = p2[0] - p1[0]
    distY = p2[1] - p1[1]
    dist = sqrt(distX*distX + distY*distY)
    return dist


def scalarMult2D(factor, vector):
    newVec = [vector[0] * factor, vector[1] * factor]
    return newVec

def plus(vec1, vec2):
    a = [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    return a

def minus(vec1, vec2):
    a = [vec1[0] - vec2[0], vec1[1] - vec2[1]]
    return a



#this is a recursive function that works independent of the order of the bezier
def getBezierPoint(points, basis):
    if(len(points) <= 1):
        return points[0]
    else:
        newPs = []
        numP = len(points)
        for i in range(numP - 1):
            v = minus(points[i+1], points[i])
            p = plus(points[i], scalarMult2D(basis, v))
            newPs.append(p)
        return getBezierPoint(newPs, basis)


def integrateBezier(points):
    numPoints = 1000

    basisArray = [i/numPoints for i in range(numPoints)]

    prevP = getBezierPoint(points, 0)
    distSum = 0
    for basis in basisArray:
        thisP = getBezierPoint(points, basis)
        distSum += point_dist(prevP, thisP)
        prevP = thisP
    return distSum


def bezierBasisSplit(bezOrig, basis):
    bezLeft = bezOrig
    bezRight = bezOrig

    x1 = bezOrig[0][0]
    y1 = bezOrig[0][1]
    x2 = bezOrig[1][0]
    y2 = bezOrig[1][1]
    x3 = bezOrig[2][0]
    y3 = bezOrig[2][1]
    x4 = bezOrig[3][0]
    y4 = bezOrig[3][1]
            
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


    bezLeft = [[x1, y1],
                 [x12, y12],
                 [x123, y123],
                 [x1234, y1234]]

    bezRight = [[x1234, y1234],
                  [x234, y234],
                  [x34, y34],
                  [x4, y4]]
    
    return [bezLeft, bezRight]

def getBezierNodeDistance(points):
    d = 0
    d = d + point_dist(points[0],points[1])
    d = d + point_dist(points[1],points[2])
    d = d + point_dist(points[2],points[3])
    return d