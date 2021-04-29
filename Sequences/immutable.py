result = True
another_result = True

print(id(result)) # id function:
print(id(another_result))

result = False
print(id(result)) #Gives a different id, because they are immutable, instead creates a new variable

result = "Correct"
another_result = result


print(id(result)) # id function:
print(id(another_result))

result += "ish" # ID changes cause strings are not mutable
print(id(result))
print(id(another_result))

