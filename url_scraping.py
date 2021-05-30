from selenium import webdriver
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as Soup
import time
from selenium.webdriver.common.keys import Keys



#使用相對位置執行webdriver
driver = webdriver.Chrome(".\..\chromedriver")

#將後面改成要爬蟲的店家網址
driver.get("https://www.google.com/maps/place/12MINI%E7%B6%93%E5%85%B8%E5%8D%B3%E4%BA%AB%E9%8D%8B-%E6%8D%B7%E9%81%8B%E5%85%AC%E9%A4%A8%E5%BA%97(%E5%83%85%E4%BE%9B%E5%A4%96%E5%B8%B6%E5%A4%96%E9%80%81%E6%9C%8D%E5%8B%99)/@25.0155113,121.462303,12z/data=!4m9!1m2!2m1!1z5YWs6aSoIOeBq-mNiw!3m5!1s0x3442a9f5d4c95191:0xa4f2536dd0dcdfb8!8m2!3d25.0155349!4d121.5323118!15sCg3lhazppKgg54Gr6Y2LWhcKBueBq-mNiyIN5YWs6aSoIOeBq-mNi5IBEmhvdF9wb3RfcmVzdGF1cmFudJoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1VRd01IWXphRmgzRUFF")

wait = 5

reviewer_name = []
reviews_num = []
reviewer_stars = []
review_date = []
review_content = []

#得到標題作為檔名，這邊失敗可能是因為time.sleep()時間不夠長
time.sleep(wait)
title = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1').text
if len(title) > 10: 
    title = title[0:11]

#點進所有評論
time.sleep(wait)
driver.find_element_by_class_name("widget-pane-link").click()

#獲得總評論數量，決定到底要滾輪滾幾次
time.sleep(wait)
reviewsnum = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]').text.rstrip(' 篇評論')
try:
    reviewsnum = int(reviewsnum)
except:
    reviewsnum = int(reviewsnum.replace(',', ''))

#嘗試過瀏覽器的滾輪極限是115次，可自己改
if reviewsnum > 1000:
    scroll_num = 10
elif 1000 > reviewsnum > 500:
    scroll_num = 5
else:
    scroll_num = 5

#向下捲動，開始爬蟲
pane = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
for i in range(0, scroll_num):
    time.sleep(1)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)

# 獲得網頁原始碼
time.sleep(wait)
soup = Soup(driver.page_source, "lxml")
all_reviews = soup.find_all(class_='ODSEW-ShBeI NIyLF-haAclf gm2-body-2')

for i in range(0, len(all_reviews)):
    # 評論者名稱
    try:
        name = all_reviews[i].find(class_="ODSEW-ShBeI-title").text
        name = name.strip(" ")
        reviewer_name.append(name)
    except:
        reviewer_name.append("N/A")

    # 評論者的評論數
    try:
        reviews = all_reviews[i].find(class_="ODSEW-ShBeI-VdSJob").text
        reviews = reviews.strip(" ").strip("在地嚮導")
        reviews_num.append(reviews)
    except:
        reviews_num.append("N/A")

    # 評論星數
    try:
        stars = str(all_reviews[i].find(class_="ODSEW-ShBeI-H1e3jb").get('aria-label').strip().strip("顆星"))
        reviewer_stars.append(stars)
    except:
        reviewer_stars.append("N/A")

    # 評論時間
    try:
        date = all_reviews[i].find(class_ = "ODSEW-ShBeI-RgZmSc-date").text
        date = date.strip(" ")
        review_date.append(date)
    except:
        review_date.append("N/A")

    # 評論內容
    try:
        text = all_reviews[i].find(class_ = "ODSEW-ShBeI-text").text
        text = text.strip(" ")
        review_content.append(text)
    except:
        review_content.append("N/A")  

#做成dataframe後輸出
allstuff = pd.DataFrame()
allstuff["reviewer_name"] = reviewer_name
allstuff["reviews_num"] = reviews_num
allstuff["reviewer_stars"] = reviewer_stars
allstuff["review_date"] = review_date
allstuff["review_content"] = review_content

allstuff.to_csv(f'{title}.csv',encoding="utf-8-sig")


print("爬蟲完畢!")