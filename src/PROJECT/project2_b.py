
def convert_income_level_to_text(income_level):
    '''
        this function converts the entered income digits to text
    '''
    if income_level == 1:
        return "WB_LI "
    elif income_level == 2:
        return 'WB_LMI'
    elif income_level == 3:
        return 'WB_UMI'
    elif income_level == 4:
        return 'WB_HI'

def income_level_extract(line):
    '''
        This function returns the income level per line
    '''
    extract01 = line[51:57]
    return extract01.strip()

def percentage_extract(line):
    '''
        this function returns the int of the percentage per line
    '''
    extract = line[58:61]
    return int(extract)

def country_extract(line):
    '''
        This function returns the country per line
    '''
    extract = line[:51]
    return extract.strip()

def year_extract(line):
    extract = line[-6:-1]
    return extract.strip()


def open_file():
    # checking if file name exists
    input_file_name = ""
    while input_file_name != "measles.txt" and input_file_name != 'measles.short.txt':
        input_file_name = input('Enter Input File Name: ')

    # opening file
    file_object = open(input_file_name, 'r')
    return file_object

def process_file(file_object):
    while True:
        try:
            year_input = int(input('Enter Year: '))
            break
        except:
            print("invalid year!")
    year_input = str(year_input)

    while True:
        try:
            income_num = int(input('Enter Income Level: '))
            break
        except:
            print("invalid input!")
    income_level = convert_income_level_to_text(income_num)

    count = 0
    percentage_sum = 0
    min_value = 100
    max_value = 0
    for line in file_object:

        # getting necessary extracts
        income = income_level_extract(line)
        percentage = percentage_extract(line)
        country = country_extract(line)
        year = year_extract(line)
        # print(income_level)

        # using the extracts to report specific information
        if year.startswith(year_input) and income == income_level:
            count += 1
            percentage_sum += percentage

            # getting minimum percentage and using it to get country with minimum percentage
            if percentage < min_value:
                min_value = percentage
                min_country = country
            if percentage > max_value:
                max_value = percentage
                max_country = country
    # printing report
    print(f'Count: {count}')
    print(f'Average percentage: {percentage_sum / count}')
    print(f'Country with the lowest percentage: {min_country}')
    print(f'Country with the highest percentage: {max_country}')

def main():
    file_object = open_file()
    process_file(file_object)

#Initiating the program
main()



