def get_num_words(text):
    """
    Returns the number of words in the given text.
    """
    return len(text.split())

def get_num_character(text):
    """
    Returns the frequency of each character in the given text.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def sort_dict_by_value(dict):
    """
    Makes a set and sorts the dictionaries inside by its values in descending order.
    """
    items = [
        {"char": char, "num": count}
        for char, count in dict.items()
        if char.isalpha()
    ]
    items.sort(key=lambda x: x["num"], reverse=True)
    return items