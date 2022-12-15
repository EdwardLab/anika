import pywebio.input
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
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
  <h1 class="display-3">欢迎使用Anika Premium面板！</h1>
  <p class="lead">在这里享受高速，便捷的下载体验</p>
  <hr class="my-4">
  <p>随时下载您的视频，只需要一个账户！</p>
  </p>
</div>  
  </body>
</html>
    """)
def main():
    head()
    put_html("<h1>Anika Premium</h1>")
    put_markdown("""
![logo](https://www.anika.download/wp-content/uploads/2022/07/Anika.ico)
    """)
    put_link("激活Premium Panel", "./active")
    put_text('_______________________',
        sep=' '
    )
    put_link("登录Premium Panel", "./premiumpanel")
    put_text('_______________________',
        sep=' '
    )
def active():
    set_env(title="Active key Premium", auto_scroll_bottom=True)
    put_html("<h1>激活您的Premium Panel</h1>")
    put_markdown(f"""
准备好您的`激活密钥`，稍后请您粘贴在下面
如果您还没有，请购买[点击这里](http://active.anika.download)
_________________________________________________

    """)
    
if __name__ == '__main__':
    start_server(main, debug=True, port=5100)
    set_env(title=f"Anika Premium",output_max_width="100%", auto_scroll_bottom=True)
    pywebio.session.hold()