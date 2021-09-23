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
# HTTP 규격에서, 헤더 전송 이후에는 반드시 줄바꿈을 하게 되어있으므로 마지막에 \r\n을 전송한다
# 마지막에 \r\n을 전송하지 않으면 브라우저 측에서 오류가 발생한다


from django.utils.simplejson import dumps, loads, JSONEncoder

def searchData(request):
    if 'searchwords' in request.POST:
        url = request.POST['searchwords']

    json = dumps(url, cls=DjangoJSONEncoder)
    return HttpResponse(json)