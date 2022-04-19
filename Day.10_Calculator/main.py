#Calculator
from replit import clear
from art import logo

print(logo)
randomvariablename = False

def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}
def value():
  operation = operations[operation_key]
  return operation(n1,n2)
n1="temp"
def calculator(randomvariablename,n1):
  if randomvariablename == True:
    n1 = n1
  else:
    n1 = float(input("What's the first number?: "))
  print("""

+
-
*
/
          
""")
  operation_key = input("Pick an operation: ")
  n2 = float(input("What's the next number?: "))
  def value():
    operation = operations[operation_key]
    return operation(n1,n2)

  print(f"{n1} {operation_key} {n2} = {value()}")
  repeat = input(f"Type 'y' to continue calculating with {value()}, or 'n' to start a new calculation: ")
  if repeat == "y":
    randomvariablename = True
    n1=value()
    clear()
    print(logo)
    calculator(randomvariablename,n1)
  else:
    clear()
    randomvariablename = False
    print(logo)
    calculator(randomvariablename,n1)

calculator(randomvariablename, n1)