class Point:
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

def main():
    p1 = Point(0, 0)
    print(p1.x)
    print(p1.y)
    print(p1)
    p1.x = 5
    p1.y = 10
    print(p1.x)
    print(p1.y)
    p2 = Point(22, 31)
    print(p1.x, p1.y)
    print(p2.x, p2.x)


if __name__ == '__main__':
    main()
