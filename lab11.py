#Q:1
import math

class Shape():
    def __init__(self, sides):
        self.sides = sides

    
    def ComputeArea(self):
        pass

class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def ComputeArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2  
        area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
        return area

class Circle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def ComputeArea(self):
        radius = self.sides[0]
        area = math.pi * radius ** 2
        return area

triangle_sides = [3, 4, 5]
circle_radius = 2

triangle = Triangle(triangle_sides)
triangle_area = triangle.ComputeArea()
print("Triangle area:", triangle_area)

circle = Circle([circle_radius])
circle_area = circle.ComputeArea()
print("Circle area:", circle_area)

print("-----------------------------------------------")

#Q:2
class Employee:
    def __init__(self, EmpName, EmpID, Salary):
        self.EmpName = EmpName
        self.EmpID = EmpID
        self.Salary = Salary

    def SalaryStatus(self):
        return "Salary: $" + str(self.Salary)


class BuildingManager(Employee):
    def __init__(self, EmpName, EmpID):
        super().__init__(EmpName, EmpID, 10000)


class ProcurementManager(Employee):
    def __init__(self, EmpName, EmpID):
        super().__init__(EmpName, EmpID, 12000)


class LogisticsManager(Employee):
    def __init__(self, EmpName, EmpID):
        super().__init__(EmpName, EmpID, 15000)


def main():
    employees = [
        BuildingManager("Omer", 1),
        ProcurementManager("Talha", 2),
        LogisticsManager("Shahzaib", 3)
    ]

    for employee in employees:
        print("Employee Name:", employee.EmpName)
        print("Employee ID:", employee.EmpID)
        print(employee.SalaryStatus())
        print()

main()

