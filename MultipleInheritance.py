class Base1(object):
    def __init__(self,nm):
        self.name1 = "Peter"
        print("Passed to Base1")
        super(Base1, self).__init__(nm)
  
    def showName1(self):
        print(self.name1)
 
  
class Base2(object):
    def __init__(self,nm):
        self.name2 = "John"
        print("Passed to Base2")
        super(Base2, self).__init__(nm)
  
    def showName2(self):
        print(self.name2)
 
 
class Child(Base2, Base1):
    def __init__(self):
        self.name3 = "Sagar"
        print("Created Child")
        super(Child, self).__init__(self.name3)
          
    def showName3(self):
        print(self.name3)
 
 
obj = Child()
print(Child.__mro__)
obj.showName1()
obj.showName2()
obj.showName3()
