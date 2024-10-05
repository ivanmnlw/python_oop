class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
    
    def calculate_tax(self, tax_rate):
        self.tax_rate = tax_rate
        return self.total_amount * tax_rate
    
    def display_order(self):
        print("Detail Pesanan ->")
        print(f"Order Id: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Amount: {self.total_amount}")

class OrderProcessor:
    def __init__(self):
        self.order_list = []
    
    def add_order(self, order):
        self.order_list.append(order)
    
    def calculate_total_revenue(self):
        total = 0
        for i in range(len(self.order_list)):
            total += self.order_list[i].total_amount
        return total
    
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for order in self.order_list:
            total_tax += order.calculate_tax(tax_rate)
        return total_tax
    
    def display_orders(self):
        for order in self.order_list:
            order.display_order()
            print("------")
        
order1 = Order("1", "Andi", "12 Januari 2024", 100000)
order2 = Order("2", "Bejo", "10 Februari 2024", 150000)
order3 = Order("3", "Pandu", "22 Januari 2024", 200000)

od_p = OrderProcessor()
od_p.add_order(order1)
od_p.add_order(order2)
od_p.add_order(order3)

od_p.display_orders()
total_revenue = od_p.calculate_total_revenue()
total_tax = od_p.calculate_total_tax(0.3)
print(f"Total Revenue: {total_revenue}")
print(f"Total Tax: {total_tax}")
