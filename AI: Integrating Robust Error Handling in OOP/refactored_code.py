import numbers

# 1. Define the custom exception class
class InvalidProductDataError(Exception):
    """Custom exception raised for errors in the input data for a Product."""
    pass

# 2. Refactor the Product class with validation
class Product:
    """Represents a product with a name, price, and quantity."""
    def __init__(self, name, price, quantity):
        self.name = name
        # 4. Use setters in __init__ to validate initial values
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """The price of the product."""
        return self.__price

    # 3. Implement the setter for price with validation
    @price.setter
    def price(self, value):
        """Sets the price, validating it's a non-negative number."""
        if not isinstance(value, numbers.Number) or value < 0:
            raise InvalidProductDataError(f"Invalid price: Price must be a non-negative number, but got {value}.")
        self.__price = value

    @property
    def quantity(self):
        """The quantity of the product."""
        return self.__quantity

    # 3. Implement the setter for quantity with validation
    @quantity.setter
    def quantity(self, value):
        """Sets the quantity, validating it's a non-negative integer."""
        if not isinstance(value, int) or value < 0:
            raise InvalidProductDataError(f"Invalid quantity: Quantity must be a non-negative integer, but got {value}.")
        self.__quantity = value


# 5. The InventoryManager class and its public interface remain unchanged
class InventoryManager:
    """Manages the collection of products and provides inventory operations."""
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product):
        """Adds a product object to the inventory list."""
        self.inventory.append(product)

    def update_quantity(self, name, new_quantity):
        """Updates the quantity of a product by name."""
        for product in self.inventory:
            if product.name == name:
                # This assignment now automatically triggers the validation in Product.quantity
                product.quantity = new_quantity
                break

    def calculate_total_value(self):
        """Calculates the total monetary value of all inventory."""
        total = 0
        for product in self.inventory:
            total += product.price * product.quantity
        return total

    def display_inventory(self):
        """Prints the current inventory list."""
        for product in self.inventory:
            print(f"{product.name} - ${product.price:.2f} x {product.quantity}")


# --- Demo Usage ---

# Original valid usage works as before
manager = InventoryManager()
manager.add_product(Product("Laptop", 1200.00, 5))
manager.add_product(Product("Mouse", 25.00, 20))
manager.update_quantity("Mouse", 18)

print("Current Inventory:")
manager.display_inventory()
print(f"\nTotal Inventory Value: ${manager.calculate_total_value():.2f}")

# Demo of the new validation and error handling
print("\n--- Demonstrating Validation ---")
try:
    # Attempting to create a product with an invalid price
    invalid_product = Product("Keyboard", -50.00, 10)
    manager.add_product(invalid_product)
except InvalidProductDataError as e:
    print(f"Error creating product: {e}")

try:
    # Attempting to update a product with an invalid quantity
    manager.update_quantity("Laptop", -3)
except InvalidProductDataError as e:
    print(f"Error updating quantity: {e}")

print("\nFinal Inventory (unchanged after errors):")
manager.display_inventory()
print("\n--- Testing Invalid Input ---")
try:
    manager.inventory[0].quantity = -5
except Exception as e:
    print(f"Test result: {e}")
