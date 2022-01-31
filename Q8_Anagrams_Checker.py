# Anagram Checker

def is_anagram():
    wrd1 = str(input("Enter the first word: "))
    wrd2 = str(input("Enter the second word: "))
    if sorted(wrd1.lower()) == sorted(wrd2.lower()):
        print("The words are anagrams of each other.")
    else:
        print("They are not anagrams.")

is_anagram()
