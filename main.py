from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_to_string = f.read()
    return file_to_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    all_characters = count_characters(text)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {count_words(text)} total words\n-------- Character Count --------")
    for dict in sort_dict(all_characters):
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
main()