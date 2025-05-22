from stats import get_num_words
from stats import get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
