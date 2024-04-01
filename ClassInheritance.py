
# base class containing attributes of an employee
class Employee:
    name = ''
    email = ''
    password = ''

# child class inheriting from the Employee class
class PermanentEmployee(Employee):
    Salary = 0.00
    ProbationaryDate = ''
    RegularizationDate = ''

# child class inheriting from the Employee class
class ContractEmployee(Employee):
    HourlyPay = 0.00
    StartOfContractDate = ''
    EndOfContractDate = ''
    
    
    
