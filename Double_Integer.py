def convert(number):
    number1 = str(number).split('.')

    number1[1] = '0.' + number1[1]
    
    number1[0] = int(number1[0])
    number1[1] = float(number1[1])
    
    if number1[1] >= 0.5:
        number1[0] += 1
        return number1[0]
    return number1[0]

number = float(input('Enter a number: '))
print(f'{number} ---> {convert(number)}')