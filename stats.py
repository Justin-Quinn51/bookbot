def number_of_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def count_characters(text):
    lowercase = text.lower()
    dictionary = {}
    character = None
    for character in lowercase:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary


def get_sorted_char_list(dictionary):
    dict_items = dictionary.items()
    char_list = []
    for char, num in dict_items:
        if not char.isalpha():
            continue
        char_list.append({"char": char, "num": num})
    char_list.sort(key=lambda single_dict: single_dict["num"], reverse=True)
    return char_list
