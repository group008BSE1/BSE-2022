# opening file
try:
    measlesfile = open("measles.txt","r")
except:
    exit()

#output file
output_file = input("Enter output file: ")
opened_file = open(output_file,"w")

year = input("Enter the year: ")

for line in measlesfile:
    # generating year portion from behind.
    year_portion = line[-5: -1]
    if year_portion.startswith(year):
        opened_file.write(line)
    elif year == 'all' or year == 'ALL' or year == '':
        opened_file.write(line)
    else:
        print('Invalid input')
        exit()









