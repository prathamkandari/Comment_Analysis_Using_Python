import scrapetube
import pandas as pd
from main import scrape
# from comment_date import comment_date

channelid="UCl_1ZH0cUIFXGh9Tj0A47DA"
list=[]

url="https://www.youtube.com/watch?v="

# dataframe = pd.DataFrame(columns=["URL"])

videos = scrapetube.get_channel(channelid)

for video in videos:
    url1 = url + str(video['videoId'])
    list.append(url1)
    # comment_date(url1)
    # print(url1)

    scrape(url1)

# print(list)

# dataframe['URL'] = list
# dataframe.to_excel("MYURL.xlsx")

# videos=scrapetube.get_channel(channelid)
