
words = open('../names.txt','r').read().splitlines()
print(words[:10]) # top 10 words
print(len(words)) # whole words length
print(max(len(w) for w in words)) # the max/ min of word in the words