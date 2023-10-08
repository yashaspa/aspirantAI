# class Item:
#     def __init__(self, csv_string, store):
#         '''
#         csv_string consists of a string
#         representing a line in one of the sample
#         CSV files, which has the name, price, and
#         category for the item in that order,
#         separated by comma.
#
#         You need to use string methods to
#         break this string up so that you can use
#         the information to initialize the
#         self.name, self.price, and self.category
#         instance variables.
#
#         Remember that the price needs to be
#         converted to a float.
#
#         store is a string representing the store
#         where the item can be found, and should
#         be used to initialize the self.store
#         instance variable.
#         '''
#         self.store = store
#         self.name, self.price, self.category = csv_string.split()
#
#
# class Store:
#     def __init__(self, name, filename):
#         '''The constructor must open the
#         specified file, and for each line
#         (except the first, which has the column
#         titles), it must create an Item object
#         using the data from that line, and append
#         it to the self.items list.
#         '''
#         self.items = []
#         fp = open(filename)
#         lines = fp.readlines()
#         for line in lines[1:]:
#
#             x = Item(line, name)
#             # name, price, category = line.split(',')
#             # ???
#
#             self.items.append(x )
#




#book code
class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        print(self.name, self.quantity)

class Book(Item):
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.author = ''

    def set_author(self, auth):
        self.author = auth

    def display(self):
        '''override display method'''
        print(f"{self.name} by {self.author} {self.quantity}")

class Produce(Item):  # Derived from Item
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.expiration = ''

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration

    def __str__(self):
        return f"{self.name} {self.quantity} {self.expiration}"


class Point:
    def __init__(self, xval,yval):
        self.x = xval
        self.y = yval

def distance(p1, p2):
    '''Calculate distance between 2 points'''
    return ((p1.x - p2.x) ** 2 +
            (p1.y - p2.y) ** 2) ** 0.5


class Polygon:
    def __init__(self, points, color):
        # number of points
        # list of points
        self.color = color
        self.point_list = points

    def get_perimeter(self):
        perim = 0
        for i in range(len(self.point_list)):
            perim += distance(self.point_list[i], self.point_list[i-1])
        return perim


class Quadrilateral(Polygon):
    def __init__(self, pt1, pt2, pt3, pt4, color):
        '''
        '''
        self.point_list = [pt1, pt2, pt3, pt4]
        self.color = color

    def get_perimeter(self):
        '''get perimeter of this quadrilateral'''
        perim = 0
        perim += distance(self.point_list[0], self.point_list[1])
        perim += distance(self.point_list[1], self.point_list[2])
        perim += distance(self.point_list[2], self.point_list[3])
        perim += distance(self.point_list[3], self.point_list[0])
        return perim

    def get_area(self):
        '''get area of this quadrilateral
        '''
        print('too hard!')


class Rectangle(Quadrilateral):
    # no need for __init__ if it's just the same thing
    def get_area(self):
        return (distance(self.point_list[0],self.point_list[1])*
                distance(self.point_list[1], self.point_list[2]))

class Square(Rectangle):
    '''Further specialization
    '''


class Triangle(Polygon):
    def __init__(self, pt1, pt2, pt3,color):
        Polygon.__init__([pt1,pt2,pt3], color)

    def centroid(self):
        cen = Point(x, y)
        return cen


    def get_area(self):
        '''get this triangle's area
        '''

    def get_perimeter(self):
        '''get perimeter of this triangle'''


class C1:

    def __init__(self):
        self.x = 0
        print('hi')

    def stuff(self):
        print('c1 stuff')

class C2:
    def __init__(self):
        self.y = 4
        print('yo')

    def stuff(self):
        print('c2 stuff')


class C3(C1, C2):
    def __init__(self):
        C1.__init__(self)
        C2.__init__(self)


    def __str__(self):
        return f"{self.x} {self.y}"



def longest_perimeter(p_list):
    '''Given a list of Polygon objects, return
    the one with the longest perimeter

    Parameter: p_list - a list of Polygons

    Return Value:
        a polygon with longest perimeter
    '''
    lpoly = p_list[0]
    for p in p_list:
        if p.get_perimeter() > lpoly.get_perimeter():
            lpoly = p
    return lpoly







def main():
    var = C3()
    print(var)
    var.stuff()

    # p1 = Produce()
    # p1.set_name('Orange')
    # p1.set_quantity(2)
    # p1.set_expiration('04-21')
    # p1.display()
    # print(p1)
    #
    # b1 = Book()
    # b1.set_name('Pride and Prejudice')
    # b1.set_author('Jane Austen')
    # b1.set_quantity(5)
    #
    # b1.display()

    #b1.set_expiration('Apr 7')
    #p1.set_author('Andy')
    #
    #
    # q1 = Quadrilateral(Point(0,0), Point(0,4),
    #         Point(3,4), Point(4,0), 'red')
    #
    # print(q1.get_perimeter())
    #
    #
    #
    #



    # r1 = Rectangle(Point(0,0), Point(0,4),
    #         Point(3,4), Point(3,0), 'red')
    #
    # print(r1.get_perimeter())
    #
    #
    # t1 = Triangle(Point(2,0), Point(5,5),
    #         Point(0,3), 'blue')




if __name__ == '__main__':
    main()
