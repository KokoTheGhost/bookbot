from stats import *

def get_book_text():
    """
    Reads the content of the book file and returns it as a string.
    """
    try:
        with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Book file not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to execute the book reading functionality.
    """
    bookPath = 'books/frankenstein.txt'
    bookText = get_book_text()
    totalWords = get_num_words(bookText)
    charCount = get_num_character(bookText)
    sortedCharCount = sort_dict_by_value(charCount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {totalWords} total words")
    print("---------- Character Count -------")
    for item in sortedCharCount:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()