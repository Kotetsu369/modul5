class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self,other_point):
       return (((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0,5)


point_1 = Point(float(input('x1')), float(input('y1')))


x = float(input('x2'))
y = float(input('y2'))
point_2 = Point(x, y)
print('Point1: (', point_1.x, point_1.y,')','Point2: (', point_2.x, point_2.y, ')' )


print(point_1.distance(point_2))





