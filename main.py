from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents  

def main():
    frank_text = get_book_text("books/frankenstein.txt")
    count_words(frank_text)
    result = count_characters(frank_text)
    print(result)
    
main()