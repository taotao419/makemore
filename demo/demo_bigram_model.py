b = {}
words = open('../names.txt','r').read().splitlines()
for w in words:
    chs = ['<S>']+ list(w) + ['<E>']
    for ch1, ch2 in zip(chs,chs[1:]):
        bigram = (ch1,ch2) # 这一行把ch1, ch2 作为元组, 就是一个key
        b[bigram] = b.get(bigram,0) + 1 # 对应的这里的value, 是元组出现的次数
sorted_dict_desc = {k: v for k, v in sorted(b.items(), key=lambda item: item[1], reverse=True)}

print(sorted_dict_desc)