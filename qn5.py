class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary

    @classmethod
    def getObjFromString(cls,inp):
        name,salary= inp.split("-")
        return cls(name,salary)

    def getname(self):
        return self.name
    def getSalary(self):
        return self.salary

emp= Employee.getObjFromString("rishitosh-5000")
print(emp.getname())
print(emp.getSalary())