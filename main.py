from stats import count_words 

def get_book_text(filepath):
    with open(filepath) as f:
        file_to_string = f.read()
    return file_to_string

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {count_words(text)} total words")

main()