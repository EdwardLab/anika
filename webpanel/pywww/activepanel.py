import pywebio.input
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
import sys
import os
import fnmatch
import re
import random
from datetime import *
import requests
import random
def sendsms(mobile, content):
    requests.get(f"http://#smsapi/sms.aspx/?action=send&userid=4621&account=#account&password=#password&mobile={mobile}&content={content}&sendTime=&extno=")
def main():
    set_env(title="Active key Premium", auto_scroll_bottom=True)
    put_html("<h1>激活您的Premium Panel</h1>")
    put_markdown(f"""
准备好您的`激活密钥`，稍后请您粘贴在下面
如果您还没有，请购买[点击这里](http://active.anika.download)
_________________________________________________

    """)
    #randomport = random.randint(10000,50000)
    f = open("key.txt")
    read = f.read()
    key = pywebio.input.textarea("在此处粘贴您的激活密钥:", minlength=25, required=True)
    if key in read:
        global username
        global password
        put_text("感谢您购买Anika Premium！")
        username = pywebio.input.input("为您的独立控制面板创建用户名：",required=True)
        password = pywebio.input.input("为您的独立控制面板创建密钥：",required=True)
        while True:
            passwordcheck = pywebio.input.input("再次输入密码：",required=True)
            if password != passwordcheck:
                toast("两次输入密码不一致！请重试！")
            else:
                break
        phonenum = pywebio.input.input("请输入11位中国大陆手机号码(用于通知等)：",required=True)
        check_code = random.randint(100000, 999999)
        print(check_code)
        sendsms(phonenum, f"【Anika会员】您好本次操作需要验证，您的验证码是{check_code}，请勿泄漏给他人。")
        while True:
            smscode = pywebio.input.input(f"验证码已发送到手机号：{phonenum}，请输入验证码：",required=True)
            print(smscode)
            if smscode != str(check_code):
                toast("短信验证码不正确！请重试！（如果无法通过短信验证码验证，请联系客服）再次获取验证码请刷新页面，在此刷新页面您的激活码不会失效")
            else:
               break
        put_info("我们正在为您创建独立下载面板，请稍后...")
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
        f = open(userpath + '/username.txt', "w")
        f.write(username)
        f.close()
        f = open(userpath + '/userpassword.txt', "w")
        f.write(password)
        getregtime = datetime.now() + timedelta(days=30)
        lastgetregtime = getregtime.strftime("%Y%m%d")
        f = open(userpath + '/regtime.txt', "w")
        f.write(lastgetregtime)
        f=open("phonenum.txt",mode="a")
        f.write(str(phonenum) + "\n")
        f=open(userpath + "/phonenum.txt",mode="w")
        f.write(str(phonenum))
        sendsms(phonenum, "【Anika会员】您的面板已成功开通，请前往官网查看。")
        try:
            os.mkdir(userpath + '/settings')
            userdir = 'panel/' + username
            viewtimeoutwrite = open(userdir + '/settings/viewtimeout.txt', 'w')
            viewtimeoutwrite.write("40")
            gauth = open(userdir + '/settings/gauth.txt', 'w')
            gauth.write("disable")
        except:
            pass
        put_success("创建成功！您的独立面板地址是http://panel.anika.download ，您的用户名是：" + username + "您的密码是：" + password + " ,请务必保存好您的密码，严禁合租，共享，本系统自带IP检测功能，一旦发现异常将会永久封禁。若面板无法登录使用，请联系客服或管理员咨询。")
    else:
        put_error("错误的密钥，请检查...")
config(theme='yeti', title='Anika Active')