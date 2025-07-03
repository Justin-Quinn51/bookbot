from stats import number_of_words
from stats import count_characters
from stats import get_sorted_char_list
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = number_of_words(book_text)
    sentence = f"{word_count} words found in the document"
    dictionary = count_characters(book_text)
    sorted_char_list = get_sorted_char_list(count_characters(book_text))
    # print(sentence)
    # print(dictionary)
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------\n"
    )
    for item_dict in sorted_char_list:
        print(f"{item_dict['char']}: {item_dict['num']}")
    print("============= END ===============")


main()
# "./books/frankenstein.txt"
# books/frankenstein.txt...\
