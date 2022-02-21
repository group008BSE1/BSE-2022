list_of_numbers = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
        list_of_numbers.append(num)

    except:
        print('Invalid input')

#printing the list
print(f'The list: {list_of_numbers}')

# getting minimun
for number in list_of_numbers:
    if number < list_of_numbers[0]:
        list_of_numbers[0] = number
print(f'Minimum number: {list_of_numbers[0]}')

# getting maximun
for number in list_of_numbers:
    if number > list_of_numbers[0]:
        list_of_numbers[0] = number
print(f'Maximum number: {list_of_numbers[0]}')
