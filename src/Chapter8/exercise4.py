# opening the file
open_file = open(input("Enter File: "), 'r')

# list of unique words
unique_words = []

# reading the file and splitting words
for line in open_file:
    each_line = line.split()
 # adding all words in the list
    for i in range(len(each_line)):
        each_word = each_line[i]
        if each_word not in unique_words:
            unique_words.append(each_word)

print(unique_words)
