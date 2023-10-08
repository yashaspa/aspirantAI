class Point:
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval


class Quadrilateral:
    def __init__(self,....):

class RightTriangle(Triangle):
    def __init__(self, p1, p2, p3, color, thickness):
        # code to double-check that this is, in fact,
        # a right triangle, give error if not

        Triangle.__init__(self,p1,p2,p3,color,thickness)

    # RightTriangle objects will have all methods of
    # Triangle objects
    def get_area(self):
        # override of get_area method


class Triangle:
    def __init__(self, p1, p2, p3, color, thickness):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.thickness = thickness

    def get_perimeter(self):
        # calculate distance between self.p1, self.p2
        # self.p2, self.p3
        # self.p3, self.p1
        # add it up, return it


    def get_area(self):
        # calculate area of triangle
