def lines(line):
  part = line.upper()
  print(part)
print("New function!")
news = input('Enter a string, please')
doing = lines(news)
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
port = ['fdj', 'red', 'dsje']
port.sort()
print(port)
