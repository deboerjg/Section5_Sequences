# Tuples are ordered sequences
# Tuples are immutable
# Tuples are enclosed in parantheses

# welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
# bad = ("Bad Company", "Bad Company", 1974)
# budgie = ("Nightflight", "Budgie", 1981)
# imelda = ("More Mayhem", "Emilda May", 2011)
# metallica = ("Ride the Lighting", "Metallica", 1984)

# Tuples use less memory than lists, less overhead from functions that mutate list
# Tuples can save integrity of data, can prevent bugs in your program
# Incorrect data can be worse than crashes in the program

# album, artist, year = metallica
# print(album, artist, year, sep=", ")
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
# name, length, width, height, price = table
# print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lighting", "Metallica", 1984),
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))



