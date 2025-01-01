def count_chars(text):
    letters = {}
    chars = list(text.lower())
    for char in chars:
        if not char.isalpha():
            continue
        try:
            letters[char] += 1
        except KeyError:
            letters[char] = 1
    return letters

def count_words(text):
    word_list = text.split()
    return len(word_list)

with open("frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words were found in the document\n")
    all_chars = count_chars(file_contents)
    for char in all_chars:
        print(f"The {char} character was found {all_chars[char]} times")
    print("--- End report ---")