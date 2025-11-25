def get_word_count(text: str):
    words = text.split()
    return len(words)


def get_character_count(text: str):
    char_dict = {}
    for letter in text:
        lowercase = letter.lower()
        if lowercase not in char_dict:
            char_dict[lowercase] = 1
            continue
        char_dict[lowercase] += 1
    return char_dict


def sort_on(items):
    return items["count"]


def clean_output(full_char_dict):
    sorted_list = []
    for entry in full_char_dict:
        if entry.isalpha():
            sorted_list.append({"char": entry, "count": full_char_dict[entry]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
