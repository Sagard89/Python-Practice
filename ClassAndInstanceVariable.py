class TestClass:
    #Class variable -> name
    name = "Sagar"

    def __init__(this,name):
        # Instance variable -> name
        this.name = name

    def showName(this):
        print(this.name)


def main():
    obj = TestClass("Ashu")
    obj1 = TestClass("Nag")
    print(TestClass.showName)
    print(obj.showName)
    obj.showName()
    TestClass.showName(TestClass)
    
    #print(TestClass.name)
    #obj.showName()

    #print(TestClass.name)
    #obj1.showName()

main()
