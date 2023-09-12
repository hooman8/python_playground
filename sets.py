# sets are mutable data type that allows you to store immutable types in an unsorted way
# sets are mutable because you can add and remove items from them
# They can contain immutable types, but not list, sets, or dic which are mutable
# sets are good for fast search

myset = {}  # this gives you a dictionary
set()  # empty set
type({1, 2, 3, 4})
myset = {1, 2, 3, 4, 2}  # note that dups are removed
names = ["Tom", "Jerry", "Matt"]
set(names)
# shortcut to check for mutability
hash(names)  # list is unhashable
hash(1)
hash("name")
my_set = {"a", 1, 3, 4}  # set is unordered so cannot use my_set[0]
my_set.add("Orange")
my_set.discard("a")

colors = {"red", "orange"}
numbers = {1, 2, 3, 4}
numbers.update(colors)  # {1, 2, 3, 4, 'orange', 'red'}
