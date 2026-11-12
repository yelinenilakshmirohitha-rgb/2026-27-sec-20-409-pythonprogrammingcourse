str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")