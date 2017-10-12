def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    points = []
    for op in ops:
        try:
            points.append(int(op))
        except:
            if (op == "D"):
                points.append(2 * points[len(points) - 1])
            elif (op == "+"):
                points.append(points[len(points) - 1] + points[len(points) - 2])
            elif (op == "C"):
                del points[len(points) - 1]
    return sum(points)

print calPoints(["5","-2","4","C","D","9","+","+"])