def add_two_numbers():
    pam_one = 2
    pam_two = 6
    sum = pam_two + pam_one
    return sum
print(add_two_numbers())

def area_of_circle():
    radius = (int(input('Enter r: '))) ** 2
    pi = 3.14
    area = radius * pi
    return area
print(area_of_circle())

def add_all_nums(*args):
    total = 0
    for item in args:
        if type(item) not in (int, float):
            return f"Invalid input: {item} is not a number"
        total += item
    return total
print(add_all_nums())

def convert_celsius_to_fahrenheit():
    celsius = int(input('Enter °C: '))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit())

def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined (division by zero)"
        return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn():
    if a == 0:
        return "This is not a quadratic equation"
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return "No real solutions"

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def capitalize_list_items():
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
        return capitalized_lst

def add_item (lst, item):
    lst.append(item)
    return item

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


def sum_of_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i
        return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def sum_of_odds(num):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
            return total

def sum_of_even(n):
    total = 0
    for i in range (1, n + 1):
        if i % 2 == 0:
            total += i
        return total

def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")


def factorial (n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result

def is_empty(param):
    if not param:
        return True
    else:
        return False

def calculate_mean(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def calculate_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]


def calculate_mode(lst):
    if not lst:
        return None
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    if len(modes) == len(frequency):
        return None
    return modes


def calculate_range(lst):
    if not lst:
        return None
    return max(lst) - min(lst)

def calculate_variance(lst):
    if not lst:
        return None
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    var = calculate_variance(lst)
    if var is None:
        return None
    return var ** 0.5

numbers = [1, 2, 2, 3, 4, 5]

print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))


def greet(name="Guest"):
    print(f"Hello, {name}!")

def show_args(**kwargs):
    output = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    print(f"Received: {output}")
