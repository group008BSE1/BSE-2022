def display_stock():
    print('Stock contains:')
    print(f'{nickels} nickels')
    print(f'{dimes} dimes')
    print(f'{quarters} quarters')
    print(f'{ones} ones')
    print(f'{fives} fives')


def calculate_num_of_dollars_and_cents(total_amount):
    '''
        This function converts a provides amount into dollars and cents
        and prints the result
    '''
    dollars = int(total_amount // 1)
    cents = int(round(total_amount * 100) % 100)
    if dollars <= 0:
        print(f'Total :{int(cents)} cents ')
    else:
        print(f'Total : {int(dollars)} dollars and {int(cents)} cents ')


def display_menu():
    '''
        Prints the menu
    '''
    print('Menu for details: ')
    print("  'n' - deposit a nickel")
    print("  'd' - deposit a dime")
    print("  'q' - deposit a quarter")
    print("  'o' - deposit a one dollar")
    print("  'f' - deposit a five dollar")
    print("  'c' - cancel the purchase")


def change():
    '''
        This calculates change to give to the customer
    '''
    print("Please take the change below.")
    if num_of_quarters != 0:
        print(f'   {int(num_of_quarters)} Quarters')
    if num_of_dimes != 0:
        print(f'   {int(num_of_dimes)} dimes')
    if num_of_nickels != 0:
        print(f'   {int(num_of_nickels)} nickels')


def entered_paymentf():
    if entered_payment == 'n':
        return 0.05

    elif entered_payment == 'd':
        return 0.1

    elif entered_payment == 'q':
        return 0.25

    elif entered_payment == 'o':
        return 1

    elif entered_payment == 'f':
        return 5

    elif entered_payment == 'c':
        return 'c'
    else:
        passed_thru_try = True
        print(f'Illegal selection: {entered_payment}')


def num_of_quartersf(total_amount):
    return int(total_amount * 100 // 25)


def num_of_dimesf(total_amount):
    amount_left_after_quarters = total_amount - (num_of_quarters * 0.25)
    return int((amount_left_after_quarters * 100) // 10)


def num_of_nickelsf(total_amount):
    amount_left_after_dimes = (total_amount - (num_of_quarters * 0.25)) - (num_of_dimes * 0.1)
    return int((amount_left_after_dimes * 100) // 5)


def ismultipleof5(number):
    if (float(number) * 100) % 5 == 0:
        return True
    else:
        return False


def isnonnegative(number):
    if (float(price) / 100) >= 0:
        return True
    else:
        return False


def change_to_take():
    print("Please take the change below.")
    if num_of_quarters != 0:
        print(f'   {int(num_of_quarters)} Quarters')
    if num_of_dimes != 0:
        print(f'   {int(num_of_dimes)} dimes')
    if num_of_nickels != 0:
        print(f'   {int(num_of_nickels)} nickels')


def extranickels_to_num_of_dollars_and_cents(total_amount):
    '''
        This function converts a provides amount into dollars and cents
        and prints the result
    '''
    total_amount = (total_amount * 5) / 100
    dollars = int(total_amount // 1)
    cents = int(round(total_amount * 100) % 100)
    if dollars <= 0:
        print(f'Amount due is :{int(cents)} cents ')
    else:
        print(f'Amount due is: {int(dollars)} dollars and {int(cents)} cents ')


# intializing break statements
not_passed_thru_except = True
not_quit = True

# intializing sum
sum_of_price = 0
balance = 0

# intializing stock coins
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

# Program starts here
print('Welcome to the vending machine payment maker program\npayment maker initialized.')
while not_quit:
    # Print the stock at the beginning
    if not_passed_thru_except:
        display_stock()

    # Prompt user to enter price
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    # intializing count for display of deposit menu
    count_for_deposit_menu = 0
    if price == 'q' or price == 'Q':
        calculate_num_of_dollars_and_cents(sum_of_price)

        not_quit = False
    else:
        try:
            if ismultipleof5(price) and isnonnegative(price):
                price = float(price)
                not_passed_thru_except = True
            else:
                print('Illegal price: Must be a non-negative multiple of 5 cents.')
                not_passed_thru_except = False
        except ValueError:
            print('Invalid input!')
            not_passed_thru_except = False

        # Getting payment for the price
        payment = 0
        not_yet_quit = True
        while not_yet_quit and not_passed_thru_except:
            count_for_deposit_menu += 1
            if count_for_deposit_menu < 2:
                display_menu()
                calculate_num_of_dollars_and_cents(float(price))

            entered_payment = input('Indicate your deposit: ')

            passed_thru_try = False
            try:
                # Allow input of 'n', 'd', 'q', 'o' and 'f' and increment accordingly
                if entered_payment == 'n':
                    nickels = nickels + 1
                elif entered_payment == 'd':
                    dimes = dimes + 1
                elif entered_payment == 'q':
                    quarters = quarters + 1
                elif entered_payment == 'o':
                    ones = ones + 1
                elif entered_payment == 'f':
                    fives = fives + 1
                elif entered_payment == 'c':
                    pass
                else:
                    passed_thru_try = True

                entered_payment = entered_paymentf()

                # Calculating payment due
                if (not passed_thru_try):
                    if entered_payment != 'c':
                        payment = payment + float(entered_payment)
                        paymentDue = price - payment
                    if paymentDue > 0 and entered_payment != 'c':
                        calculate_num_of_dollars_and_cents(paymentDue)
                    elif paymentDue == 0 and entered_payment != 'c':
                        sum_of_price = sum_of_price + price
                        print('Please take the change below')
                        print('  No change due')
                        break
                    else:
                        # Calculating change in terms of dimes and nickels
                        paymentDue = abs(paymentDue)
                        if entered_payment == 'c':
                            paymentDue = payment
                        # Quarters
                        num_of_quarters = num_of_quartersf(paymentDue)
                        if num_of_quarters > quarters:
                            num_of_quarters = quarters
                        # Dimes
                        num_of_dimes = num_of_dimesf(paymentDue)
                        if num_of_dimes > dimes:
                            num_of_dimes = dimes
                        # Nickels
                        num_of_nickels = num_of_nickelsf(paymentDue)
                        if num_of_nickels > nickels:
                            extra_nickels = num_of_nickels - nickels
                            num_of_nickels = nickels
                            if extra_nickels > 0:
                                print('Machine is out of change.')
                                print('See store manager for remaining refund.')
                                extranickels_to_num_of_dollars_and_cents(extra_nickels)

                        # subtracting change from the stock in form of coins awarded to buyer

                        # Quarters
                        quarters = quarters - num_of_quarters

                        # Dimes
                        dimes = dimes - num_of_dimes

                        # Nickels
                        nickels = nickels - num_of_nickels

                        # updating total of purchase prices
                        sum_of_price = sum_of_price + price

                        # giving change
                        change_to_take()

                        break
            except ValueError:
                print(f'Illegal selection: {entered_payment}')

#      GROUP 8 MEMBERS
# Kisakye Joshua 2021/BSE/062/PS
# Kibalama James 2021/BSE/058/PS
# Abaho Davis 2021/BSE/001/PS
# Amos Merber 2021/BSE/018/PS
# Ntwari Reagan 2021/BSE/134/PS

# DATE: 21/02/2022





