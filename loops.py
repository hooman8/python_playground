colors = ["red", "yellow", "white", "green"]
for color in colors:
    print(color)

list(range(0, 3))  # ending point is not inclusive
for num in range(3, 7):
    print(num)

list(enumerate(colors))
# [(0, 'red'), (1, 'yellow'), (2, 'white'), (3, 'green')]

for index, color in enumerate(colors):
    print(f"index: {index} is holding color: {color}")

my_numbers = {"one": 1, "two": 2, "three": 3}
my_numbers.items()
for key, value in my_numbers.items():
    print(f"{key}:{value}")
