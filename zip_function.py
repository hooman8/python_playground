# talking about zip
squares = {num: num * num for num in range(11)}
squares.values()
squares.keys()
squares.items()  # returns a list of tuples


players = ["Nina", "Bob", "Alice"]
scores = [100, 5, 97]
zip(players, scores)
for item in zip(players, scores):
    print(item)
# return tuples

for name, score in zip(players, scores):
    print(f"Name: {name} had a score of {score}")

[f"Name: {name} had a score of {score}" for name, score in zip(players, scores)]
# this is going to give you a list of formatted strings

list(zip(players, scores))
dict(zip(players, scores))
