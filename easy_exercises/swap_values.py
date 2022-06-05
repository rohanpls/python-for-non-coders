value1 = int(input('Enter Value 1: '))

value2 = int(input('Enter Value 2: '))
print(f'Current values:\n Value 1 = {value1}\n Value 2 = {value2}')
value1, value2 = value2, value1
print(f'Swapped values:\n Value 1 = {value1}\n Value 2 = {value2}')