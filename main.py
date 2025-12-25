from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_to_string = f.read()
    return file_to_string

def main():
    text = get_book_text("./books/frankenstein.txt")
    all_characters = count_characters(text)
    print(f"Found {count_words(text)} total words")
    print(all_characters)
main()