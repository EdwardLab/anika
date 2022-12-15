import web
import json
import os


urls = (
    '/', 'index'
)

class index:
    def GET(self):
        url = int(web.input().url)
        getytdlpjson = json.load(os.popen("yt-dlp " + url + " -j"))
        title = getytdlpjson['title']
        os.system('yt-dlp --output "/www/wwwroot/downloadfiles.anika.download" --no-mtime --merge-output-format mp4')
        geturl = f"http://downloadfiles.anika.download/{title}.mp4"
        article_info = {}
        data = json.loads(json.dumps(article_info))
        data['title'] = title
        data['url'] = geturl
        returnjson = json.dumps(data, ensure_ascii=False)
        return returnjson

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()