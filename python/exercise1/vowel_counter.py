#!/usr/bin/env python3

def num_vowels(text):
    """Return the number of vowels in string."""
    vowels = "aeiou"
    return sum(text.lower().count(v) for v in vowels)

def num_consonants(text):
    """Return the number of consonants in the string (excluding spaces and punctuation)."""
    vowels = "aeiou"
    return sum(1 for letter in text.lower() if letter.isalpha() and letter not in vowels)
    
# Get user input
text = str(input("Enter a sentence: "))

#print results
print("Number of vowels", num_vowels(text))
print("Number of consonants", num_consonants(text))


