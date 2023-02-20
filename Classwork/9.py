
words = ["language!", "programming", "Python", "the", "love", "I"]
str = ''
for x in reversed(words):
    str += x + " "

str = str.strip()

print(str)
print(str[len(str) - 1])
