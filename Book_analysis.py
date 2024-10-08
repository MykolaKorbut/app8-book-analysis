import re

# # Load the book
with open("miracle_in_the_andes.txt", 'r') as file:
    book = file.read()

# Counting with string methods (wrong amount because the method count all
# words "chapter", including words that are contained in the text)
print("Wrong amount of chapters is", book.count("Chapter"))

# Counting with regex (right method)
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)
print("Amount of chapters is", len(findings))

# Which are the sentences where "love" was used?
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)
#print(findings)

# # What are the most used words?
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
print("10 most used words (quantity, word): ", d_list[0:10])
