import os

# --- Basic Math Functions ---
# Separated for better structure and testing
def add_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def mult_nums(a, b):
    return a * b

def div_nums(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def clear_console():
    # Works for both Windows (cls) and Mac/Linux (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def main_app():
    print("=== MY COMMAND LINE CALCULATOR ===")
    print("Instructions: Enter numbers and choose an operator.")
    print("Type 'clear' to reset or 'exit' to close.")

    while True:
        try:
            # Taking first input
            user_input = input("\nEnter 1st number (or exit/clear): ").lower().strip()
            
            if user_input == 'exit':
                print("Closing the application...")
                break
            if user_input == 'clear':
                clear_console()
                continue
            
            val1 = float(user_input)
            
            # Choosing operator
            op = input("Select operator (+, -, *, /): ").strip()
            
            # Taking second number
            val2 = float(input("Enter 2nd number: "))

            # Calculating based on operator
            if op == '+':
                output = add_nums(val1, val2)
            elif op == '-':
                output = sub_nums(val1, val2)
            elif op == '*':
                output = mult_nums(val1, val2)
            elif op == '/':
                output = div_nums(val1, val2)
            else:
                print("Invalid operator! Please try again.")
                continue

            print(f"Result: {output}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main_app()