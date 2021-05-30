# Use BeautifulSoup and selenium to scrap google reviews

* 台灣大學<R語言程式設計與資料科學導論>的期末專案中的爬蟲部分，在專案開始前所作的嘗試。 
* 如果程式有error可能是瀏覽器還沒載入完畢，要在滾動或是網頁載入前後加上time.sleep()或增加等待時間 
* 滾動次數個人嘗試過是115次為上限，再多可能會當機  
    <br>
* The maximum scrolling attempts is 115 times (as I try),and it may crash if you enter more.
* If there is an error, the reason may be the browser has not finished loading. Add time.sleep() or increase the waiting time may help.

## URL.py

* 只要在地圖上有出現的店家都可以爬取
* 沒有爬取圖片 
* 爬取的網址在google地圖上必須以這種形式展現 e.g. [溏老鴨平價小火鍋](https://www.google.com/maps/place/溏老鴨平價小火鍋/@25.019571,121.463328,12z/data=!4m9!1m2!2m1!1z5Y-w5aSnIOeBq-mNiw!3m5!1s0x3442a9891704aba5:0xe8a5e5e77ee338a3!8m2!3d25.019571!4d121.5333658!15sCg3lj7DlpKcg54Gr6Y2LWh4KDeWPsOWkpyDngavpjYsiDeWPsOWkpyDngavpjYuSASNzaGFidV9zaGFidV9hbmRfc3VraXlha2lfcmVzdGF1cmFudJoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1VSWk5IRjZhRWhuRUFF)   
   <br>
* This code helps scrap all stores and reviews that appears on map.
* No pictures included. 
* The scraped URL must show in this form on the google map as displayed. e.g. [Faros London](https://www.google.com/maps/place/Faros+London/@51.5176041,-0.2848219,11z/data=!3m1!5s0x48761b4905760fcf:0xf92dbf0a644bcc8!4m8!1m2!2m1!1slondon+spaghetti!3m4!1s0x48761b49057684f1:0x65cb2e8b0c61129b!8m2!3d51.5222255!4d-0.1140018) 

## Keywords.py

* URL檔的改動，目標是讓user可以直接在console輸入想要搜尋的關鍵字e.g. 「台大 周邊美食」或「溫州街 咖啡廳」以爬取店家及評論  
    <br>
* Allow users to directly enter the keywords (e.g. London spaghetti )in the console that they want to search on map then scrap stores and comments.



