people = ["frazer", "bob", "alice"]

for person in people:
	print(person)

cap_people = []

for person in people:
	cap_p = person.capitalize()
	cap_people.append(cap_p)
	
print(cap_people)

cap_people = [person.capitalize() for person in people]

print(cap_people)

squares = [i**2 for i in range(15)]

print(squares)

even_squares = [i**2 for i in range(15) if i**2 % 2 == 0]

print(even_squares)

some_dictoinary = {i: None for i in range(5)}

print(some_dictoinary)

another_dictionary = {i: j for i, j in zip(range(5), reversed(range(5)))}

print(another_dictionary)

