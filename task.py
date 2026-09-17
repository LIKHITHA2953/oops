
def task_logger(func):
    def wrapper(self, task_name):
        print("Task execution started")
        func(self, task_name)
        print("Task execution completed")
    return wrapper


class Employee:

  
    company_name = "TechSolutions"

    def __init__(self, name, employee_id, salary):
      
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("Company:", self.company_name)
        print("Employee:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print()

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    
    @staticmethod
    def validate_salary(salary):
        if salary > 0:
            return True
        return False


class Developer(Employee):

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(self.name, "is writing code using", self.programming_language)
        print()


class ProjectManager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    @task_logger
    def assign_task(self, task_name):
        if task_name == "":
            print("Invalid input: Task name cannot be empty.")
        else:
            print("Task assigned:", task_name)




developer1 = Developer(
    "Ravi",
    "E101",
    40000,
    "Python"
)

developer2 = Developer(
    "Priya",
    "E102",
    45000,
    "Java"
)

manager = ProjectManager(
    "Arjun",
    "E103",
    60000,
    5
)


print("EMPLOYEE DETAILS")
print("----------------")

developer1.display_details()
developer2.display_details()
manager.display_details()


print("DEVELOPER ACTIVITIES")
print("--------------------")

developer1.write_code()
developer2.write_code()



print("PROJECT MANAGER ACTIVITY")
print("------------------------")

manager.assign_task("Develop login page")
print()


Employee.change_company_name("CodeCraft Solutions")

print("Company name updated to", Employee.company_name)
print()


print("UPDATED COMPANY NAME")
print("--------------------")

print(developer1.name, ":", developer1.company_name)
print(developer2.name, ":", developer2.company_name)
print(manager.name, ":", manager.company_name)
print()


print("SALARY VALIDATION")
print("-----------------")

negative_salary = -5000

if Employee.validate_salary(negative_salary):
    print("Valid salary")
else:
    print("Invalid salary: Salary must be greater than zero.")


valid_salary = 50000

if Employee.validate_salary(valid_salary):
    print("Valid salary:", valid_salary)
else:
    print("Invalid salary.")
print()


print("EMPTY TASK VALIDATION")
print("---------------------")

manager.assign_task("")
print()


print("INDEPENDENT EMPLOYEE DATA")
print("-------------------------")

employee1 = Employee("Suresh", "E104", 30000)
employee2 = Employee("Anita", "E105", 50000)

employee1.salary = 35000

print("Employee 1:", employee1.name, employee1.salary)
print("Employee 2:", employee2.name, employee2.salary)