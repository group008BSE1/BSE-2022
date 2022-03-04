file_name = input("Enter file name: ")
open_file = open(file_name,"r")

for line in open_file:
    line = line.upper()
    print(line.rstrip())