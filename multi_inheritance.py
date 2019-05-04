class A:
    def f1(self):
        print("Executing A.f1()")
    def f2(self):
        print("Executing A.f2()")

class B:
    def f1(self):
        print("Executing B.f1()")
    def f3(self):
        print("Executing B.f3()")

class C(A, B):
    def f2(self):
        print("Executing C.f2()")

class D(B, A):
    def f2(self):
        print("Executing D.f2()")

c = C()
c.f1()
c.f2()
c.f3()

print('')

d = D()
d.f1()
d.f2()
d.f3()

# [Running] python -u "d:\dev\test\python\multi_inheritance.py"
# Executing A.f1()
# Executing C.f2()
# Executing B.f3()
#
# Executing B.f1()
# Executing D.f2()
# Executing B.f3()
# [Done] exited with code=0 in 0.128 seconds

""" Shows:
1. how multi inheritance works
2. that only methods not present at class itself are imported from its base class
3. that the order in the imported list affect the result of which methods are imported

Observe that in C:
1. B.f1() was not imported because A.f1() was (A come before B at class definition)
2. A.f2() was not imported because C.f2() was present

Observe that in D:
1. A.f1() was not imported because B.f1() was (B come before A at class definition)
2. there is no A methods present at D
 """
