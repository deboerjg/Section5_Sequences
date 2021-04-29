# Mutable objects: list, dict, set, bytearray
shopping_list = ["Siracha", "Eggs", "Ground Turkey", "Toothpaster"]
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["Rubbers"]
print(shopping_list)
print(id(shopping_list))

print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding Creampie")
b.append("Creampie") # Methods like append, are functions attached to an object, they use dot notation
print(c)
print(d)