def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    split_w = split_the_words(text)
    word_c = get_word_count(split_w)
    let_ari = make_letter_dictionary(text)
    ar_list = make_list_of_aries(let_ari)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"Word count is {word_c}")
    print()
    
    for entry in ar_list:
        print(f"The '{entry['let']}' character was found {entry['num']} times.")
    
    print("--- End report ---")


def sort_on(j):
    return j["num"]


def make_list_of_aries(let_ari):
    sorted_aries_list = []
    for let in let_ari:
        sorted_aries_list.append({"let": let, "num": let_ari[let]})
    sorted_aries_list.sort(reverse=True, key=sort_on)
    return sorted_aries_list


def make_letter_dictionary(text):
    lower_letters = text.lower()
    letter_dictionary = {}
    for letter in lower_letters:
        if letter.isalpha():
            if letter not in letter_dictionary:
                letter_dictionary[letter] = 1
            elif letter in letter_dictionary:
                letter_dictionary[letter] += 1
    return letter_dictionary


def get_word_count(split_w):
    word_count = 0
    for word in split_w:
        word_count += 1
    return word_count


def split_the_words(text):
    indv_words = text.split()
    return indv_words


def get_text(path):
    with open(path) as f:
        return f.read()


main()
