bool  # maps to the constructor for built in true or false
bool(1)
bool([])
bool([1, 2, 3])
bool(None)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1 == list2
list1 is list2  # checks for identity, do these point to the same place in memory?
# dont do a == True, instead a is True
