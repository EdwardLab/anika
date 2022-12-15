# -- coding: utf-8 --**
from django.http import HttpResponse
from django.shortcuts import render
import os
import json
import subprocess
import random
# 表单
def search_form(request):
    return render(request, 'download.html')
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'download' in request.GET and request.GET['download']:
        randomport = random.randint(10000,50000)
        message = 'If the independent download link has been opened, the browser will automatically jump. If there is no jump, please manually visit:http://download.anika.download:' + str(randomport)
        autojump = '<meta http-equiv="refresh" content="2;url= http://serverdefault.anika.download:' + str(randomport) + ' ">'
        #os.system("you-get" + request.GET['download'] + " --json")
        
        #geturl = json.loads(os.popen("you-get " + request.GET['download'] + " --json").read())
        #print(geturl['src'])
        #from you_get import common
        downui = os.system("python3 Anika/downui.py " + request.GET['download'] + " " + str(randomport) + " 2>&1 &")
        #down = common.any_download(url=request.GET['download'],info_only=False,output_dir=r'tempvideos',merge=True)
        #os备用调用方案
        #geturl = os.popen("you-get -o tempvideos " + request.GET['download']).read()
        #result = json.loads(getjson)
        #videourl = result['streams']
        #jsformat = json.dumps(videourl, sort_keys=True, indent=4, separators=(',', ':'))
    else:
        message = 'Please enter the download link'
    return HttpResponse([message, autojump])