class Item:
    def __init__(self, csv_string, store):
        '''
        csv_string consists of a string
        representing a line in one of the sample
        CSV files, which has the name, price, and
        category for the item in that order,
        separated by comma.

        You need to use string methods to
        break this string up so that you can use
        the information to initialize the
        self.name, self.price, and self.category
        instance variables.

        Remember that the price needs to be
        converted to a float.

        store is a string representing the store
        where the item can be found, and should
        be used to initialize the self.store
        instance variable.
        '''
class Store:
    def __init__(self, name, filename):
        '''The constructor must open the
        specified file, and for each line
        (except the first, which has the column
        titles), it must create an Item object
        using the data from that line, and append
        it to the self.items list.
        '''
        self.items = []
        fp = open(filename)
        lines = fp.readlines()
        for line in lines[1:]:
            x = Item(line, name)

class Point:
    def __init__(self, xval,yval):
        self.x = xval
        self.y = yval

def distance(p1, p2):
    '''Calculate distance between 2 points'''
    return ((p1.x - p2.x) ** 2 +
            (p1.y - p2.y) ** 2) ** 0.5

class Shape:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_perimeter(self):
        print('error: unimplemented method get_perimeter')
        # really throw an error
        return 0


class Quadrilateral(Shape):
    def __init__(self, pt1, pt2, pt3, pt4, color):
        self.point_list = [pt1,pt2,pt3,pt4]
        Shape.__init__(self, color)


    def get_perimeter(self):
        '''get perimeter of this quadrilateral'''
        total = 0
        for i in range(len(self.point_list)):
            total += distance(self.point_list[i-1],
                                self.point_list[i])
        return total

    def get_area(self):
        '''do some complicated math to figure
        out area!
        '''
        print('too hard, not implemented')
        return 0.0


class Rectangle(Quadrilateral):
    # def __init__(self, pt1, pt2, pt3, pt4, color)
    #     Quadrilateral.__init__(pt1, pt2, pt3, pt4, color)

    def get_area(self):
        return (distance(self.point_list[0], self.point_list[1]) *
                    distance(self.point_list[1], self.point_list[2]))

class Triangle(Shape):
    def __init__(self, pt1, pt2, pt3,color):
        self.point_list = [pt1, pt2, pt3]
        Shape.__init__(self, color)

    def get_area(self):
        '''do some complicated math to figure
        out area!
        '''

    def get_perimeter(self):
        '''get perimeter of this triangle'''
        total = 0
        for i in range(len(self.point_list)):
            total += distance(self.point_list[i-1],
                                self.point_list[i])
        return total

def get_largest_perimeter(shape_list):
    '''takes in a list of Shape objects
    and returns the one with the largest perimeter
    quad_list: list containing Quadrilaterals or
        and object that is a derived class of Quad

    '''
    highest_perimeter = shape_list[0].get_perimeter()
    highest = shape_list[0]
    for item in shape_list:
        if item.get_perimeter() > highest_perimeter:
            highest = item
            highest_perimeter = item.get_perimeter()

    return highest


def main():
    r1 = Rectangle(Point(0,0), Point(0,4),
            Point(3,4), Point(3,0), 'red')

    print(r1.get_perimeter())

    q1 = Quadrilateral(Point(-1,-1), Point(0,4),
            Point(3,4), Point(3,0), 'red')

    print(q1.get_perimeter())

    t1 = Triangle(Point(2,0), Point(5,5),
            Point(0,3), 'blue')




if __name__ == '__main__':
    main()
