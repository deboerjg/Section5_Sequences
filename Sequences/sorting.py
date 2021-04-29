pangram = "The quick brown jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.6, 1.6]
sorted_numbers = sorted(numbers) # creates a different list
print(sorted_numbers)
print(numbers)

numbers.sort() # doesn't create a new list
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)
print(missing_letter)

names = ['Graham',
         'John',
         'terry',
         'eric',
         'Terry',
         'micheal',
         ]

names.sort(key = str.casefold)
print(names)

