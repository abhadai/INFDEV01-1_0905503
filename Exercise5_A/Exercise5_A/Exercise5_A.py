sentence = input("Type something. It will reverse your sentence")
output = ""

for s in reversed(sentence):
    output += s

print(output)