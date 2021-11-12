sentance="Arjun went to shop to bought a new pen and also bought new pencil"

wordList=sentance.split() # split the sentance in to word list
counts = {} #it keeps unique word set
for word in wordList:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1 #if the word is exist in the count set incrementing by 1
print(counts)
