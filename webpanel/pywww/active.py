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
def main():
    set_env(title="Anika Premium", auto_scroll_bottom=True)
    put_html("<h1>Anika Premium</h1>")
    put_text("为什么需要Premium？")
    put_markdown("""
1.完整的本地化与中文支持
2.免费的客服（除附加服务外）
3.完全独立的Anika Premium Panel控制面板，支持设置自己密码，随处享受高速下载和长期不变的端口
4.yl-dlp下载内核支持，支持更多网站的视频下载，更稳定
5.高速的网络支持
6.安心的售后，若出现任何不可使用的问题，直接更换面板（免费版仅社区支持）
7.premium用户专门的讨论群，任何问题第一知晓
不只是这些！快来升级您的服务！
    """)
    put_link("我还没有密钥呢，我要购买密钥", "http://active.anika.download")
    put_text('_______________________',
        sep=' '
    )
    put_link("我有密钥啦！现在去激活独立面板", "./activepanel")
    put_text('_______________________',
        sep=' '
    )
    put_link("我要登陆", "./premiumpanel")
    put_text('_______________________',
        sep=' '
    )
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=9000)
    pywebio.session.hold()