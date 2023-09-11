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


# Q2.

class Restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_table=[]
        self.customer_orders={}

    
    def add_item_to_menu(self,item, price):
        self.menu_items[item]= price

    def book_tables(self,table_num):
        self.book_table.append(table_num)
    def customer_order(self,table_num, order):
        order_details={'tble_num': table_num,'order':order}
        self.customer_orders.append(order_details)

    def print_menu(self):
        for item, price in self.menu_items.items():
            print(item,price)

    def print_table_reservatio(self):
         for table in self.book_table:
             print(table)
    def print_customer_orders(self):
        for order in self.customer_orders:
            print(order['table_num'], order['order'])

# Q>3.
class BankAccount:
    def __init__(self,account_number,balance, date_of_opening,customer_name):
        self.account=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name

    def deposit(self, amount):
        self.balance=self.balance +amount

    def withdraw(self,w_amount):
        self.balance=self.balance-w_amount

    def check_balance(self):
        print(self.balance)
        
        

    

