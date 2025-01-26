import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the document")
    sorted_letter_count = sorted_dict(file_contents)  # Użycie posortowanej funkcji
    print_letter_counts(sorted_letter_count)


def count_words(file):
    return len(file.split())

def letter_count(file):
    letter_dict = {}   # Dictionary to count letters
    list_dict = []     # List to store individual letter count dictionaries
    text = file.lower()  # Convert text to lowercase for case-insensitive counting
    
    for letter in text:
        # Only process alphabetic characters
        if letter in string.ascii_lowercase:
            if letter not in letter_dict:
                letter_dict[letter] = 0
            letter_dict[letter] += 1
    
    # After counting, create a list of dictionaries for unique letters
    for letter, count in letter_dict.items():
        list_dict.append({letter: count})
    
    return list_dict

def sorted_dict(text):
    # Uzyskaj listę słowników z funkcji letter_count
    letter_list = letter_count(text)
    
    # Sortuj listę w miejscu za pomocą funkcji `get_value`
    letter_list.sort(key=get_value, reverse=True)  # Sortowanie w miejscu za pomocą sort()
    
    # Zwróć posortowaną listę
    return letter_list

def get_value(dictionary):
    # Pobiera pierwszą (i jedyną) wartość ze słownika
    return list(dictionary.values())[0]

def print_letter_counts(sorted_list):
    # Wyświetl wynik w pożądanym formacie
    for letter_dict in sorted_list:
        for letter, count in letter_dict.items():
            print(f"The '{letter}' character was found {count} times")

main()