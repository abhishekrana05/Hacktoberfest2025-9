# ------------------------------------------------------------
# Vowel Counter
# Description:
#   Counts the total number of vowels (a, e, i, o, u)
#   in a given sentence, case-insensitive.
# Author: Abhishek Rana
# ------------------------------------------------------------

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Total vowels: {count_vowels(sentence)}")
