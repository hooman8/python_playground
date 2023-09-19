my_string = "hello, there!"
my_string[7:13]
my_string[:13]  # start from the begining
my_string[7:]  # go to the end
my_string[-1]  # returns the last index

"""
Making a shallow copy of the names list. The slicing operation [:] returns a new list
"""
names = ["nina", "max"]
new_names = names[:]
new_names.append("george")


my_list = list(range(11))
my_list[::2]  # interval
# [0, 2, 4, 6, 8, 10]
my_list[::-1]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
