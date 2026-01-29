ch = input("Enter a character: ")

if ch.isalpha():
    if ch in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Symbol")
