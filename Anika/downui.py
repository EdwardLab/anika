import pywebio.input
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
import sys
import subprocess
import os
import random
import string
import json
getdownurl = sys.argv[1]
getport = sys.argv[2]
r_num = 15
#randomport = random.randint(10000,50000)
print("http://download.anika.download:" + str(getport))
def get_result(cmd):
        popen = subprocess.Popen(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 text=True)
        while True:
            buff = popen.stdout.readline()
            if buff:
                put_text(buff)
            elif popen.poll() is not None:
                break
def main():
    set_env(title="preparing...", auto_scroll_bottom=True)
    put_html("<h1>Anika Video Downloader Panel</h1>")
    randomname = ''.join(random.sample(string.digits + string.ascii_letters,r_num))
    put_markdown(f"""


User Name: `Free_User`
Panel Expiration Time: `use once`
Panel Custom Port Number (Premium only):`{getport}`
Panel type: `One-time generation`
_________________________________________________
Panel info(one-off version):
Download URL:`{getdownurl}`
For external network resources and websites with slow downloads, we recommend that you use Download Video to download from our server and then transfer them to your computer. For websites with very fast local speeds, we recommend that you get the second Get Video Download url to get the Paste the URL into the browser to download, so that the download speed will be faster through the source link.
_________________________________________________

    """)
    options = pywebio.input.select("Download the video or get the download address of the video", ["Download Video", "Get Video Download url", "Get video full info json"])
    if options == 'Download Video':
        set_env(title="preparing...", auto_scroll_bottom=True)
        put_html("<h3>正在高速获取资源，请稍后...</h3>")
        put_loading(shape='border', color='primary')
        try:
            #get_result("you-get -o tempvideos --format=mp4 --no-caption " + getdownurl
            get_result(f"you-get -i {getdownurl}")
        except:
            put_error("Can't run shell, Please ask server admin or report this bug to Anika Telegram Group")
        format = pywebio.input.input("请输入下载画质和格式的format或者itag标签，我们提供多个格式，请选择后输入（上方列表中的format或itag，例如您应该输入 format dash-flv 或者 itag 18）：")
        container = pywebio.input.input("请输入对应上方格式container的内容来指定格式（例如mp4或flv或webm等，只能输入上个输入框输入的format或itag对应的格式，否则无法下载：")
        put_warning("资源获取正在继续，请勿关闭或退出，稍后即可看到下载进度...")
        get_result(f"you-get -o /www/wwwroot/downloadfiles.anika.download -O {randomname} --{format} {getdownurl}")
        put_success("云端下载完毕！请不要离开页面，我们正在云端解析视频信息...")
            #getjson = json.loads(os.popen("you-get " + getdownurl + " --json").read())
            #videoname = getjson['title'] + "." + container
        videoname = randomname + "." + container
        #os.rename(videoname, randomname)
        #get_result(f"ffmpeg -i {tempname} -c copy -map 0 {randomname}.mp4")
        put_html(f'<meta http-equiv="refresh" content="0;url= http://downloadfiles.anika.download/{videoname}">')
        put_success("一切就绪！正在下载到本机...")

    if options == 'Get Video Download url':
        put_loading(shape='border', color='primary')
        get_result("you-get --url " + getdownurl)
        put_text("You can copy Real URLs to browser and download it more fast")
        sys.exit()
    if options == 'Get video full info json':
        put_loading(shape='border', color='primary')
        get_result("you-get " + getdownurl + " --json")
        sys.exit()
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=getport)
    pywebio.session.hold()