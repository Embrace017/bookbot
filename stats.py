def word_count(text):
    word_list = text.split()
    count = len(word_list)
    return count

def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            
    return char_dict

def sort_on(char_dict):
    # This returns the value to sort by
    return char_dict["count"]  # Note: we're using "count" based on your assignment

def chars_to_sorted_list(char_dict):
    chars_list = []
    for char in char_dict:
        # Create a dictionary with 'char' and 'count' keys
        char_info = {"char": char, "count": char_dict[char]}
        chars_list.append(char_info)
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list