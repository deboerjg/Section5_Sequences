# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
#
# print(len(even))
# print(len(odd))
#
# print(sum(even))
# print()
#
# print("Mississippi".count("issi"))
#
# # Method is same as function, but is bound to an object
# s = "Mississippi"

empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

# even.extend(odd)
# another_even = even
# print(another_even)
#
# even.sort(reverse=True) # Sort does not create another copy, otherwise known as sorting 'in place'
# print(even)
# print(another_even)

#Create a list by concatinating lists
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)