def main():
    print('Welcome to the Tip Calculator')
    bill = float(input('What was the total bill? $'))
    tip = float(input('How much tip would you like to give (10, 12, or 15)? ')) 
    people = int(input('How many people to split the bill? '))
    tip_amount = bill * tip / 100
    pay_per_person = (bill + tip_amount) / people
    print(f'Each person should pay: ${pay_per_person:.2f}')


if __name__ == '__main__':
    main()
