

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
    thisPoint = points[0]
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
