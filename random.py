count = dict()
files = open('Python_prac')
for g in files:
    sent = g
    word = sent.split()
    for j in word:
        count[j] = count.get(j,0) + 1
print(count)
types = list()
for k,v in count.items():
    news = (v,k)
    types.append(news)
