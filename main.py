def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    counted_letters = count_each_letter(text)
    
    print_report(book_path, num_words, counted_letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_each_letter(text):
    lower_text = text.lower()
    letter_counts = {}
    for letter in lower_text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def print_report(path, num_words, counted_letters):

    
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document.")
    print("")
    for letter, count in dict(sorted(counted_letters.items())).items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

main()