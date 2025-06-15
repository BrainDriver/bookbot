def count_words(text):
    print(f"{len(text.split())} words found in the document")

def count_characters(text):
    count={}
    for char in text.lower():
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count
