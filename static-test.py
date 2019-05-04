class A():
    __x = 0
    def __init__(self):
        self._y = 0
    
    @staticmethod
    def x_():
        return A.__x
    
    @property
    def x(self):
        return A.__x
    
    @x.setter
    def x(self, value):
        A.__x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

print(f"A.x = {A.x_()}")

a = A()
a.x = 1
a.y = 2

b = A()

print(f"A({a.x}, {a.y}) <=> B({b.x}, {b.y})")
print(f"A.x = {A.x_()}")

# [Running] python -u "d:\dev\test\python\static-test.py"
# A.x = 0
# A(1, 2) <=> B(1, 0)
# A.x = 1
# [Done] exited with code=0 in 0.561 seconds

""" You can observe that:
1. variable A.__x being a class variable exist before any instances be created (with value 0)
2. x is an object property that access a class variable
3. y is an object property that access a instance variable
4. the value of x property is shared between objects (or instances)
5. the value of y property is not shared between objects (or instances)
6. the value of x changed by instance variable a was reflected in variable b
7. as A.__x is private, to get its value, we created a static method A.x_()
 """
