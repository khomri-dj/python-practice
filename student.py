class student:
    def __init__(self,name,):
        self.name=name
        self.grades=[]
    def addgrades(self,grade):
        if 0<= grade <=20:
            self.grades.append(grade)
        else:
            print("try again")    
    def average(self):
        return sum(self.grades)/len(self.grades)
    def result(self):
        avg=self.average()
        if avg >=10:
            return "passed"
        else:
            return "failed"
r1=student("ahmed")
r1.addgrades(5)
r1.addgrades(7)
r1.addgrades(23)
print(r1.average())
print(r1.result())