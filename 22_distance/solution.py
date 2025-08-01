def dist(points):
    smallNo = points[0]
    largNo = points[0]

    for i in points:
        if i < smallNo:
            smallNo = i
        elif i > largNo:
            largNo = i

    return largNo - smallNo

  