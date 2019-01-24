"""This program uses differents uses of lists in python.
"""

# list of men (name, age, salary)
men = [
	["Joe DONALD", 43, 140_206.500],
	["Maxime VICTAL", 33, 1_000_000.000],
	["Mamkoul JAGA", 57, 2_345_000.213],
]

women = [
	["Mafouta RICY", 22, 1_100_000.500],
	["Caroline DAVYLI", 40, 800_009.000],
	["Jetaime Boteh", 26, 487_900],
	["Vitaline KOUA", 19, 2_345_000.213],
	["Jacqueline Bouviama", 57, 2_345_000.213],
	["Joe CLARAM", 57, 200_500.213],
]
print("===Program starts ===")
print(f"List of men : {men}")
print(f"List of women : {women}")

# method 'append', 'insert', 'extend' 
print("===Add 2 new men :===")
tow_men = []
for i in range(2):
	man = []	
	man.append(int(input("Age :")))
	man.insert(0,input("Name :"))
	man.append(float(input("Salary :")))
	tow_men.append(man)
print(f"List of 2 new men : {tow_men}")
men.extend(tow_men)
print(f"New list of men : {men}")

# method 'sort' and 'reverse'
print("===Sorting lists===")
men.sort(key=lambda man: man[2], reverse=True)
print(f"Men sorted by descending salary : {men}")
women.sort(key=lambda man: man[1], reverse=True)
women.reverse()
print(f"Women sorted by ascending age : {women}")

# method 'copy', slicing, and list comprehension
print("===List of men and women with salary greather than 1_000_000 ===")
population = men.copy()
population.extend(women[:])
millionaires = [person for person in population if person[2] >= 1_000_000.0]
print(f"Liste of millionaires : {millionaires}")
# function 'zip', list compregension
print("===List of possible couples===")
possible_couples = [(man[0], woman[0]) for man in men for woman in women]
print(f"Liste of possible couples : {list(possible_couples)}")



