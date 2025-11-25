import sys

from stats import (
    clean_output,
    get_character_count,
    get_word_count,
)


def get_book_path(sys_input):
    if len(sys_input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys_input[1]


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for output in sorted_dict:
        print(f"{output['char']}: {output['count']}")
    print("============= END ===============")


def main():
    book_path = get_book_path(sys.argv)
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_dict = clean_output(character_count)
    print_report(book_path, word_count, sorted_dict)


if __name__ == "__main__":
    main()
