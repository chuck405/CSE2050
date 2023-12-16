class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __lt__(self, other):
        return Point.dist_from_origin(self) < Point.dist_from_origin(other)

    def __gt__(self, other):
        return Point.dist_from_origin(self) > Point.dist_from_origin(other)

    def __eq__(self, other):
        return Point.dist_from_origin(self) == Point.dist_from_origin(other)    

if __name__ == '__main__':
    p1 = Point(3,4)
    p2 = Point(5,6)
    p3 = Point(-3,-4)
    p4 = Point(-5,-6)
    assert p1.x == 3
    assert p1.y == 4
    assert str(p1) == "Point(3, 4)"
    assert str(p2) == "Point(5, 6)"
    assert p1 < p2
    assert not (p2 < p1)
    assert p2 > p1
    assert not (p1 > p2)
    assert p1 == p3
    assert p2 == p4