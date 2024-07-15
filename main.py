def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(f"The total amount of words in {book_path} is {word_count}.")
    print(f"Amount of letters: {letter_count}")


def get_letter_count(text):
    ltr_amt = {}
    lower_case = text.lower()

    for char in lower_case:
        if char.isalpha():
            if char not in ltr_amt:
                ltr_amt[char] = 1
            else:
                ltr_amt[char] += 1
    return ltr_amt


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
