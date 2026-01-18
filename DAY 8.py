dog = {}
dog = {
    'name': 'Siya',
    'color':'white',
    'breed':'chihua',
    'legs':'short',
    'age':'six'
}
print(dog)

student = {
    'first_name':'Walker',
    'last_name':'Forest',
    'gender':'m',
    'age':'20',
    'marital status': 'single',
    'skills':'programming',
    'country':'USA',
    'city':'Chicago',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'] = 'Arabian Language', 'Singer'
print(student['skills'])

keys = student.keys()
print(keys)


values = student.values()
print(values)

print(student.items())

print(student.pop('skills'))
del student