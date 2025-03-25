# addition_calculator.py
print("Enter two numbers to add them together (or 'q' to quit).")

while True:
    # Prompt for two numbers
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    # Try to add them
    try:
        result = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Sorry, please enter numbers only (e.g., '5' or '12').")