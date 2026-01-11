string_1 = 'Thirty'
string_2 = 'Days'
string_3 = 'Of'
string_4 =  'Python'
space = ' '
unite = string_1 + space + string_2 + space + string_3 + space + string_4
print(unite)


str_1 = 'Coding'
str_2 = 'For'
str_3 = 'All'
space = ' '
reunion = str_1 + space + str_2 + space + str_3
print(reunion)


company = (reunion)
print(company)
print(len(company))

up = company.upper()
print(up)

low = company.lower()
print(low)
print(company.capitalize())
print(company.title())
print(company.swapcase())


cut_first_word = company[6:14]
print(cut_first_word)
print(cut_first_word.find('Coding'))
print(cut_first_word.find('Coding'))
print(reunion.replace('Coding', 'Python'))
first = "Python for Everyone"
print(first.replace("Everyone", "All"))
print(reunion.split())

media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(media.split(", "))


phrase = "Python For Everyone"
words = phrase.split()
acronym = "".join([words[0][0], words[1][0], words[2][0]])
print(acronym)


ph = 'Coding for all'
wrds = ph.split()
abrev = ''.join([wrds[0][0], wrds[1][0], wrds[2][0]])
print(abrev)


position = ph.index("C")
print(position)

pose = ph.index("f")
print(pose)

ok =  "Coding For All People."
print(ok.rfind('I'))
sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

you = "You cannot end a sentence with because because because is a conjunction"
print(you.rindex('because'))


rase = sentence[sentence.find('because because because') : sentence.find('because because because') + len('because because because')]
print(rase)

position = sentence.index('because')
print(position)

company = "Coding For All"
print(company.startswith("Coding"))
print(company.endswith("coding"))

text = '   Coding For All      '
clean_text = text.strip()
print(clean_text)


print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '# '.join(libraries)
print(joined_libraries)

sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(text)

radius = 10
area = 3.14 * radius ** 2
output = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(output)

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

