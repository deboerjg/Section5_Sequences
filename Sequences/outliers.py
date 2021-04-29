# data = [4,5,104,105,110,120,130,130,150,160,170,183,187,188,191,350,360]
data = [1,6]
# del data[:2]
# print(data)
#
# del data[-2:]
# print(data)
min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index] # Deleting items in a list while iterating forward will cause problems
#
# print(data)

# Process low values of the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop] # We delete data up to but not including stop, this only works on sorted lists
print(data)

#Process high values of the list, start processing at the end
start = 0
for index in range(len(data)-1, -1, -1): # Work from the very end
    if data[index] <= max_valid:
        start = index + 1 # Add one, because index is reffering to first item below max, we dont want to delete that value
        break

print(start)
del data[start:]
print(data)

