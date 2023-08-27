from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import sys
import time
# from grpc import channel
import io
import csv
import pandas as pd

def scrape(url):


    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    driver.maximize_window()

    time.sleep(5)

    title = driver.find_element(By.XPATH,
        '//*[@id="title"]/h1/yt-formatted-string'
    ).text

    print(title)

    comment_section=driver.find_element(By.XPATH, '//*[@id="comments"]')
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(7)

    last_height= driver.execute_script('return document.documentElement.scrollHeight')
    
    while(True):
        driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

        time.sleep(2)
        new_height= driver.execute_script('return document.documentElement.scrollHeight')

        if new_height == last_height:
            break

    driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

    username_elems = driver.find_elements(By.XPATH, '//*[@id="author-text"]')
    comment_elems = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

    with io.open("finaltest.csv","w",newline='',encoding='utf-16') as file:
        writer = csv.writer(file, delimiter=',',quoting=csv.QUOTE_ALL)
        writer.writerow(["Username", "Comment"])
        for username, comment in zip(username_elems, comment_elems):
            writer.writerow([username.text, comment.text])


if __name__ == '__main__':
    scrape(sys.argv[1])