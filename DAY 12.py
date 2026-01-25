import random

def random_user_id():
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    user_id = ' '
    for i in range(6):
        user_id += random.choice(characters)
    return user_id
print(random_user_id())

def user_id_gen_by_user():
    num_of_chr = int(input('Enter the number of characters: '))
    num_of_ids = int(input('Enter the number of IDs: '))
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ids = []
    for i in range(num_of_ids):
        user_id = ''
        for j in range(num_of_chr):
            user_id += random.choice(chars)
        ids.append(user_id)
    return ids
print(user_id_gen_by_user())

def  rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return  f"rgb({r},{g},{b})"
print(rgb_color_gen())

def list_of_hexa_colours(num_colours):
    hex_chars = '0123456789abcdef'
    colours = []

    for i in range(num_colours):
        color = '#'
        for j in range(6):
            color += random.choice(hex_chars)
        colours.append(color)

    return colours
print(list_of_hexa_colours(5))

def list_of_rgb_colors(num_colors):
    colors = []

    for i in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r},{g},{b})"
        colors.append(color)
    return colors
print(list_of_rgb_colors(5))


def generate_colors(color_type, num_colors):
    colors = []
    if color_type.lower() == 'hexa':
        hex_chars = '0123456789abcdef'
        for i in range(num_colors):
            color = '#'
            for j in range(6):
                color += random.choice(hex_chars)
            colors.append(color)

    elif color_type.lower() == 'rgb':
        for i in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"rgb({r},{g},{b})"
            colors.append(color)

    else:
        return "Invalid color type! Choose 'hexa' or 'rgb'."

    return colors

    print(generate_colors('hexa', 3))
    print(generate_colors('hexa', 1))
    print(generate_colors('rgb', 3))
    print(generate_colors('rgb', 1))

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))
print("Original list:", my_list)

def seven_unique_numbers():
    return random.sample(range(10), 7)

print(seven_unique_numbers())