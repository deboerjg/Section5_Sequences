menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]

# Challenge: write code prints out all the meals in menu without spam

# My answer
for meal in menu:
    top_index = len(meal) - 1
    for index, ingredient in enumerate(reversed(meal)):
        if ingredient == "spam":
            del meal[top_index - index]
    print(", ".join(meal))



# # Second approach
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ") # Can't use sep because you need multiple objects
#     print()

