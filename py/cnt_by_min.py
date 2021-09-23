import pandas as pd

df = pd.read_csv("youtube.csv")
freq={}
a=df['영상 시간']

L=[]
for i in a:
  tmp = i.split(":")
  if len(tmp)==2:
    L.append(tmp[0])
  elif len(tmp)==3:
    aa=int(tmp[1])+60
    L.append(str(aa))

for t in L:
    cnt = freq.get(t, 0)
    freq[t] = cnt + 1

keys = list(freq.keys())
values = list(freq.values())
print(freq)

file_data = OrderedDict()
