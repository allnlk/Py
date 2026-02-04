import requests
import re

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text


text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)

words = text.split()


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_words[:10]
for word, count in top_10:
    print(word, count)


cats_api = "https://api.thecatapi.com/v1/breeds"
response = requests.get(cats_api)
breeds = response.json()
weights = []
lifespans = []

country_count = {}

def mean(data):
    return sum(data) / len(data)

def median(data):
    data = sorted(data)
    n = len(data)
    middle = n // 2

    if n % 2 == 0:
        return (data[middle - 1] + data[middle]) / 2
    else:
        return data[middle]

def standard_deviation(data):
    m = mean(data)
    total = 0

    for x in data:
        total += (x - m) ** 2

    variance = total / len(data)
    return variance ** 0.5

def parse_range(text):
    parts = text.split('-')
    low = float(parts[0].strip())
    high = float(parts[1].strip())
    return (low + high) / 2

for breed in breeds:
    weight = breed.get("weight", {}).get("metric")
    if weight:
        weights.append(parse_range(weight))

        life = breed.get("life_span")
        if life and "-" in life:
            lifespans.append(parse_range(life))

        country = breed.get("origin", "Unknown")
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

print("CAT WEIGHT (kg)")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", mean(weights))
print("Median:", median(weights))
print("Std Dev:", standard_deviation(weights))

print("\nCAT LIFESPAN (years)")
print("Min:", min(lifespans))
print("Max:", max(lifespans))
print("Mean:", mean(lifespans))
print("Median:", median(lifespans))
print("Std Dev:", standard_deviation(lifespans))

print("\nCOUNTRY FREQUENCY TABLE")
for country, count in country_count.items():
    print(country, count)

