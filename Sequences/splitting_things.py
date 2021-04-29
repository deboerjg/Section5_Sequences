panagram = """The quick brown fox jumped over the lazy dog"""


words = panagram.split() # Split defaults to splitting one or more whitespaces
print(words)

numbers = "9,233,372,036,854,775,807"
print(numbers.split(sep=","))


# Mini Challenge: Replace list of string values with list of integers
values_list = ['9', '223', '036', '854', '775', '807']

# My solution
value_int = []
for values in values_list:
    value_int.append(int(values))

print(value_int)

# other solution
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)