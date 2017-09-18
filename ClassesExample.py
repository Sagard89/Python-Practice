class Bank:
    name = ""
    address = ""
    branchCount = 0
    def __init__(self,*args):
        self.name = args[0]
        self.address = args[1]
        self.branchCount = args[2]

    def __enter__(self):
        print("Super class enter")

    def __exit__(self):
        print("Super class exit")
        
    def show(self):
        print("Bank Name: ", self.name)
        print("Bank Address: ", self.address)
        print("Number of branches: ", self.branchCount)

class Branch(Bank):
    employesCount = 0
    managerName = ""
    branchAddress = ""
    def __init__(self,*args):
        super().__init__(args[0],args[1],args[2])
        self.employesCount = args[3]
        self.managerName = args[4]
        self.branchAddress = args[5]
        
    def __enter__(self):
        print("Child class enter")

    def __exit__(self):
        print("Child class exit")
    
    def show(self):
        super().show()
        print("Manager Name: ", self.managerName)
        print("Branch Address: ", self.branchAddress)
        print("Number of employees: ", self.employesCount)
    
    
branch1 = Branch("SBI", "Mumbai", 123, 123243, "ABC", "Uttam Nagar")
branch1.show()
print("********************************************************")
branch2 = Branch("PNB", "Hyderabad", 154, 343121, "def", "Vikas Puri")
branch2.show()
#print(branch.__dict__)
