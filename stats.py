def count_words(book_text):
    split_text = book_text.split()
    count = 0
    for t in split_text:
        count += 1
    return print (f"{count} words found in the document")

def count_characters(book_text):
    split_text = book_text.split()
    char_dict = {}
    for word in split_text:
        for char in word:
            lower_char = char.lower()
            if lower_char in char_dict: 
                char_dict[lower_char] += 1
            else: 
                char_dict[lower_char] = 1
    return char_dict



        
                

