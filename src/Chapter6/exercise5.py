str = 'X-DSPAM-Confidence: 0.8475 '

# Getting start and ending index
start_index = str.find('0')
end_index = str.find('5')

# Slicing the str
value = str[start_index:end_index + 1]

# Converting into floating point
value = float(value)
print(value)