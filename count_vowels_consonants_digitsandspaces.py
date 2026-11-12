text = input("enter the string:")
vowel = 0
consonant = 0
digit = 0
spaces = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowel += 1
    elif ch.isalpha() :
         consonant += 1
    elif ch.isdigit() :
        digit += 1
    elif ch == " ":
         spaces += 1
print("vowel:",vowel)
print("cosonant:",consonant) 
print("digit:",digit)
print("spaces:",spaces)