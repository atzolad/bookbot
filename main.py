from stats import get_num_words
from stats import get_num_char
from stats import sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    #print(f"{num_words} words found in the document")
    #print(num_chars)
    sorted = sort_dict(num_chars)
    print_report(book_path, num_words, sorted)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, sorted):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")    

main()
            