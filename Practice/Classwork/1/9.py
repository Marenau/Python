
words = ["language!", "programming", "Python", "the", "love", "I"]
str = ''
for x in words[::-1]:
    str += x + " "

str = str.strip()

print(str)
print(str[len(str) - 1])
