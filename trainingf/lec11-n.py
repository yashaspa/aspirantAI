class Vector:
    '''Class that represents a vector starting
    from (0,0) and ending at (x,y) in the 2-d plane
    '''
    def __init__(self, xval=0, yval=0):
        self.x = xval
        self.y = yval

    def get_magnitude(self):
        return (self.x*self.x + self.y*self.y)**0.5

    def scalar_multiply(self, val):
        '''multiply x and y by val,
        alter this vector's x and y values'''
        self.x = self.x * val
        self.y = self.y * val

    def __repr__(self):
        '''return a string representation of
        this vector object'''
        #return '(' + str(self.x) + ', ' + str(self.y) + ')'
        return f"({self.x}, {self.y})"
    # 
    # def __str__(self):
    #     '''return a string representation of
    #     this vector object'''
    #     #return '(' + str(self.x) + ', ' + str(self.y) + ')'
    #     return f"({self.x}, {self.y})"


    def __add__(self, other):
        newv = Vector(self.x + other.x, self.y + other.y)
        return newv


def main():
    v1 = Vector(4,3)
    print(v1.x) # 4
    print(v1.y)
    print(v1)
    result = v1.get_magnitude()
    print(result)
    v1.scalar_multiply(2)
    print(v1)

    v2 = Vector()
    print(v2.x)
    print(v2.y)
    print(v2.get_magnitude())

    v3 = v1 + v2


    print([v1,v2,v3])

if __name__ == '__main__':
    main()
