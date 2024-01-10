vowels = ["a","e","i","o","u","õ","ä","ö","ü"] 
sentence = input("Kirjuta midagi: ")

count = 0

for letter in sentence:
    if letter.lower() in vowels:
        count += 1
        print(count)