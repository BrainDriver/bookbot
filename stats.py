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