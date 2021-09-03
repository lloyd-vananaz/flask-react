should_repeat = 'y'

while should_repeat == 'y':
    try:
        age = int(input('Age: '))
        print(age)
    except ValueError as error: # Catches a specific ValueError
        print(f'Please enter a number. {error}')
    except: # Catches all errors
        print('Something else went wrong.')
    else: # Executes if no exceptions encountered
        print('Thank you!')
    finally: # Executes after all blocks
        should_repeat = input('Again (y/n)? ')