# Simple CLI Calculator 🔢💻

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

print("📌 Welcome to CLI Calculator 🔢💻")
print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculation
if choice == '1':
    print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"✅ Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"✅ Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("❌ Invalid choice! Please select 1-4.")
