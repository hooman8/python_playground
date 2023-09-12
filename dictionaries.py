# dictionaries are mutable, but keys needs to be hashable and therefore immutable
type({"one": 1, "two": 2})

my_number = {"one": [1, 2, 2]}
# dictionaries have no orders
my_number["one"]
my_number.get("one", "default")  # doesnt return an error
my_number["one"] = "two"  # new keys could be added or updated using this technique
my_number["one"]

my_number.items()
my_number.keys()
my_number.values()
