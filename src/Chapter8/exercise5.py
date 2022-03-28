# opening the file

open_file = open(input("Enter File: " ),"r")

count = 0

# reading through each line
for line in open_file:
    if line.startswith('From '):
        count += 1
        each_line = line.split()

        # extracting the email
        for i in range(len(each_line)):
            email = each_line[1]
          print(email)
print(f'There were {count} lines in the file with From as the first word')
