def count_words(text):
    return len(text.split())

def count_characters(text):
    count={}
    for char in text.lower():
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count
def book_report(data):
    sorted_list=[]
    for key in data:
        temp_dict={}
        if key.isalpha():
            temp_dict["char"]=key
            temp_dict["num"]=data[key]
            sorted_list.append(temp_dict)
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list





