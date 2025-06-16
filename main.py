from stats import count_characters,count_words,book_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text=get_book_text("books/frankenstein.txt")
    number_of_words=count_words(book_text)
    all_characters_in_book=count_characters(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for i in book_report(all_characters_in_book):
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
main()
    