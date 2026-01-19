age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    age <= 18
    need = 18 - age
    print(f'You need {need} more years to learn to drive.')

my_age = 18
your_age = int(input('Enter your age: '))

if my_age == your_age:
    print('We are the same age!')
else:
    age_dif = abs(my_age - your_age)
    year_text = "year" if age_dif == 1 else "years"

    if your_age > my_age:
        print(f"You are {age_dif} {year_text} older than me.")
    else:
        print(f"I am {age_dif} {year_text} older than you.")



first_num = int(input('Enter number one: '))
second_num = int(input('Enter number two: '))
if first_num > second_num:
    print(f'{first_num} is greater than {second_num}')
else:
    print(f'{second_num} is greater than {first_num}')

if first_num == second_num:
    print(f'{first_num} is equal to {second_num}')


score_tab = input('Enter sh: ')
if score_tab == 'sh':
    print("""
90–100 : A
80–89  : B
70–79  : C
60–69  : D
0–59   : F
""")

student_score = int(input('Enter you score: '))
if student_score <= 100 and student_score >= 90:
    print(f'{student_score}, A')
elif student_score <= 89 and student_score >= 80:
    print(f'{student_score}, B')
elif student_score <= 79 and student_score >= 70:
    print(f'{student_score}, C')
elif student_score <= 69 and student_score >= 60:
    print(f'{student_score}, D')
elif student_score <= 59 and student_score >= 0:
    print(f'{student_score}, F')


month = input('Enter month: ').lower()
if month in ('september', 'october', 'november'):
    print('The season is Autumn')
elif month in ('december', 'january', 'february'):
    print('The season is Winter')
elif month in ('march', 'april', 'may'):
    print('The season is Spring')
elif month in ('june', 'july', 'august'):
    print('The season is Summer')
else:
    print('Invalid month')


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_list = input('Enter sh: ')
add = input('Enter fruit: ').lower()
if fruit_list == 'sh':
    print(fruits)
if add in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(add)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(skills[middle])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python skill found')
    else:
        print('Python skill not found')
skills = person.get('skills', [])

if skills == ['JavaScript', 'React']:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')
if person['is_married'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} lives in Finland. He is married.")






