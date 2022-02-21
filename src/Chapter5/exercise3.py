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
        print('Stock contains:')
        print(f'{nickels} nickels')
        print(f'{dimes} dimes')
        print(f'{quarters} quarters')
        print(f'{ones} ones')
        print(f'{fives} fives')

    # Prompt user to enter price
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    # intializing count for display of deposit menu
    count_for_deposit_menu = 0
    if price == 'q' or price == 'Q':
        num_of_dollars = sum_of_price // 1
        num_of_cents = sum_of_price % 1 * 100
        if num_of_dollars <= 0:
            print(f'Total : int(num {int(num_of_cents)} cents ')
        else:
            print(f'Total : {int(num_of_dollars)} dollars and {int(num_of_cents)} cents ')
        not_quit = False
    else:
        try:
            if (float(price) * 100) % 5 == 0 and (float(price) / 100) >= 0:
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
                print('Menu for details: ')
                print("  'n' - deposit a nickel")
                print("  'd' - deposit a dime")
                print("  'q' - deposit a quarter")
                print("  'o' - deposit a one dollar")
                print("  'f' - deposit a five dollar")
                print("  'c' - cancel the purchase")
            entered_payment = input('Indicate your deposit: ')
            if entered_payment == 'c':
                # Dimes
                num_of_dimes01 = (payment * 100) // 10
                # Nickels
                amount_left_after_dimes01 = (payment * 100) - (num_of_dimes01 * 10)
                num_of_nickels01 = amount_left_after_dimes01 / 5
                print("Please take the change below.")
                print(f'   {int(num_of_dimes01)} dimes')
                print(f'   {int(num_of_nickels01)} nickels')

                # Updating stock
                nickels = nickels - int(num_of_nickels01)
                dimes = dimes - int(num_of_dimes01)
                break

            passed_thru_try = False
            try:
                # Allow input of 'n', 'd', 'q', 'o' and 'f' and increment accordingly
                if entered_payment == 'n':
                    entered_payment = 0.05
                    nickels = nickels + 1
                elif entered_payment == 'd':
                    entered_payment = 0.1
                    dimes = dimes + 1
                elif entered_payment == 'q':
                    entered_payment = 0.25
                    quarters = quarters + 1
                elif entered_payment == 'o':
                    entered_payment = 1
                    ones = ones + 1
                elif entered_payment == 'f':
                    entered_payment = 5
                    fives = fives + 1
                else:
                    passed_thru_try = True
                    print(f'Illegal selection: {entered_payment}')

                # Calculating payment due
                if not passed_thru_try:
                    payment = payment + float(entered_payment)
                    paymentDue = price - payment
                    num_of_paymentDue_dollars = int(paymentDue // 1)
                    num_of_paymentDue_cents = int(paymentDue % 1 * 100)
                    if num_of_paymentDue_dollars <= 0:
                        print(f'Payment due: {num_of_paymentDue_cents} cents')
                    else:
                        print(f'Payment due: {num_of_paymentDue_dollars} dollars and {num_of_paymentDue_cents} cents')


            except ValueError:
                print(f'Illegal selection: {entered_payment}')

            # Calculating payment and balance in nickels, dimes, quarters, ones and fives
            if payment >= price:
                sum_of_price = sum_of_price + price
                print(f'Amount Paid: {sum_of_price}')

                # Calculating balance
                balance = payment - price
                # Dimes
                num_of_dimes = int(balance // 0.1)
                # Nickels
                amount_left_after_dimes = balance - (balance - num_of_dimes * 0.1)
                num_of_nickels = int(amount_left_after_dimes // 0.05)

                # Updating the stock
                nickels = nickels - num_of_nickels
                dimes = dimes - num_of_dimes

                # Printing change
                print("Please take the change below.")
                print(f'   {num_of_dimes} dimes')
                print(f'   {num_of_nickels} nickels')

                not_yet_quit = False
                count = 0

#      GROUP 8 MEMBERS
# Kisakye Joshua 2021/BSE/062/PS
# Kibalama James 2021/BSE/058/PS
# Abaho Davis 2021/BSE/001/PS
# Amos Merber 2021/BSE/018/PS
# Ntwari Reagan 2021/BSE/134/PS

#DATE: 21/02/2022



