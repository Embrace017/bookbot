from stats import word_count, char_count, sort_on, chars_to_sorted_list
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
    
    # Get word count and character counts
        word_count_result = word_count(book_text)
        char_counts = char_count(book_text)
    
    # Sort the character counts
        sorted_chars = chars_to_sorted_list(char_counts)
    
    # Print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count_result} total words")
        print("--------- Character Count -------")
    
    # Print each character and its count (only alphabetical characters)
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {count}")
    
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
