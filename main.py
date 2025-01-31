def sort_on(dict):
    return dict["count"]
def main():
    charcount = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    lowercase = file_contents.lower()
    for char in lowercase:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
    char_list = []
    for char , count in charcount.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")

    





    

main()
