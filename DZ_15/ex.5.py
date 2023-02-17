f = open('data.txtex5', 'r')

words = 0

for word in f:
    words += len(word.split())

print("Words:", words)
