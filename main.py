print('Welcome to the calculator app.')

isContinuing = True
is_starting = True

def calculate(num1, num2, operation):
  """Takes two numbers and an operation and returns the result of the calculation of the two numbers with the specific operation given"""
  if(operation == '+'):
    return num1 + num2
  elif(operation == '-'):
    return num1 - num2
  elif(operation == '*'):
    return num1 * num2
  elif(operation == '/'):
    return num1 / num2

while(is_starting == True):
  first_num = float(input("What's the first number?:\n"))
  operation = input("Choose an operation: '+', '-', '*', '/'\n")
  second_num = float(input("What's the next number?\n"))

  result = calculate(first_num, second_num, operation)
  print(f"{first_num} {operation} {second_num} = {result}")
  keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")

  while(isContinuing == True):
    if(keep_going == 'y'):
      next_operation = input("Choose an operation: '+', '-', '*', '/'\n")
      next_num = float(input("What's the next number?\n"))
      
      result = calculate(result, next_num, next_operation)
      print(f"{result} {next_operation} {next_num} = {result}")
      keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")
    else:
      isContinuing = False
