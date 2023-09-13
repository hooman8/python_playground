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
