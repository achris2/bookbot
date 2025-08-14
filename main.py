from stats import count_words, count_characters
from stats import generate_sorted_list
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents  

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    elif sys.argv[1]: 
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = count_words(book_text)
        char_dictionary = count_characters(book_text)
        sorted_list_dicts=generate_sorted_list(char_dictionary)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_list_dicts:
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    
main()