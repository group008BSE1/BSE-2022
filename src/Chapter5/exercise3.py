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
            print(f'Total :{int(num_of_cents)} cents ')
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
        num_of_paymentDue_dollars = int(float(price) // 1)
        num_of_paymentDue_cents = (int(float(price) * 100)) % 100
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
                if num_of_paymentDue_dollars < 1:
                    print(f'Payment due: {num_of_paymentDue_cents} cents')
                else:
                    print(f'Payment due: {num_of_paymentDue_dollars} dollars and {num_of_paymentDue_cents} cents')
            entered_payment = input('Indicate your deposit: ')
            if entered_payment == 'c':
                # Quarters
                num_of_quarters01 = int(payment * 100 // 25)
                # Dimes
                amount_left_after_quarters01 = payment - (num_of_quarters01 * 0.25)
                num_of_dimes01 = int((amount_left_after_quarters01 * 100) // 10)
                print(f'no_of_dimes{amount_left_after_quarters01}')
                # Nickels
                amount_left_after_dimes01 = amount_left_after_quarters01 - (num_of_dimes01 * 10)
                num_of_nickels01 = int((amount_left_after_dimes01 * 100) // 5)
                print("Please take the change below.")
                if num_of_quarters01 != 0:
                    print(f'   {int(num_of_quarters01)} Quartes')
                if num_of_dimes01 != 0:
                    print(f'   {int(num_of_dimes01)} dimes')
                if num_of_nickels01 != 0:
                    print(f'   {int(num_of_nickels01)} nickels')

                # Updating stock
                nickels = nickels - int(num_of_nickels01)
                dimes = dimes - int(num_of_dimes01)
                quarters = quarters - int(num_of_quarters01)
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
                if (not passed_thru_try):
                    payment = payment + float(entered_payment)
                    paymentDue = price - payment
                    if paymentDue > 0:
                        num_of_paymentDue_dollars = int(paymentDue // 1)
                        num_of_paymentDue_cents = int(round(paymentDue % 1 * 100))
                        if num_of_paymentDue_dollars <= 0:
                            print(f'Payment due: {num_of_paymentDue_cents} cents')
                        else:
                            print(f'Payment due: {num_of_paymentDue_dollars} dollars and {num_of_paymentDue_cents} cents')
                    elif paymentDue == 0:
                        sum_of_price = sum_of_price + price
                        print('Please take the change below')
                        print('  No change due')
                        break
                    else:
                        # Calculating change in terms of dimes and nickels
                        paymentDue = abs(paymentDue)
                        print(paymentDue,'paydue')
                        # Quarters
                        num_of_quarters = int(paymentDue * 100 // 25)
                        # Dimes
                        amount_left_after_quarters = paymentDue - (num_of_quarters * 0.25)
                        num_of_dimes = int((amount_left_after_quarters * 100) // 10)
                        # Nickels
                        amount_left_after_dimes = amount_left_after_quarters - (num_of_dimes * 0.1)
                        num_of_nickels = int((amount_left_after_dimes * 100) // 5)



                        # subtracting change from the stock in form of coins awarded to buyer

                        quarters = quarters - num_of_quarters
                        dimes = dimes - num_of_dimes
                        nickels = nickels - num_of_nickels

                        # updating total of purchase prices
                        sum_of_price = sum_of_price + price
                        print('price',price)
                        print('sum_of_price',sum_of_price)

                        print("Please take the change below.")
                        if num_of_quarters != 0:
                            print(f'   {int(num_of_quarters)} Quarters')
                        if num_of_dimes != 0:
                            print(f'   {int(num_of_dimes)} dimes')
                        if num_of_nickels != 0:
                            print(f'   {int(num_of_nickels)} nickels')
                        break
            except ValueError:
                print(f'Illegal selection: {entered_payment}')


#      GROUP 8 MEMBERS
# Kisakye Joshua 2021/BSE/062/PS
# Kibalama James 2021/BSE/058/PS
# Abaho Davis 2021/BSE/001/PS
# Amos Merber 2021/BSE/018/PS
# Ntwari Reagan 2021/BSE/134/PS

#DATE: 21/02/2022





