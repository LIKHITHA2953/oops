# Employee Task Management System

# Task 3: Decorator
def task_logger(func):
    def wrapper(self, task_name):
        print("Task execution started")
        func(self, task_name)
        print("Task execution completed")
    return wrapper


# Task 1: Parent Class
class Employee:

    # Class Variable
    company_name = "TechSolutions"

    def __init__(self, name, employee_id, salary):
        # Instance Variables
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Instance Method
    def display_details(self):
        print("Company:", self.company_name)
        print("Employee:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print()

    # Class Method
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    # Static Method
    @staticmethod
    def validate_salary(salary):
        if salary > 0:
            return True
        return False


# Task 2: Developer Class
class Developer(Employee):

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(self.name, "is writing code using", self.programming_language)
        print()


# Task 2: Project Manager Class
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


# Task 4: Create Objects

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


# 1. Display all employee details
print("EMPLOYEE DETAILS")
print("----------------")

developer1.display_details()
developer2.display_details()
manager.display_details()


# 2. Both developers write code
print("DEVELOPER ACTIVITIES")
print("--------------------")

developer1.write_code()
developer2.write_code()


# 3. Project Manager assigns a task
print("PROJECT MANAGER ACTIVITY")
print("------------------------")

manager.assign_task("Develop login page")
print()


# 4. Change company name
Employee.change_company_name("CodeCraft Solutions")

print("Company name updated to", Employee.company_name)
print()


# 5. Display updated company name for all employees
print("UPDATED COMPANY NAME")
print("--------------------")

print(developer1.name, ":", developer1.company_name)
print(developer2.name, ":", developer2.company_name)
print(manager.name, ":", manager.company_name)
print()


# Task 5: Input Validation

# 1. Negative salary
print("SALARY VALIDATION")
print("-----------------")

negative_salary = -5000

if Employee.validate_salary(negative_salary):
    print("Valid salary")
else:
    print("Invalid salary: Salary must be greater than zero.")


# 2. Valid salary
valid_salary = 50000

if Employee.validate_salary(valid_salary):
    print("Valid salary:", valid_salary)
else:
    print("Invalid salary.")
print()


# 3. Empty task name
print("EMPTY TASK VALIDATION")
print("---------------------")

manager.assign_task("")
print()


# 4. Independent employee data
print("INDEPENDENT EMPLOYEE DATA")
print("-------------------------")

employee1 = Employee("Suresh", "E104", 30000)
employee2 = Employee("Anita", "E105", 50000)

employee1.salary = 35000

print("Employee 1:", employee1.name, employee1.salary)
print("Employee 2:", employee2.name, employee2.salary)