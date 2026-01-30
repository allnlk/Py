import re

paragraph = (
    'I love teaching. If you do not love teaching what else can you love. '
    'I love Python if you do not love something which can give you all the '
    'capabilities to develop an application what else can you love.'
)

words = re.findall(r'\b\w+\b', paragraph.lower())

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent_word = max(word_count, key=word_count.get)

print("Most frequent word:", most_frequent_word)
print("Frequency:", word_count[most_frequent_word])



txt = (
    "The position of some particles on the horizontal x-axis are -12, -4, -3 "
    "and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
)

points = re.findall(r'-?\d+', txt)

points = list(map(int, points))

sorted_points = sorted(points)

distance = max(sorted_points) - min(sorted_points)

print("Extracted points:", points)
print("Sorted points:", sorted_points)
print("Distance:", distance)


def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def most_frequent_words(text):
    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [(count, word) for word, count in sorted_words[:3]]


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

print(most_frequent_words(cleaned_text))