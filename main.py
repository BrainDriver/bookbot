import sys
from stats import count_characters,count_words,book_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text=get_book_text(sys.argv[1])
    number_of_words=count_words(book_text)
    all_characters_in_book=count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for i in book_report(all_characters_in_book):
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
main()
    