countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

def change_to_upper(country):
    return country.upper()

countries_upper = map(change_to_upper, countries)
print(list(countries_upper))

def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

def change_to_up(name):
    return name.upper()
names_upper = map(change_to_up, names)
print(list(names_upper))

def is_land(country):
    return 'land' in country.lower()
land = filter(is_land, countries)
print(list(land))


def is_six(country):
    if len(country) == 6:
        return True
    return False
six = filter(is_six, countries)
print(list(six))

def is_six_more(country):
    if len(country) >= 6:
        return True
    return False
six_more = filter(is_six_more, countries)
print(list(six_more))

def starts_with_e(country):
    return country.startswith('E')

countries_starting_with_e = filter(starts_with_e, countries)
print(list(countries_starting_with_e))

def to_lowercase(country):
    return country.lower()

def contains_land(country):
    return 'land' in country

def to_uppercase(country):
    return country.upper()

# chain map → filter → map
result = map(
    to_uppercase,
    filter(
        contains_land,
        map(to_lowercase, countries)
    )
)

print(list(result))

def get_string_lists(lst):
    return [item for item in lst if type(item) == str]
mixed_list = ['apple', 42, 'banana', True, 'cherry', 3.14]
strings_only = get_string_lists(mixed_list)
print(strings_only)


from functools import reduce
def add(a, b):
    return a + b
total = reduce(add, numbers)
print(total)

all_but_last = countries[:-1]
last_country = countries[-1]
sentence_start = reduce(lambda a, b: a + ', ' + b, all_but_last)
full_sentence = f"{sentence_start}, and {last_country} are north European countries."
print(full_sentence)


