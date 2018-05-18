def add(num1, num2):
    return int(num1) + int(num2)

while True:
    number1 = input('What is your first number? ')
    number2 = input('What is your second number? ')
    try:
        print(add(number1, number2))
    except ValueError:
        print('Could not add "{}" and "{}". Please use numbers for both values.'.format(number1, number2))
