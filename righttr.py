#!/usr/bin/env python

import math


class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hypotenuse(self):
        return math.sqrt(self.a**2 + self.b**2)
    
    
def main():
    a = input("Enter length of side a: ")
    b = input("Enter length of side b: ")
    
    rttr = RightTriangle(a,b)
    print "Lenth of side c is: ", rttr.hypotenuse()
    
    
if __name__ == '__main__':
    main()
