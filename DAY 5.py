empty_list = list()

lst = ['macos', 'windows', 'linux', 'android', 'ios', 'system']
print(len(lst))

first_item = lst[0]
print(first_item)

middle_item = lst[-4]
print(middle_item)

last_item = lst[-1]
print(last_item)

mixed_data_types = ['alina', '18', '163', 'single', 'kiyv']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))
first_company = it_companies[0]
print(first_company)
middle_company = it_companies[len(it_companies) // 2]
print(middle_company)
last_company = it_companies[-1]
print(last_company)


it_companies[2] = 'epam'
print(it_companies)

it_companies.append('genesis')
print(it_companies)

it_companies.insert(4, 'SoftServe')
print(it_companies)

it_companies[2] = it_companies[2].upper()
print(it_companies)

result = '#; '.join(it_companies)
print(result)

does_exist = 'Facebook' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

first_three = it_companies[0:3]
print(first_three)

last_three = it_companies[-3:]
print(last_three)

middle = it_companies[len(it_companies)//2 : len(it_companies)//2 + 1]
print(middle)

it_companies.remove('Amazon')
print(it_companies)


it_companies.remove('IBM')
print(it_companies)

it_companies.remove('Apple')
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
programming = front_end + back_end
print(programming)


full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, ' Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)
ages.append(min_age)
ages.append(max_age)
ages.sort()
n = len(ages)
middle1 = ages[n//2 - 1]
middle2 = ages[n//2]
median = (middle1 + middle2) / 2
print(median)
average_age = sum(ages) / len(ages)
print(average_age)
range_of_the_ages = max(ages) - min(ages)
print(range_of_the_ages)
com1 = abs(min_age - average_age)
com2 = abs(max_age - average_age)
print(com1)
print(com2)


country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = country
print(scandic)




