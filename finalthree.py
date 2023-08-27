from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from grpc import Channel
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
    
    comment_section=driver.find_element(By.XPATH, '//*[@id="comments"]')
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(5)

    last_height= driver.execute_script('return document.documentElement.scrollHeight')
    
    while(True):
        driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

        time.sleep(2)
        new_height= driver.execute_script('return document.documentElement.scrollHeight')

        if new_height == last_height:
            break

    driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

    comment_elems = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    for comment_elem in comment_elems:
        comment_text = comment_elem.text
        if "What" in comment_text or "what" in comment_text or "Why" in comment_text or "why" in comment_text or "How" in comment_text or "how" in comment_text or "When" in comment_text or "when" in comment_text or "Where" in comment_text or "where" in comment_text or "Who" in comment_text or "who" in comment_text or "Which" in comment_text or "which" in comment_text or "Whose" in comment_text or "whose" in comment_text or "If" in comment_text or "if" in comment_text or "Would" in comment_text or "would" in comment_text or "Can" in comment_text or "can" in comment_text or "Are" in comment_text or "are" in comment_text or "Did" in comment_text or "did" in comment_text or "?" in comment_text:
            data.append({'URL': url, 'TITLE': title, 'DATE': dates, 'COMMENTS': comment_text})


if __name__ == '__main__':

    urls = [
        'https://www.youtube.com/watch?v=5aY2JW6Ss9I',
        'https://www.youtube.com/watch?v=KznoERwgQHI',
        'https://www.youtube.com/watch?v=VINCo_5v7sI',
        'https://www.youtube.com/watch?v=XD-nGE3CAWU',
        'https://www.youtube.com/watch?v=Q1Ep_DfACZ8',
        'https://www.youtube.com/watch?v=XBA69k03ekA',
        'https://www.youtube.com/watch?v=73lfb11Lx7s',
        'https://www.youtube.com/watch?v=djz7oBCNyzs',
        'https://www.youtube.com/watch?v=6LvSInz3JwA',
        'https://www.youtube.com/watch?v=C1UqsEol5Ng',
    ]

    for url in urls:
        scrape(url)

    # Create a DataFrame from the collected data
    dataframe = pd.DataFrame(data)

    # Save the dataframe to Excel
    dataframe.to_excel("Comments1.xlsx", index=False)

    # channelid="UCl_1ZH0cUIFXGh9Tj0A47DA"
    # list=[]

    # url="https://www.youtube.com/watch?v="
    # videos = scrapetube.get_channel(channelid)

    # for video in videos:
    #     url1 = url + str(video['videoId'])
    #     list.append(url1)
    #     scrape(url1)

    # dataframe = pd.DataFrame(data)
    # dataframe.to_excel("Comments.xlsx", index=False)