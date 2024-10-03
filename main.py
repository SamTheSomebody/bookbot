def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_dictionary(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def get_char_apperances(text):
    lowered_text = text.lower()
    char_dict = {}
    for c in lowered_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for e in char_dict:
        sorted_list.append({"char": e, "num": char_dict[e]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_dictionary(book_path, text):
    word_count = get_num_words(text)
    char_dict = get_char_apperances(text)
    char_sorted_list = char_dict_to_sorted_list(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for e in char_sorted_list:
        if not e["char"].isalpha():
            continue
        print(f"The '{e['char']}' character was found {e['num']} times.")
    print("--- End report ---")


main()
