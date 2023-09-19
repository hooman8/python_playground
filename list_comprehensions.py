names = ["bruce", "amy", "zack"]
my_list = []
for name in names:
    my_list.append(len(name))
print("before: ", my_list)

my_list = [name for name in names if len(name) % 2 != 0]

print("After: ", my_list)

names_string = "Nina,Zhina,Ruby,Rber"
names_list = names_string.split(",")
" - ".join(names_list)
my_num = [1, 2, 3, 4]
", ".join([str(num * 2) for num in my_num])

list_comp = [x**2 for x in range(10) if x % 2 == 0]
gen_comp = (x**2 for x in range(10) if x % 2 == 0)
type(gen_comp)


names = ["Nina", "Max", "Jimmy"]
upper_name = []
for name in names:
    upper_name.append(name.upper())

my_names_upper = [name.upper() for name in names]
# call list on range to see what's inside of it
list(range(0, 4))
list(range(1, 5, 2))

[num * num for num in range(6)]

[("length", len(name)) for name in names]
", ".join([f"name is {name}" for name in names])


even_squares = [num * num for num in range(6) if num % 2 == 0]
", ".join([str(even_square) for even_square in even_squares])

squares = [num * num for num in range(6)]
sum(squares)

min(squares)
max(squares)
sorted(squares)
sorted(sorted, reverse=True)

lottery_numbers_string = "4, 5, 134, 10"
list(lottery_numbers_string)
max([int(num) for num in lottery_numbers_string.split(", ")])
