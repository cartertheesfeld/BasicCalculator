class Calculator:
    def __init__(self, initial_total):
        self.total = initial_total

    def add(self, num):
        self.total += num
        return self.total

    def subtract(self, num):
        self.total -= num
        return self.total

    def multiply(self, num):
        self.total *= num
        return self.total

    def divide(self, num):
        if num == 0:
            print("Cannot divide by zero.")
        else:
            self.total /= num
        return self.total

    def reset(self):
        self.total = 0
        return "Total has been reset to 0"


# Get the starting number from the user
initial_number = float(input("Enter the starting number: "))
my_calculator = Calculator(initial_number)

while True:
    # Display options to the user
    print("\nOptions:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset")
    print("6. Exit")

    # Get user choice
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Add
        num_to_add = float(input("Enter the number to add: "))
        result = my_calculator.add(num_to_add)
        print("Total after addition:", result)
    elif choice == "2":
        # Subtract
        num_to_subtract = float(input("Enter the number to subtract: "))
        result = my_calculator.subtract(num_to_subtract)
        print("Total after subtraction:", result)
    elif choice == "3":
        # Multiply
        num_to_multiply = float(input("Enter the number to multiply: "))
        result = my_calculator.multiply(num_to_multiply)
        print("Total after multiplication:", result)
    elif choice == "4":
        # Divide
        num_to_divide = float(input("Enter the number to divide by: "))
        result = my_calculator.divide(num_to_divide)
        if result is not None:
            print("Total after division:", result)
    elif choice == "5":
        # Reset
        reset_message = my_calculator.reset()
        print(reset_message)
    elif choice == "6":
        # Exit the program
        print("Exiting the calculator program. Final total:", my_calculator.total)
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")