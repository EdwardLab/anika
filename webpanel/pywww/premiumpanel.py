# coding=utf-8
# -*- coding: utf-8 -*-
from sysconfig import get_path_names
import pywebio.input
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
from pywebio.pin import *
import pywebio.platform
import subprocess
import os
import random
import json
import time
import datetime
import string
import requests
import datetime
import math
from python_authentiator import TOTP
big = math.inf
appname = 'Anika'
#randomport = random.randint(10000,50000)
r_num = 15
config(title=f"{appname} Premium")
def googleauth(lsecret, llabel, laccount):
    g_auth = TOTP(
        origin_secret=lsecret,
        label=llabel,
        account=laccount
    )

    # 生成密钥
    gsecret = g_auth.generate_secret()
    # 生成一次性密码
    gpassword = g_auth.generate_code(gsecret)
    # 生成二维码
    qrcode = g_auth.generate_qrcode(gsecret)
    return(gsecret,gpassword,qrcode)
#gsecret,gpassword,qrcode = googleauth()
def head():
        put_html(f"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>
  <body>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
<!-- Image and text -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <img src="https://www.anika.download/wp-content/uploads/2022/07/Anika.ico" width="30" height="30" class="d-inline-block align-top" alt="">
    Anika Premium Panel
  </a>
</nav>
<div class="jumbotron">
  <h1 class="display-3">欢迎使用{appname} Premium面板！</h1>
  <p class="lead">在这里享受高速，便捷的下载体验</p>
  <hr class="my-4">
  <p>随时下载您的视频，只需要一个账户！</p>
  </p>
</div>  
  </body>
</html>
    """)
class GetError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
def sendsms(mobile, content):
    requests.get(f"http://bidao123.com/sms.aspx/?action=send&userid=4621&account=xingyujie&password=2294001xyj&mobile={mobile}&content={content}&sendTime=&extno=")
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
def loginerror():
    try:
        raise GetError("Disconnect from server")
    except:
        put_error("用户名或密码或Google Authenticator（仅设定）错误！三秒跳转主页，请重试！")
        time.sleep(3)
        put_link("重试", './premiumpanel')   
        go_app('#', new_window=False)
        time.sleep(big)
def login():
    global getdownurl
    global username
    global password
    global randomname
    global ostime
    #put_success("欢迎使用Anika Premium面板！需要帮助？客服Telegram:@xingyujie")
    with use_scope('loginwelcome'):  # 创建并进入scope 'scope1'
        put_markdown(f"## 登录到{appname} Premium")
        put_info(f"欢迎使用{appname} Premium面板！登录遇到问题？需要帮助？请联系客服Telegram:@xingyujie")
    userinput = input_group("登录到Premium Panel",[
    pywebio.input.input('请输入您的用户名：', name='username'),
    pywebio.input.input('请输入您的密码：', name='password', type=PASSWORD)
])   
    username = userinput['username']
    password = userinput['password']
    #put_html("<h1>Anika Video Downloader Panel</h1>")
    randomname = ''.join(random.sample(string.digits + string.ascii_letters,r_num))
        #username = pywebio.input.input("请输入您的用户名：",required=True,help_text='请输入您设置的用户名')
    try:
        open('panel/' + username + '/username.txt')
    except:
        loginerror()
    try:
        getpassword = open('panel/' + username + '/userpassword.txt')
    except:
        pass
    #password = pywebio.input.input("请输入您的密码：",required=True,help_text='请输入您设置的密码')
    try:
        if password != getpassword.read():
            loginerror()
        else:
            pass
    except:
        pass
    userdir = 'panel/' + username
    f = open(userdir + '/settings/gauth.txt', 'r')
    if f.read() == "enable":
        with use_scope('glogin'):
            put_text("需要二次验证！")
        gsecret,gpassword,qrcode = googleauth(username, 'Anika Premium: ' + username, username + '@anikapremium')
        gcode = pywebio.input.input("请输入谷歌验证器的验证码：")
        if gcode != gpassword:
            put_text("验证码不正确！")
            loginerror()
        output.clear('glogin')
    output.clear('loginwelcome')
    pywebio.output.scroll_to('middle')
    with use_scope('loading'):
        put_markdown("# Loading Panel...")
        put_processbar('bar');
        for i in range(1, 11):
            set_processbar('bar', i / 10)
            time.sleep(0.1)
    output.clear('loading')
    #addusertime = os.path.getctime('panel/' + username)
    ISOTIMEFORMAT = '%Y%m%d'
    ostime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    f = open('panel/' + username + '/regtime.txt','r',encoding='UTF-8')
    if ostime > f.read():
        put_warning(f"此用户已过期，请立即续费，续费在面板的用户设置中。若下次登录前未续费，下次登录后将会注销此用户。")
        os.system('rm -rf panel/' + username)
def downurl():
    global getdownurl
    with use_scope('downinfo'):  # 创建并进入scope 'scope1'
        put_success("请输入您要下载URL吧")
    getdownurl = pywebio.input.input("请输入下载资源链接：",required=True)
    output.clear('downinfo')
def viewtimeout():
    userdir = 'panel/' + username
    f = open(userdir + '/settings/viewtimeout.txt', 'w')
    settime = pywebio.input.input("请输入更改后的超时时间（秒）：")
    f.write(settime)
    toast("设置成功！")
    output.clear('settings')
def gauth_enable():
    gsecret,gpassword,qrcode = googleauth(username, 'Anika Premium: ' + username, username + '@anikapremium')
    userdir = 'panel/' + username
    f = open(userdir + '/settings/gauth.txt', 'w')
    f.write("enable")
    put_text(f"Google Auth Secret是：{gsecret}，请妥善保管此密钥，丢失将无法登录账户！")
def gauth():
    gsecret,gpassword,qrcode = googleauth(username, 'Anika Premium: ' + username, username + '@anikapremium')
    popup('您确认要开启Google authenticator吗？', [
    put_html('<h3>您必须知道这是什么再开启！否则您将会无法登录！</h3>'),
    put_buttons(['我已了解风险，自愿开启！'], onclick=lambda _: [gauth_enable(), close_popup()])
])
    
    put_html(f'<a href="{qrcode}"  target="_blank">请通过Play Store,App Store等下载Google authenticator应用程序，并点击我扫描二维码绑定</a>')
def gauthclose():
    userdir = 'panel/' + username
    f = open(userdir + '/settings/gauth.txt', 'w')
    f.write("disable")
    toast("已取消！")
def settings():
    with use_scope('settings'):
        put_markdown("## 用户设置")
        put_button("设置获取链接的超时时间（默认40秒）", onclick=lambda: viewtimeout(), color='success', outline=True)
        put_button("更改账户密码", onclick=lambda: changepassword(), color='success', outline=True)
        put_button("通过密钥续费时长", onclick=lambda: updatetime(), color='success', outline=True)
        put_button("绑定Google authenticator，让账户更安全（登录时需要动态令牌验证）", onclick=lambda: gauth(), color='success', outline=True)
        put_button("取消绑定Google authenticator", onclick=lambda: gauthclose(), color='success', outline=True)
        put_button("返回下载视频", onclick=lambda: downui(), color='success', outline=True)
def updatetime():
    f = open("key.txt")
    read = f.read()
    put_info(f"密钥为Active {appname}密钥，与注册新用户是一个密钥，续费后从激活当天开始算往后推30天，购买密钥请前往http://activeanika.xingyujie.xyz/")
    key = pywebio.input.textarea("在此处粘贴您的激活密钥:", minlength=25, required=True)
    if key == 'admin_withoutkey_verification':
        admincode = random.randint(1000000, 9999999)
        sendsms(18990149475, f"【Anika会员】您好本次操作需要验证，您的验证码是{admincode}，请勿泄漏给他人。")
        verifyadmin = pywebio.input.input("人工授权激活，请输入临时验证令牌以验证您的身份：")
        if verifyadmin == str(admincode):
            userpath = 'panel/' + username
            getregtime = datetime.datetime.now() + datetime.timedelta(days=30)
            lastgetregtime = getregtime.strftime("%Y%m%d")
            f = open(userpath + '/regtime.txt', "w")
            f.write(lastgetregtime)
            userdir = 'panel/' + username
            phonenum = open(userdir + '/phonenum.txt', 'r')
            for i in range(10):
                put_success("人工授权续费成功！")
            toast("续费成功！")
        else:
            put_error("授权失败！")
    if key in read:
        put_text(f"感谢您购买{appname} Premium！")
        #username = pywebio.input.input("为您的独立控制面板创建用户名：",required=True)
        #password = pywebio.input.input("为您的独立控制面板创建密钥：",required=True)
        put_info("我们正在为您续费...")
        lineList = []
        file = open('key.txt','r',encoding='UTF-8')  
        while 1:
            line = file.readline()
            if not line:        
                print("Read file End or Error")        
                break
            line2 = line.replace(key,'')
            lineList.append(line2)
            
        file.close()
        file = open(r'key.txt', 'w',encoding='UTF-8')
        for i in lineList:
            file.write(i)
        file.close()
        #runcmd = os.system("python3 premiumpanel.py " + str(randomport) + ' ' + password + " 2>&1 &")
        try:
            os.makedirs('panel/' + username)
        except:
            pass
        userpath = 'panel/' + username
        getregtime = datetime.datetime.now() + datetime.timedelta(days=30)
        lastgetregtime = getregtime.strftime("%Y%m%d")
        f = open(userpath + '/regtime.txt', "w")
        f.write(lastgetregtime)
        userdir = 'panel/' + username
        phonenum = open(userdir + '/phonenum.txt', 'r')
        sendsms(phonenum.read(), "【Anika会员】您好，您的面板续费成功！请登入面板查看")
        try:
            os.mkdir(userpath + '/settings')
            userdir = 'panel/' + username
            viewtimeoutwrite = open(userdir + '/settings/viewtimeout.txt', 'w')
            viewtimeoutwrite.write("40")
        except:
            pass
        put_success("续费成功！")
        toast("续费成功！")
    else:
        put_error("错误的密钥，请检查...")
def changepassword():
    check_code = random.randint(100000, 999999)
    userdir = 'panel/' + username
    f = open(userdir + '/phonenum.txt', 'r')
    checkphone = pywebio.input.input("验证您的手机号码，请输入注册用户时绑定的手机号码：")
    if checkphone == f.read():
        sendsms(checkphone, f"【Anika会员】您好本次操作需要验证，您的验证码是{check_code}，请勿泄漏给他人。")
        inputcode = pywebio.input.input(f"验证码已发送到：{checkphone}，请输入验证码：")
        if inputcode != str(check_code):
            toast("短信验证码不正确！请重试！（如果无法通过短信验证码验证，请联系客服）再次获取验证码请刷新页面，在此刷新页面您的激活码不会失效")
        setnewpassword = pywebio.input.input("设置您的新密码：")
        newpasswordcheck = pywebio.input.input("请再次输入确认您的新密码：")
        if setnewpassword == newpasswordcheck:
            f = open(userdir + '/userpassword.txt', 'w')
            f.write(setnewpassword)
            toast("密码更改成功！")
        else:
            put_error("两次密码输入不一致！请检查！")
    else:
        put_error("手机号码不正确，请重新输入！")
    output.clear('settings')
def downui():
    head()
    put_button("用户设置", onclick=lambda: settings(), color='success', outline=True)
    downurl()
    userdir = 'panel/' + username
    viewtimeout = open(userdir + '/settings/viewtimeout.txt', 'r')
    put_markdown(f"""

欢迎使用 {appname} Premium Panel!
用户名: `{username}`
面板到期时间: `理论共计30天`，面板开通/上次续费时间`{ostime}`
面板类型: `Premuim Panel`
_________________________________________________
下载链接:`{getdownurl}`
_________________________________________________
续费请直接再次购买激活码，并进入激活页面激活，激活时输入您的用户名`{username}`并设置相同的密码即可续费。

* 第一项是直接下载视频
* 第二项是获取视频源链接（部分网站音频与图像是分开的）
* 第三项是获取视频的JSON解析数据
* 第四项是通过yt-dlp内核下载视频（未完善，bug多，不建议使用）
* 第五项是通过yt-dlp内核解析JSON数据
(第一二三项是you-get内核)
    """)
    put_button("点此重新输入视频链接（下载其他链接的视频）", onclick=lambda: downui(), color='success', outline=True)
    options = pywebio.input.select("选择视频的下载方式", ["Download Video", "Get Video Download url", "Get video full info json", "Download videos via yt-dlp", 'Get video json via yt-dlp'])
    if options == 'Download Video':
        set_env(title="preparing...", auto_scroll_bottom=True)
        put_html("<h3>正在高速获取资源，请稍后...</h3>")
        put_loading(shape='border', color='primary')
        try:
            #get_result("you-get -o tempvideos --format=mp4 --no-caption " + getdownurl
            get_result(f"you-get -i {getdownurl}")
        except:
            put_error(f"Can't run shell, Please ask server admin or report this bug to {appname} Telegram Group")
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
        time.sleep(5)
        downui()
    if options == 'Get Video Download url':
        put_loading(shape='border', color='primary')
        get_result("you-get --url " + getdownurl)
        put_text("您可以粘贴Real URLs 到浏览器中直链下载，这样下载会更快哦(Real URLs部分网站的音频和图像是分开的，一个链接是音频，一个链接是图像，下载后可以通过软件合成完整的视频！")
        put_info(f'此页面系统将会显示{str(viewtimeout.read())}S，到时自动返回主页，可在"用户设置"中设置超时时间')
        viewtimeout.seek(0,0)
        time.sleep(int(viewtimeout.read()))
        viewtimeout.seek(0,0)
        downui()
    if options == 'Get video full info json':
        put_loading(shape='border', color='primary')
        get_result("you-get " + getdownurl + " --json")
        put_info(f'此页面系统将会显示{str(viewtimeout.read())}S，到时自动返回主页，可在"用户设置"中设置超时时间')
        viewtimeout.seek(0,0)
        time.sleep(int(viewtimeout.read()))
        viewtimeout.seek(0,0)
        downui()
    if options == 'Download videos via yt-dlp':
        set_env(title="preparing...", auto_scroll_bottom=True)
        put_html("<h3>正在通过yt-dlp高速获取资源，请稍后...</h3>")
        put_loading(shape='border', color='primary')
        try:
            readytdlp = get_result("yt-dlp -P tempvideos --merge-output-format mp4 --no-mtime " + getdownurl)
        except:
            put_error(f"Can't download, Please ask server admin or report this bug to {appname} Telegram Group")
        put_text(readytdlp)
        getytdlpjson = json.load(os.popen("yt-dlp " + getdownurl + " -j"))
        ytdlptitle = getytdlpjson['title']
        ytdlptype = '.mp4'
        try:
            os.system("cp tempvideos/" + ytdlptitle + ytdlptype + " /www/wwwroot/downloadfiles.anika.download")
        except:
            put_error(f"Can't copy files, Please ask server admin or report this bug to {appname} Telegram Group")
        #getytdlpjson = str(json.loads(readytdlp))
        #ytdlpvideoname = getytdlpjson['title']
        put_text("Cloud download complete! Preparing for high-speed download to local, please wait...")
        put_success("Cloud download complete! Preparing for high-speed download to local, please wait...")
        put_html('<meta http-equiv="refresh" content="0;url= http://downloadfiles.anika.download/' + ytdlptitle + ytdlptype + ' ">')
        put_success("start download..")
        time.sleep(5)
        downui()
    if options == 'Get video json via yt-dlp':
        set_env(title="preparing...", auto_scroll_bottom=True)
        put_html("<h3>通过yt-dlp获取视频完整解析...</h3>")
        put_loading(shape='border', color='primary')
        getytdlpjson = json.load(os.popen("yt-dlp " + getdownurl + " -j"))
        put_text(getytdlpjson)
        put_success("JSON解析完成！")
        put_info(f'此页面系统将会显示{str(viewtimeout.read())}S，到时自动返回主页，可在"用户设置"中设置超时时间')
        viewtimeout.seek(0,0)
        time.sleep(int(viewtimeout.read()))
        viewtimeout.seek(0,0)
        downui()
config(theme='yeti', title=f'{appname} Premium Panel')
def main():
    set_env(title=f"{appname} Premium",output_max_width="100%", auto_scroll_bottom=True)
    login()
    downui()

if __name__ == '__main__':
    start_server(main, debug=True, port=5123)
    pywebio.session.hold()