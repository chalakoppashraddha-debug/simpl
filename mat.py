# math.py
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"maltiplication: {a * b}")
    if b!=0:
      print(f"division: {a / b}")
    else:
      print("zero is not alowed")
    
    
except ValueError:
    print("Please enter valid numbers.")
