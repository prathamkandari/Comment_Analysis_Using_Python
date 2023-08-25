from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from grpc import Channel
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import sys
import time
import pandas as pd
from bs4 import BeautifulSoup
import scrapetube
import io
import csv

#function for scraping details from youtube
# Initialize an empty list to store data
data = []

# Function for scraping details from YouTube
def scrape(url):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # Find and extract title and dates      
    title = driver.find_element(By.XPATH, '//*[@id="title"]/h1/yt-formatted-string').text
    dates = driver.find_element(By.XPATH, '//*[@id="info"]/span[3]').text
    print(title)
    print(dates)
    prev_h = 0
    # OLD ONE

    while True:
        height = driver.execute_script("""
                function getActualHeight() { 
                    return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                    );
                }
                return getActualHeight();
            """)
        driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 200})")
        time.sleep(1)
        prev_h +=200
        if prev_h >= height:
            break

    soup=BeautifulSoup(driver.page_source, 'html.parser')

    comment_div = soup.select('#content #content-text')
    comment_list = [x.text for x in comment_div]
    # print(comment_list)
    comments_with_questions = []
    for comment in comment_list:
    # Check if the substring "UK" is present in the comment
        if "What" in comment or "what" in comment or "Why" in comment or "why" in comment or "How" in comment or "how" in comment or "When" in comment or "when" in comment or "Where" in comment or "where" in comment or "Who" in comment or "who" in comment or "Which" in comment or "which" in comment or "Whose" in comment or "whose" in comment or "If" in comment or "if" in comment or "Would" in comment or "would" in comment or "Can" in comment or "can" in comment or "Are" in comment or "are" in comment or "Did" in comment or "did" in comment or "?" in comment:
            # comments_with_questions.append(comment)
            print(comment)
            data.append({'URL': url, 'TITLE': title, 'DATE': dates, 'COMMENTS': comment})

    driver.quit()  # Close the browser



if __name__ == '__main__':

    # urls = [
    #     'https://www.youtube.com/watch?v=NE8ifdpTZ2g',
    # ]

    # for url in urls:
    #     scrape(url)

    # # Create a DataFrame from the collected data
    # dataframe = pd.DataFrame(data)

    # # Save the dataframe to Excel
    # dataframe.to_excel("Comments.xlsx", index=False)

    channelid="UCl_1ZH0cUIFXGh9Tj0A47DA"
    list=[]

    url="https://www.youtube.com/watch?v="
    videos = scrapetube.get_channel(channelid)

    for video in videos:
        url1 = url + str(video['videoId'])
        list.append(url1)
        scrape(url1)

    dataframe = pd.DataFrame(data)
    dataframe.to_excel("Comments.xlsx", index=False)