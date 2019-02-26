# A simple calculator program taking inputs from the command lines.

func = input('Press 0 for +\nPress 1 for -\nPress 2 for *\nPress 3 for /\n>> ')
num1 = input('Please enter your first number\n>> ')
num2 = input('Please enter your second number\n>> ')

if func == '0':
    print('{} + {} = {}'.format(num1, num2, float(num1) + float(num2)))
elif func == '1':
    print('{} - {} = {}'.format(num1, num2, float(num1) - float(num2)))
elif func == '2':
    print('{} * {} = {}'.format(num1, num2, float(num1) * float(num2)))
elif func == '3':
    print('{} / {} = {}'.format(num1, num2, float(num1) / float(num2)))
else:
    print('Error. Please try again')
