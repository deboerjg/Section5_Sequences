a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76 # Unpacking a tuple
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76
x, y, z = data
print(x)
print(y)
print(z)

# Can unpack any sequence type

print("Unpacking a list")
data_list = [12,13,14]
p, q, r = data_list
print(p)
print(q)
print(r)

# Tuples can always be unpacked successfully, since you cannot append things to them
