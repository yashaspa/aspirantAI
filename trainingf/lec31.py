class Vector:
    '''Class that represents a vector starting
    from (0,0) and ending at (x,y) in the 2-d plane

    '''
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

    # def __str__(self):
    #     '''return a string version of this object'''
    #     return 'test'

    def __repr__(self):
        '''return string representation of
        a Vector object
        '''
        return 'Vector: (' + str(self.x) + ', ' + str(self.y) + ')'

    # I want a method to add two Vector objects
    # __add__ can use + operator
    def __add__(self, other):
        '''add two Vector objects,
        return a Vector that is the sum of those two
        '''
        xresult = self.x + other.x
        yresult = self.y + other.y
        return Vector(xresult, yresult)


    def get_magnitude(self):
        '''this method will return
        the magnitude (i.e. distance from 0,0)
        of this vector'''
        # x*x + y*y
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def scalar_multiply(self, val):
        '''multiply this vector by given scalar
        value val
        '''
        self.x = self.x * val
        self.y = self.y * val

def main():
    v1 = Vector(6,8)
    v2 = Vector(5, -2)
    v3 = v1 + v2
    print(v1)
    print(v2)
    print(v3)
    lst = [v1,v2,v3]
    print(lst)
    # print(v1)
    # print(v1.x)
    #print(v1.yval)
    #print(self.y)
    # print(v1.get_magnitude())

    # v1.scalar_multiply(2)
    # print(v1.x, v1.y)
    # print(v1.get_magnitude())



if __name__ == '__main__':
    main()
