
words = ["language!", "programming", "Python", "the", "love", "I"]
str = ''
for x in reversed(words):
    str += x + ' '

print(str.strip())