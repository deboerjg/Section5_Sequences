# for index, character in enumerate("abcdefgh"): # Enumerate is efficient way to get indexes and the object from iterables
#     print(index, character)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
0
