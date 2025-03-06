def main():
    print('Welcome to the Tip Calculator!')
    bill = int(input('What was the total bill?: $'))
    tip = int(input('How much tip would you like to give (10, 12, or 15)?: ')) / 100
    people = int(input('How many people to split the bill?: '))
    pay_per_person = ((bill * tip) + bill) / people
    print(f'Each person should pay: ${pay_per_person:.2f}')


if __name__ == '__main__':
    main()
