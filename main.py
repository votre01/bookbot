def main():
    book_path = "books/frankenstein.txt"    
    text = read_file(book_path)
    d = sort_dict(count_chars(text))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    for key in d:
        if key.isalpha():
            print(f"The '{key}' character was found {d[key]} times")
    print("--- End report ---")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if chars.get(char) == None:
            chars[char] = 1
        else:
            chars[char] += 1 
    return chars

def sort_dict(d):
    return dict(
        sorted(d.items(),
        key=lambda item: item[1],
        reverse=True))


  

main()