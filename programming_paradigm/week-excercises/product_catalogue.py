class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")

def collect_product_data():
    products = []
    while True:
        name = input("Enter product name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        products.append(Product(name, price, quantity))
    return products

def display_all_products(products):
    for product in products:
        product.display_info()

# Collect and display product data
products = collect_product_data()
display_all_products(products)
