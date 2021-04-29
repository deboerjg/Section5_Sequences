available_parts = [('computer', 500),
                   ('monitor', 100),
                   ('keyboard', 50),
                   ('mouse', 25),
                   ('HDMI cable', 5),
                   ('DVD drive', 20),
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)] #THIS WILL MAKE SENSE LATE
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))


print(valid_choices)



current_choice = "-"
computer_parts = [] # Create empty list
cost = 0

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice)-1
        chosen_part = available_parts[index][0]
        if chosen_part in computer_parts:
            # It's already in, so remove it
            print("Removing {}".format(available_parts[int(current_choice)-1][0]))
            computer_parts.remove(chosen_part)
            cost -= available_parts[int(current_choice)-1][1]
        else:
            print("Adding {}".format(available_parts[int(current_choice)-1][0]))
            computer_parts.append(chosen_part)
            cost += available_parts[int(current_choice)-1][1]

        print("Your list now contains: {}".format(computer_parts))
        print("Your current cost is {}".format(cost))
    else:
        print("Please add options from the list below")
        for number, (part, price) in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))


    current_choice = input()

print(computer_parts)
print("Your current cost is {}".format(cost))
