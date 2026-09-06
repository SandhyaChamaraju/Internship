class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        total = 0

        print("Product\tPrice\tQuantity\tTotal")
        print("----------------------------------------")

        for p in self.products:
            amount = p.price * p.quantity
            total += amount
            print(p.name, "\t", p.price, "\t", p.quantity, "\t\t", amount)

        tax = total * 0.18
        final_total = total + tax

        print("----------------------------------------")
        print("Total:", total)
        print("Tax:", tax)
        print("Final Bill:", final_total)


# Create products
p1 = Product("Pen", 10, 2)
p2 = Product("Book", 50, 3)

# Create bill
bill = Bill()
bill.add_product(p1)
bill.add_product(p2)

# Display bill
bill.display_bill()
