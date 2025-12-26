def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    all_characters = dict()
    for character in string:
        character = character.lower()
        if character in all_characters.keys():
            all_characters[character] += 1
        else:
            all_characters[character] = 1
    return all_characters

def sort_dict(dictionary):
    sorted_list = list()
    for k in dictionary:
        sorted_dict = dict()
        sorted_dict["char"] = k
        sorted_dict["num"] = dictionary[k]
        sorted_list.append(sorted_dict)
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list