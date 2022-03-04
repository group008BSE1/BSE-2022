#prompt user to enter a file name
file_name = input("Enter file name: ")
#accessing the text file and storing it as a storing it
open_file = open(file_name,"r")
count = 0
sum = 0
#moving through text file line by line
for line in open_file:
    #find lines that start with  “X-DSPAM-Confidence:
    if line.startswith("X-DSPAM-Confidence: "):
        float_str = line.strip("X-DSPAM-Confidence: ")
        float_values = float(float_str)
        count += 1
        sum += float_values
#calculating the average
average = sum/count
#formating the average to 12 decimal places
average = format(average,".12f")

print(f'Average spam confidence: {average}')

