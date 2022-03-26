people = ["Frazer", "Bob", "Alice"]
ages = [16, 29, 43]

mapped_people = list(map(lambda person, age: (person, age), people, ages))

print(mapped_people)

squares = [i**2 for i in range(15)]

print(squares)

rooted_nums = list(map(lambda square: int(square**0.5), squares))

print(rooted_nums)

test_scores = [52, 95, 17, 20]

passing_scores = list(filter(lambda score: score >= 50, test_scores))

print(passing_scores)

zipped_people = list(zip(people, ages))

print(zipped_people)

for person, age in zip(people, ages):
	print(f"{person} is {age} years old.")
