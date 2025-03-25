# addition.py
print("Enter two numbers to add them together.")

# Prompt for two numbers
try:
    num1 = input("First number: ")
    num2 = input("Second number: ")
    result = int(num1) + int(num2)
    print(f"The sum of {num1} and {num2} is {result}.")
except ValueError:
    print("Sorry, please enter numbers only (e.g., '5' or '12').")