from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class Developer(Employee):
    def __init__(self, base_salary, project_count, project_bonus):
        self.base_salary = base_salary
        self.project_count = project_count
        self.project_bonus = project_bonus

    def calculate_salary(self):
        return self.base_salary + (self.project_count * self.project_bonus)

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

manager = Manager(base_salary=50000, bonus=10000)
developer = Developer(base_salary=40000, project_count=5, project_bonus=1000)
intern = Intern(stipend=15000)

print(f"Manager Salary: {manager.calculate_salary()}")
print(f"Developer Salary: {developer.calculate_salary()}")
print(f"Intern Salary: {intern.calculate_salary()}")

