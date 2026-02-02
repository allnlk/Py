count = 0

with open('C:\\Users\\User\\Downloads\\obama_speech.txt', 'r') as fp:
    lines = fp.readlines()
    num_lines = len(lines)

    for line in lines:
        count += len(line.split())
print('Total number of lines: ', num_lines)
print("Total Words:", count)

with open ('C:\\Users\\User\\Downloads\\michelle_obama_speech.txt', 'r') as file:
    lns = file.readlines()
    num_lns = len(lns)

    for ln in lns:
        count += len(ln.split())
print('Total number of lines: ', num_lns)
print("Total Words:", count)


import json

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as fp:
        countries = json.load(fp)

    language_count = {}

    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    result = []
    for language, count in language_count.items():
        result.append((count, language))

    result.sort(reverse=True)

    return result[:top_n]
print(most_spoken_languages('C:\\Users\\User\\Downloads\\countries_data.json', 10))


def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as fp:
        countries = json.load(fp)

    result = []

    for country in countries:
        result.append({
            'country': country['name'],
            'population': country['population']
        })


    result.sort(key=lambda x: x['population'], reverse=True)

    return result[:top_n]
print(most_populated_countries('C:\\Users\\User\\Downloads\\countries_data.json', 10))


def find_most_frequent_words(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as fp:
        text = fp.read()

    for char in ",.;:!?\"'()[]{}":
        text = text.replace(char, "")

    text = text.lower()
    words = text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    count_list = []
    for word, count in word_count.items():
        count_list.append((count, word))

    count_list.sort(reverse=True)
    return count_list[:top_n]
top_10_words = find_most_frequent_words('C:\\Users\\User\\Downloads\\obama_speech.txt', 10)
print(top_10_words)

with open('hacker_news_csv', 'r', encoding='utf-8') as fp:
    count = 0
    for line in fp:
        if 'python' in line.lower():
            count += 1
print("Number of lines containing 'python':", count)
