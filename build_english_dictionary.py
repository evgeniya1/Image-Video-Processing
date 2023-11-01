import json

file = open('data.json')

data = json.load(file)

# print(type(data))
# print(data['island'])

def define(word):
    word = word.lower()
    if word in data:
        return data[word]

word = input("Please enter a word:\n")
definition = define(word)

if definition:
    for item in definition:
        print(item)
else:
    print(f"Word {word} was not found")