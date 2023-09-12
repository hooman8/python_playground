# immutable - light weight collections used to keep track of related but different items
# read only snapshot of your data
()
my_tup = ()
type(my_tup)
my_tup = "hi"  # the type is going to be a string
# tuple with a single item needs to have a comma

student = ("Marcy", 21, "history", 3.5)
name, age, subject, gpa = student
name, age, subject, _ = student  # _ means ignore a single value
