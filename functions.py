def my_func():
    print("hi")


# a function that doesnt return anything, if try to assign it its value is None


def add_numbers(x, y):
    return x + y


def add_numbers_with_default(x, y, z=1):
    return x + y + z


add_numbers_with_default(x=1, y=2, z=5)


# dont use mutable type as default arguement
def do_stuff(my_list=[]):
    my_list.append("stuff")
    return my_list


# everytime you call the function you'll be appending to the same list


def do_more_stuff(my_list=None):
    if my_list is None:
        my_list = []
        my_list.append("stuff")
    return my_list
