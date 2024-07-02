# Defining a single-line string
string = 'Python'

# Defining a multi-line string
sentence = '''I hope you
are enjoying
python'''

# Printing the multi-line string
print(sentence)

# String concatenation
language = 'python'
platform = 'iCodeGuru'
# Concatenating two strings with a space in between
print(language + ' ' + platform)

# Slicing
# Slicing has a thumb rule that it includes the starting index and excludes the ending index
# Extracting characters from index 0 to 4 (5 is excluded)
print(platform[0:5])
# Extracting characters from index 5 to the end of the string
print(platform[5:])

# Reversing the string
# Slicing with a step of -1 to reverse the string
print(platform[::-1])

# Skipping characters while slicing
# Extracting characters from index 0 to 5 with a step of 2 (every second character)
print(platform[0:6:2])  # start, stop, step