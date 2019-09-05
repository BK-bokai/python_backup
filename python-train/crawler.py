#抓取 PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index8058.html"
#建立一個Request 物件,附加 Request Header 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)
#資料原始碼, 取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title") #尋找class="title"的div標籤
print(titles)

for title in titles:
    if title.a !=None:
        print(title.a.string)