#!E:\Anaconda3\envs\webenv\python.exe
# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
######### 2~5번행 까지는 브라우저에서 한글을 표기하기 위한 코드##########
import cgi
import cgitb

cgitb.enable()
# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로, cgitb.enable()
# 할 경우 런타임 에러를 웹브라우저로 전송한다
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우
# 웹서버는 클라이언트에게 HTTP 응답코드 500을 전송한다
print("Content-type: text/html;charset=utf-8\r\n")

from pytchat import LiveChat
import pafy
#import pandas as pd
import csv

#####################DEFAULT VARIABLE########################
youtube_api_key = "AIzaSyDp1ty7eikSivn-Ktv7fIhvWtlvlH9H2m4"
video_id = 'iYpljxNmZB0'
csv_file_name = "./data/youtube.csv"
encoding_status = True      #Encoding 여부
#############################################################

#####################DEFAULT FUNCTION#######################

############################################################

pafy.set_api_key(youtube_api_key)

video = pafy.new(video_id)
video_title = video.title
video_author = video.author
video_published = video.published

print(video_title)
print(video_author)
print(video_published)

# empty_frame = pd.DataFrame(columns=['댓글 작성자','댓글 작성 시간', '댓글 내용'])
# empty_frame.to_csv('./youtube.csv')

if (encoding_status):
    csv_file = open(csv_file_name, 'w', encoding='UTF-8')
else:
    csv_file = open(csv_file_name, 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['댓글 작성자', '댓글 작성 시간', '댓글 내용'])
csv_file.close()

chat = LiveChat(video_id = video_id, topchat_only = 'FALSE')
while chat.is_alive():
    try:
        data = chat.get()
        items = data.items
        for c in items:
            print(f"{c.datetime} [{c.author.name}]- {c.message}" + "check")
            data.tick()
            # data2 = {'댓글 작성자' : [c.author.name], '댓글 작성 시간' : [c.datetime], '댓글 내용' : [c.message]}
            # result = pd.DataFrame(data2)
            # result.to_csv('youtube.csv', mode='a', header=False)
            if (encoding_status):
                csv_file = open(csv_file_name, "a", encoding='UTF-8')
            else:
                csv_file = open(csv_file_name, "a")
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([c.author.name, c.datetime, c.message])

    except KeyboardInterrupt:
        print("댓글 추출을 중지합니다.")
        chat.terminate()
        csv_file.close()
        break