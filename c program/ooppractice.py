class Employee:
    def __init__(self,emp_name, emp_id, emp_salary, emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department

    def calc_emp_salary(self, salary, hours_worked):
        self.salary=salary
        overtime=0
        if hours_worked > 50:
            overtime = hours_worked - 50
            print(salary + (overtime * (salary / 50)))
        else:
            print(salary)
        
        
    def emp_assign_department(self,emp_department):
        self.emp_department=emp_department
        

    def employee_details(self):
        print(f"name = {self.emp_name}")
        print(f"id= {self.emp_name}")
        print(f"salary = {self.emp_salary}")
        print(f"department={self.emp_department}")