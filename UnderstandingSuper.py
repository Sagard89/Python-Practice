class A(object):
    def foo(self):
        print('A')

class Foreign(object):
    def foo(self):
        print('Foreign')
        super().foo()

class B(Foreign):
    def foo(self):
        print('B')
        super().foo()
 
class C(A):
    def foo(self):
        print('C')
        super().foo()
 
class D(B,C):
    def foo(self):
        print('D')
        super().foo()
 
d = D()
d.foo()
#print(D.__mro__)
