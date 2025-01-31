def main():
    charcount = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(count)
    lowercase = file_contents.lower()
    for char in lowercase:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
    print(charcount)





    

main()
