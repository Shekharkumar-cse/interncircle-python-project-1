"""Interactive Calculator and Unit Converter - InternCircle Project 01.

Run with: python main.py
Currency rates below are examples for practice, not live exchange rates.
"""


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Please enter a valid number.')


def read_choice(prompt, allowed):
    while True:
        choice = input(prompt).strip()
        if choice in allowed:
            return choice
        print('Invalid choice. Try again.')


def calculator():
    print('\nArithmetic: +, -, *, /')
    operator = read_choice('Choose operation: ', {'+', '-', '*', '/'})
    first = read_number('First number: ')
    second = read_number('Second number: ')
    if operator == '+':
        result = first + second
    elif operator == '-':
        result = first - second
    elif operator == '*':
        result = first * second
    else:
        while second == 0:
            print('Cannot divide by zero.')
            second = read_number('Enter a non-zero second number: ')
        result = first / second
    print(f'Result: {result:.4f}')


def convert_units():
    print('\n1. Kilometers to miles')
    print('2. Miles to kilometers')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    option = read_choice('Choose conversion: ', {'1', '2', '3', '4'})
    amount = read_number('Enter value: ')
    if option == '1':
        print(f'{amount:g} km = {amount * 0.621371:.4f} miles')
    elif option == '2':
        print(f'{amount:g} miles = {amount / 0.621371:.4f} km')
    elif option == '3':
        print(f'{amount:g} °C = {amount * 9 / 5 + 32:.2f} °F')
    else:
        print(f'{amount:g} °F = {(amount - 32) * 5 / 9:.2f} °C')


def convert_currency():
    # Fixed sample rates for a beginner project. Not suitable for financial use.
    sample_inr_per_usd = 85.0
    print('\nCurrency conversion (DEMO RATE: 1 USD = 85 INR)')
    print('1. USD to INR')
    print('2. INR to USD')
    option = read_choice('Choose conversion: ', {'1', '2'})
    amount = read_number('Enter amount: ')
    while amount < 0:
        print('Currency amount cannot be negative.')
        amount = read_number('Enter a non-negative amount: ')
    if option == '1':
        print(f'${amount:.2f} = ₹{amount * sample_inr_per_usd:.2f} (demo only)')
    else:
        print(f'₹{amount:.2f} = ${amount / sample_inr_per_usd:.2f} (demo only)')


def main():
    print('=== Interactive Calculator & Unit Converter ===')
    while True:
        print('\n1. Calculator')
        print('2. Unit converter')
        print('3. Currency converter (demo rates)')
        print('4. Exit')
        option = read_choice('Select 1-4: ', {'1', '2', '3', '4'})
        if option == '1':
            calculator()
        elif option == '2':
            convert_units()
        elif option == '3':
            convert_currency()
        else:
            print('Thanks for using the program!')
            break


if __name__ == '__main__':
    main()
