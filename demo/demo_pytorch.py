import torch
import matplotlib.pyplot as plt

N = torch.zeros((28,28),dtype=torch.int32)
words = open('../names.txt','r').read().splitlines()
chars = sorted(list(set(''.join(words)))) # a~z 26个字符
stoi = { s:i for i,s in enumerate(chars)} # string to index , 每个字符有一个对应的索引整数.
stoi['<S>'] = 26 # 给特殊的起始符 给一个索引整数 26
stoi['<E>'] = 27

itos = { i:s for s,i in stoi.items()}

for w in words:
    chs = ['<S>']+ list(w) + ['<E>']
    for ch1, ch2 in zip(chs,chs[1:]):
        ix1 = stoi[ch1] # 字符1 对应的索引整数
        ix2 = stoi[ch2] # 字符2 对应的索引整数 
        N[ix1,ix2] += 1 # 统计出 这个二维数组的任意两个字符出现次数
        
plt.figure(figsize=(16,16))
plt.imshow(N,cmap="Blues")
for i in range(28):
    for j in range(28):
        chstr = itos[i]+itos[j]
        plt.text(j,i,chstr,ha="center",va="bottom", color='gray')
        plt.text(j,i,N[i,j].item(),ha="center",va="top", color='gray')
plt.axis('off')        
plt.savefig('matpltlib.png')