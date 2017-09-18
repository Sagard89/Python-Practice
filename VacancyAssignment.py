import uuid
class WeeksAvailable(object):
    def __init__(self,number):
        self.weekNumber = number
        self.assignedTo = []

    def assignToUser(self,userid):
        if (self.assignedTo.count(userid) == 0):
            if ()
            self.assignedTo.append(userid)
            return True
        else:
            return False

class User(object):
    def __init__(self,name):
        self.userid = uuid.uuid4().hex
        self.name = name
        self.maxVacancy = 3
        
    def getUserId(self):
        return self.userid

class VacancyAssignment(object):
    def __init__(self,nameList):
        self.weeksList = [WeeksAvailable(i) for i in range(52)]
        self.usersList = [User(n) for n in nameList]

    def showWeeks(self):
        for w in self.weeksList:
            print(w.weekNumber)
        for u in self.usersList:
            print(u.name)

def main():
    nameList = ["John","Adam","Sandra","Stephen","Peter","Dynamo"]
    v = VacancyAssignment(nameList)
    v.showWeeks()

main()
