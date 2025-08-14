def count_words(book_text):
    split_text = book_text.split()
    count = 0
    for t in split_text:
        count += 1
    return count 

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

def sort_on(items):
    return items['num']

def generate_sorted_list(char_dictionary):
# {'char': key, 'count': value}
    list_to_sort = []
    for key, value in char_dictionary.items():
        if key.isalpha():
            list_to_sort.append({'char': key, 'num': value})
    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort


