def word_count(contents):
    words = contents.split()
    return len(words)

def character_times(contents):
    chars = {}
    for i in contents:
        lowered = i.lower()
        if lowered in chars: 
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def helper_sort(listed_items):
    return listed_items["num"]

def sorted_list(unsorted_dict):
    the_list = []
    for i in unsorted_dict:
        smol_dict = {"char": i, "num": unsorted_dict[i]}
        the_list.append(smol_dict)
        the_list.sort(reverse=True, key=helper_sort) 
    return the_list
        
def format_list(sorted_list):
    result = [] 
    for i in sorted_list:
        if i["char"].isalpha():
            result.append(f"{i["char"]}: {i["num"]}")
    return "\n".join(result)

