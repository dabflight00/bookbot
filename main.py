from stats import character_times, word_count, sorted_list, format_list 

def main():
    book_path = "./books/frankenstein.txt"
    example = get_book_text(book_path)
    this = word_count(example)
    dict_unsorted = character_times(example)
    list_you_want = sorted_list(dict_unsorted)
    listed=format_list(list_you_want) 

    output = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {this} total words
--------- Character Count -------
{listed}
"""
    
    print(output)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

   

main()
