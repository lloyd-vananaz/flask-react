should_repeat = 'y'

while should_repeat == 'y':
    try:
        age = int(input('Age: '))
        print(age)
    except ValueError as error:
        print(f'Please enter a number. {error}')
    else:
        print('Thank you!')
    finally:
        should_repeat = input('Again (y/n)? ')