# using int
birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print(age)

# using type
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# converting weight
weight = input("What is your weight? ")
pounds_to_kilo=.45 * int(weight)
print(pounds_to_kilo)
