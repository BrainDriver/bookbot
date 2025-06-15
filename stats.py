def count_words(text):
    print(f"{len(text.split())} words found in the document")

def count_characters(text):
    dict={}
    for char in text.lower():
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    return dict
