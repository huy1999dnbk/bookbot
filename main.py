def count_word(string):
    return len(string.split())

def count_letters(string):
    set_words = {}
    for item in list(string):
        item = item.lower()
        if item in set_words:
            set_words[item]+=1
        else:
            set_words[item] = 1
    return set_words

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    count_words = count_word(file_content)
    count_letter = count_letters(file_content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in the document")
    print("")
    print("")
    res = []
    for item in count_letter:
        if item.isalpha():
            res.append({
                'letter': item,
                'c': count_letter[item]
            })
    res.sort(key=lambda x: x['c'], reverse=True)
    for item in res:
        letter = item['letter']
        count = item['c']
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")