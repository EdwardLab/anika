from django.http import HttpResponse
from django.shortcuts import render
import os
import json
import random
import string
def anika(request):
    context          = {}
    hi = "Welcome to Anika"
    return render(request, 'index.html', {"hi":hi})

def anikaapi(request):
    r_num = 15
    randomname = ''.join(random.sample(string.digits + string.ascii_letters,r_num))
    if request.method=="GET":
        url = request.GET["url"]
        getytdlpjson = json.load(os.popen("yt-dlp " + url + " -j"))
        title = getytdlpjson['title']
        #--output "替换这里/%(title)s.%(ext)s" --no-mtime --merge-output-format mp4
        os.system(f'yt-dlp --output "/www/wwwroot/downloadfiles.anika.download/%({randomname})s.%(mp4)s" --no-mtime --merge-output-format mp4')
        geturl = f"http://downloadfiles.anika.download/{randomname}.mp4"
        data = [ { 'url' : geturl, 'title' : title,  } ]
        data2 = json.dumps(data)
    elif request.method=="POST":
        pass
    else:
        pass
    return HttpResponse(data2)
