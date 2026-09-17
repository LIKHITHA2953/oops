def task_logger(func):
    def wrapper(*args, **kwargs):
        print("Task execution started")
        func(*args, **kwargs)
        print("Task execution completed")
    return wrapper


class Employee:
    company_name = "TechSolutions"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("Company:", Employee.company_name)
        print("Employee:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print("Company name updated to", cls.company_name)

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


class ProjectManager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    @task_logger
    def assign_task(self, task_name):
        if task_name == "":
            print("Invalid task name")
        else:
            print("Task assigned:", task_name)


developer1 = Developer("Ravi", "E101", 40000, "Python")
developer2 = Developer("Sita", "E102", 45000, "Java")
manager = ProjectManager("Arjun", "E103", 60000, 8)

developer1.display_details()
print()

developer2.display_details()
print()

manager.display_details()
print()

developer1.write_code()
developer2.write_code()
print()

manager.assign_task("Develop login page")
print()

Employee.change_company_name("CodeCraft Solutions")
print()

print("Developer 1 Company:", developer1.company_name)
print("Developer 2 Company:", developer2.company_name)
print("Manager Company:", manager.company_name)

print("\n--- Input Validation ---")

if Employee.validate_salary(-5000):
    print("Valid salary")
else:
    print("Invalid salary: Salary must be greater than zero")

if Employee.validate_salary(50000):
    print("Valid salary:", 50000)
else:
    print("Invalid salary")

manager.assign_task("")

employee1 = Employee("Kiran", "E104", 30000)
employee2 = Employee("Priya", "E105", 50000)

print("\nEmployee 1:")
employee1.display_details()

print("\nEmployee 2:")
employee2.display_details()