def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    chars = text.lower()
    characters = {}

    for char in chars:
        characters[char] = characters.get(char,0) + 1
    
    return characters

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    newlist = []

    for k,v in dict.items():
        newlist.append({"char": k, "num" : v})
    #print("first time", newlist)
    newlist.sort(reverse=True, key=sort_on)
    return newlist
