
# function exception_handling module packages

def safe_divide(a, b):
    """Divides two numbers and handles division by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage
# if __name__ == "__main__":
#     print(safe_divide(10, 2))  # Output: 5.0
#     print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.

#     # Example of printing characters safely
#     n = 5
#     for j in range(n):
#         print('*', end=' ')
#     print()


#WAP to calc sum of any number
def add(*args):
    return sum(args)


# print(add(1, 2, 3, 4, 5))  # Output: 6

#  Mysum.py

# WAF to print greeting msg for a dinner party.

def greet(*names):
    for name in names:
        print(f"Welcome Mr./Mrs.{name} \n You are invited to a dinner party tonight.")
        print("#" * 50)


# greet("John", "Alice", "Bob")


#Exception

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")
