numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_less = [i for i in numbers if i <= 0 ]
print(numbers_less)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for sublist in list_of_lists for num in sublist]
print(flat_list)

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
comb = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(comb)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]
print(dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
combo = [
    f"{name} {last_name}"
    for[(name, last_name)] in names
]
print(combo)

line_params = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1),
    y1 - ((y2 - y1) / (x2 - x1)) * x1
)
a, b = line_params(1, 2, 3, 6)
print(a, b)