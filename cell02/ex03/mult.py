first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
result = first_number * second_number
print(f"{first_number} x {second_number} = {result}")
if result > 0:
    print("The result is positive.")
if result < 0:
    print("The result is negative.")
if result == 0:
    print("The result is positive and negative.")