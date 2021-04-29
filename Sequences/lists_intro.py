computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

print(computer_parts)

# Lists are mutable; Strings are not

# Immutable types: int, float, bool, strings

#Replace items in list with index
# computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts)
