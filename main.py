def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = count_char(text)
    sorted_list = turn_dict_into_sorted_list(chars)

    print(f"{num_words} words were found in {book_path}")
    for item in sorted_list: 
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print ("----End Report----")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]

def turn_dict_into_sorted_list(dict):
    sorted_list = []
    for item in dict:
        sorted_list.append({"char": item, "num": dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars: 
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
 
main()