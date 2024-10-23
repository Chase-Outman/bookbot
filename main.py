def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_text(path_to_book)   
    num_words = count_words_in_text(book_text) 
    characters = count_characters_in_text(book_text)
    alpha_list = get_alpha_list(characters)

    print_report(num_words, characters, alpha_list)
    
    

def get_text(book):
    with open(book) as f:
        return f.read()

def count_words_in_text(book):
    words = book.split()
    return len(words)

def count_characters_in_text(book):    
    characters = {}

    for c in book:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1    

    return characters

def print_report(num_words, characters, alpha_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the text\n")

    for c in alpha_list:
        print(f"The '{c}' was found {characters[c]} times")

def get_alpha_list(characters):
    alpha_list = []
    for c in characters:
        if c.isalpha():
            alpha_list.append(c)
    alpha_list.sort()
    
    return alpha_list

main()

