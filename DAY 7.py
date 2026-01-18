# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['EPAM', 'ZONE 300'])
print(it_companies)

it_companies.remove('Amazon')
print(it_companies)

print(A.union(B))

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))
del it_companies, A, B

print(len(age))
age = set(age)
print(len(age))


sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(unique_words)
print("Number of unique words:", len(unique_words))
