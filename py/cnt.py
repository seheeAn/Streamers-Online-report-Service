import pandas as pd

df = pd.read_csv("youtube.csv")
freq={}
a=df['영상 시간']
for t in a:
    cnt = freq.get(t, 0)
    freq[t] = cnt + 1

keys = list(freq.keys())
values = list(freq.values())
print(freq)