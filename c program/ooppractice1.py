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

        
        

