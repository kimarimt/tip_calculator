def main():
    print('Welcome to the tip calculator!')
    bill = float(input('What was the total bill? $'))
    tip = float(input('How much tip would you like to give (10, 12, or 15)? ')) / 100
    people = int(input('How many people to split the bill? '))
    total = (bill * tip) + bill
    pay_per_person = total / people
    print(f'Each person should pay: ${pay_per_person:.2f}')


if __name__ == '__main__':
    main()
