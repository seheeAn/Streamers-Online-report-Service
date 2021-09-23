#!E:\Anaconda3\envs\webenv\python.exe

import sys
import json
import cgi
import cgitb

cgitb.enable()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"


import pandas as pd

wt = {}
nt = {}
wt = pd.read_csv("data/youtube.csv").iloc[0]['영상 시간']
nt = pd.read_csv("data/youtube.csv").iloc[-1]['영상 시간']
result['data'] = wt
result['data2'] = '00:'+nt #채팅 기록이 시간까지 표기되도록 요청

video = result['data'].split(':')
last = result['data2'].split(':')
if len(last)==4:
    h = int(last[1])
    m = int(last[2])
    s = int(last[3])
else:
    h = int(last[0])
    m = int(last[1])
    s = int(last[2])

if '-' in last[0]:
    m = 0 - int(last[1])
    s = 0 - int(last[2])

if '-' in last[1]:
    s = 0 - int(last[2])


video_s = int(video[0])*3600 + int(video[1])*60 + int(video[2])
last_s = h*3600 + m*60 + s

percent = (last_s/video_s)*100
progress = round(percent,0)

if progress < 0:
    progress = 0
result['progress'] = progress


sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
