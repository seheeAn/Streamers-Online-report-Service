#!E:\Anaconda3\envs\webenv\python.exe
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import json
import cgi
import cgitb

from pytchat import LiveChat
import pafy
import pandas as pd
import csv
import time

cgitb.enable()
fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d
result['data2'] = fs.getvalue('url_list')

sys.stdout.write("\n")


pafy.set_api_key('AIzaSyDvXnY4POjnMmzkOxDQ3yzC7fuyQXANU88')
# video_id = 'WkvQgfQxFQU' # Sarang Choi
url = result['data2'][-11:]
video_id = url # song

v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published
t = v.duration

#print(title)
#print(author)
#print(published)
#print(t)

# empty_frame = pd.DataFrame(columns=['댓글 작성자','댓글 작성 시간', '댓글 내용'])
# empty_frame.to_csv('./youtube.csv')

csvfile = open("data/youtube.csv", "w", encoding='UTF-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['댓글 작성자','영상 시간', '댓글 내용'])
csvwriter.writerow(['Lee', t , 'TEST'])
result["video_time"] = t
#all=time.time()
chat = LiveChat(video_id = video_id, topchat_only = 'FALSE')

while chat.is_alive():
    try:
        data = chat.get()
        items = data.items
        for c in items:
            #print(f"{c.elapsedTime} [{c.author.name}]- {c.message}")
            data.tick()
            # data2 = {'댓글 작성자' : [c.author.name], '댓글 작성 시간' : [c.datetime], '댓글 내용' : [c.message]}
            # result = pd.DataFrame(data2)
            # result.to_csv('youtube.csv', mode='a', header=False)
            csvfile = open("data/youtube.csv", "a", encoding='UTF-8')
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([c.author.name, c.elapsedTime, c.message])

    except KeyboardInterrupt:
        chat.terminate()
        break

        #분당 채팅 수 카운트 ans json 생성->
import json
from collections import OrderedDict

df = pd.read_csv("data/youtube.csv")
freq={}
a=df['영상 시간']
x=''
L=[]
for i in a:
  if i == a[0]:
        continue
  x=str(i)
  tmp = x.split(":")
  if len(tmp)==2:
    if '-' in tmp[0]:
        aa = '0:00'
    elif int(tmp[0]) >= 10:
        aa = '0:' + tmp[0]
    else:
        aa = '0:0'+tmp[0]
    L.append(str(aa))
  elif len(tmp)==3:
    if '-' in tmp[0]:
        aa = '0:00'
    elif '-' in tmp[1]:
        aa = '0:00'
    else:
        aa = tmp[0] + ':' + tmp[1]
    L.append(str(aa))

for t in L:
    cnt = freq.get(t, 0)
    freq[t] = cnt + 1

keys = list(freq.keys())
values = list(freq.values())

max = 0
for i in values:
    if i > max:
        max = i
max += max % 8
lay = max/8

file_data = OrderedDict()
file_data["time"] = keys
file_data["values"] = values

result["time"] = file_data["time"]
result["values"] = file_data["values"]
result["range"] = '0:'+str(max)+':'+str(lay)


with open('data/ForChart.json', 'w', encoding="UTF-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)

sys.stdout.write(json.dumps(result,indent=1))

#print("Total time : %f"%(time.time() - all))
