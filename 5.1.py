def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    distance = ((a ** 2 + b ** 2) ** 0.5)
    return float("{0:.2f}".format(distance))
