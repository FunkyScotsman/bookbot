import sys
from stats import get_num_words, get_num_letters, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Process book
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    num_letters = get_num_letters(book_text)
    sorted_letters = sort_char_count(num_letters)

    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # Word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count section
    print("--------- Character Count -------")
    for item in sorted_letters:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")

    # Footer
    print("============= END ===============")




main()