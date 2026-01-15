empty_tuple = ()
empty_tuple = tuple()
sisters = ('Sonya', 'Kate', 'Ann')
brothers = ('Mykyta', 'Danya')
siblings = sisters + brothers
print(siblings)
print(len(siblings))

siblings = list(siblings)
siblings[0] = 'Jane'
siblings = tuple(siblings)
print(siblings)

father_and_mother = tuple()
mother = ('Julia',)
father = ('Sergiy',)
father_and_mother = mother + father
family_members = siblings + father_and_mother
print(family_members)

siblings = family_members[:5]
parents = family_members[5:]
print("Siblings:", siblings)
print("Parents:", parents)

food_stuff_tp = tuple()
fruits = ('banana', 'apple', 'orange', 'pomelo')
vegetables = ('carrot', 'potato', 'cabbage')
animal = ('dog', 'cat', 'pig', 'cow')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
middle_two_items = food_stuff_lt[4:6]
print(middle_two_items)


first_three = food_stuff_lt[:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


