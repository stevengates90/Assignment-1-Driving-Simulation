import re

Words = input("Enter the word:")

c = re.findall("[A-Z]",Words)
print(c)

c = Words.isupper
print(len(c))
