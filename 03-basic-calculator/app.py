def add(a, b):
  answer = a + b
  print(f'{a} + {b} = {answer}')

def substract(a, b):
  answer = a - b
  print(f'{a} + {b} = {answer}')

def multiply(a, b):
  answer = a * b
  print(f'{a} x {b} = {answer}')

def divide(a, b):
  if b == 0:
    print('Infinite')
  answer = a / b
  print(f'{a} / {b} = {answer}')

while True:
  print('a - add')
  print('b - substract')
  print('c - multiply')
  print('d - divide')

  choice = input('Input your choice')

  if choice == 'a' or choice == 'A':
    print('add')
    a = int(input('first number'))
    b = int(input('second number'))
    add(a, b)
  elif choice == 'b' or choice == 'B':
    print('substract')
    a = int(input('first number'))
    b = int(input('second number'))
    substract(a, b)
  elif choice == 'c' or choice == 'C':
    print('multiply')
    a = int(input('first number'))
    b = int(input('second number'))
    multiply(a, b)
  elif choice == 'd' or choice == 'D':
    print('divide')
    a = int(input('first number'))
    b = int(input('second number'))
    divide(a, b)
  else:
    print('exit')
    quit()