from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    #count_words(get_book_text("books/frankenstein.txt"))
    #print(get_book_text("books/frankenstein.txt"))
    print(count_characters(get_book_text("books/frankenstein.txt")))

main()
    