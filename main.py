print('Welcome to the calculator app.')

is_continuing = True
is_starting = True

def add(n1, n2):
  """Takes two numbers and returns the sum of the two numbers"""
  return n1 + n2

def subtract(n1, n2):
  """Takes two numbers and returns the difference of the two numbers"""
  return n1 - n2

def multiply(n1, n2):
  """Takes two numbers and returns the product of the two numbers"""
  return n1 * n2

def divide(n1, n2):
  """Takes two numbers and returns the quotient of the two numbers"""
  return n1 / n2

function_dictionary = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply

}

def calculate(num1, num2, operation):
  """Takes two numbers and an operation and returns the result of the calculation of the two numbers with the specific operation given"""
  if(operation == '+'):
    function = function_dictionary["+"]
    return function(num1, num2)
  elif(operation == '-'):
    function = function_dictionary["-"]
    return function(num1, num2)
  elif(operation == '*'):
    function = function_dictionary["*"]
    return function(num1, num2)
  elif(operation == '/'):
    function = function_dictionary["/"]
    return function(num1, num2)
  
def printSymbols():
  options_str = ''
  for symbol in function_dictionary:
    options_str += f"'{symbol}' "
  return input(f"Choose an operation: {options_str}\n")



while(is_starting == True):
  first_num = float(input("What's the first number?:\n"))
  operation = printSymbols()
  second_num = float(input("What's the next number?\n"))

  result = calculate(first_num, second_num, operation)
  print(f"{first_num} {operation} {second_num} = {result}")
  keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")

  while(is_continuing == True):
    if(keep_going == 'y'):
      next_operation = printSymbols()
      next_num = float(input("What's the next number?\n"))
      
      result = calculate(result, next_num, next_operation)
      print(f"{result} {next_operation} {next_num} = {result}")
      keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")
    else:
      is_continuing = False
