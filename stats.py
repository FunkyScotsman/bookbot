def get_num_words(txt):
    words = txt.split()
    return len(words)

def get_num_letters(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_char_count(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list
    