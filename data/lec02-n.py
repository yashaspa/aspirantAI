import math
import turtle

def text_example():
    msg3 = "A'm\"z"
    print(msg3)
    msg4 = """Hello!
My name is Andy"""

    print(msg4)
    msg5 = "Hello!\nMy name is Andy"
    print(msg5)

text_example()

def turtle_module_example():
    t = turtle.Turtle()
    t.forward(50)
    t.left(60)
    t.forward(70)
    sc = t.getscreen()
    sc.exitonclick()

#turtle_module_example()

def math_module_example():
    x = math.pi
    result = math.sin(x)
    print(result)

#math_module_example()

def math_stuff():
    x = 23.2
    y = 0.1
    print(x)
    print(y)
    print(x - y)

    print(5 ** 3)
    print(5 ** (-3))

    print(10001 // 5)
    print(10001 % 5)

#math_stuff()

def very_complex_function(n):
    val = 3 * n + 1
    return val

# result = very_complex_function(6)
# print(result)
# result = very_complex_function(10)
# print(result)

# function with 2 inputs
#  4 times the first input cubed
#  plus 2nd input squared
def one_math_function(num1, num2):
    num3 = 4 * num1 ** 3 + num2 ** 2
    return num3
#
# r = one_math_function(2, 3)
# print(r)
