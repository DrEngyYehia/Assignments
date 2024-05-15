class Product:
    """Base class for products"""
    SUPERMARKET_NAME = "XYZ Supermarket"

    def _init_(self, product_id, name, price, manufacturer, weight, expiration_date, year):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def print_product_details(self):
        """Print product details"""
        print(f"Supermarket Name: {self.SUPERMARKET_NAME}")
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Weight: {self.weight}g")
        print(f"Expiration Date: {self.expiration_date}")
        print(f"Year: {self.year}")


class Healthy(Product):
    """Subclass for healthy products"""

    def _init_(self, product_id, name, price, manufacturer, weight, expiration_date, year):
        super()._init_(product_id, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = []

    def print_healthy_product_details(self):
        """Print healthy product details"""
        super().print_product_details()
        print(f"Calories: {self.calories} per gram")
        print(f"Components: {', '.join(self.components)}")

    def change_calories(self, new_calories):
        """Change calories"""
        self.calories = new_calories

    def compute_total_calories(self, weight_in_grams):
        """Compute total calories"""
        return self.calories * weight_in_grams


def main():
    while True:
        print(" XYZ Supermarket")
        print("1. Product Sub-system")
        print("2. Healthy Sub-system")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            product_subsystem()
        elif choice == "2":
            healthy_subsystem()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


def product_subsystem():
    while True:
        print("Product Sub-system")
        print("1. Add new Product")
        print("2. Display Product Details")
        print("3. Change/Edit product_ID")
        print("4. Exit the sub-system")
        print("5. Exit the Supermarket cashier system")
        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_product_details()
        elif choice == "3":
            change_product_id()
        elif choice == "4":
            break
        elif choice == "5":
            exit()
        else:
            print("Invalid option. Please try again.")


def healthy_subsystem():
    while True:
        print("Healthy Sub-system")
        print("1. Add new Healthy Product")
        print("2. Display Healthy Product Details")
        print("3. Change/Edit calories")
        print("4. Check calories and components of Healthy Product")
        print("5. Compute total calories of the Healthy Product")
        print("6. Exit the sub-system")
        print("7. Exit the Supermarket cashier system")
        choice = input("Choose an option: ")

        if choice == "1":
            add_healthy_product()
        elif choice == "2":
            display_healthy_product_details()
        elif choice == "3":
            change_calories()
        elif choice == "4":
            check_calories_and_components()
        elif choice == "5":
            compute_total_calories()
        elif choice == "6":
            break
        elif choice == "7":
            exit()
        else:
            print("Invalid option. Please try again.")


def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    manufacturer = input("Enter product manufacturer: ")
    weight = input("Enter product weight (grams): ")
    expiration_date = input("Enter product expiration date: ")
    year = input("Enter product year: ")
    print("Product added successfully!")

def display_product_details():
    product_id = input("Enter product ID: ")
    print("Product details:")
    print("Not implemented yet.")

def change_product_id():
    old_product_id = input("Enter old product ID: ")
    new_product_id = input("Enter new product ID: ")
    print("Product ID changed successfully!")

def add_healthy_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    manufacturer = input("Enter product manufacturer: ")
    weight = input("Enter product weight (grams): ")
    expiration_date = input("Enter product expiration date: ")
    year = input("Enter product year: ")
    calories = input("Enter product calories per gram: ")
    components = input("Enter product components (comma-separated): ").split(',')
    print("Healthy product added successfully!")

def display_healthy_product_details():
    product_id = input("Enter product ID: ")
    print("Healthy product details:")
    print("Not implemented yet.")

def change_calories():
    product_id = input("Enter product ID: ")
    new_calories = input("Enter new calories per gram: ")
    print("Calories changed successfully!")

def check_calories_and_components():
    product_id = input("Enter product ID: ")
    print("Calories and components:")
    print("Not implemented yet.")

def compute_total_calories():
    product_id = input("Enter product ID: ")
    weight_in_grams = float(input("Enter weight in grams: "))
    print("Total calories computed successfully!")


main()