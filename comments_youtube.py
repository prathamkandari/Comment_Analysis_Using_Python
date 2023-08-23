import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from bs4 import BeautifulSoup
import pandas as pd
import re

def ScrapComment(url):
    geckodriver_path = GeckoDriverManager().install()
    firefox_service = FirefoxService(executable_path = geckodriver_path)
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    # option = webdriver.FirefoxOptions()
    # option.add_argument("--headless")
    # driver = webdriver.Firefox(executable_path = GeckoDriverManager().install(), options = option)
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    driver.get(url)
    time.sleep(2)
    prev_h = 0
    list2 = []
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
        driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 300})")
        time.sleep(2)
        prev_h +=300
        if prev_h >= height:
            break
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    dataframe = pd.DataFrame(columns=['URL'])
    dataframe = pd.DataFrame(columns=['TITLE'])
    dataframe = pd.DataFrame(columns=['COMMENTS'])
    dataframe = pd.DataFrame(columns=['DATE'])
    title_text_div = soup.select_one('#title h1').get_text('yt-formatted-string')
    title = title_text_div[19:-19]
    comment_div = soup.select('#content #content-text')
    comment_list = [x.text for x in comment_div]
    comments_with_questions = []
    for comment in comment_list:
    # Check if the substring "UK" is present in the comment
        if "What" in comment or "what" in comment or "Why" in comment or "why" in comment or "How" in comment or "how" in comment or "When" in comment or "when" in comment or "Where" in comment or "where" in comment or "Who" in comment or "who" in comment or "Which" in comment or "which" in comment or "Whose" in comment or "whose" in comment or "If" in comment or "if" in comment or "Would" in comment or "would" in comment or "Can" in comment or "can" in comment or "Are" in comment or "are" in comment or "Did" in comment or "did" in comment or "?" in comment:
            dataframe['URL'] = url
            dataframe['TITLE'] = title
            comments_with_questions.append(comment)
            print(url, title, comments_with_questions)
            dataframe['COMMENTS'] = comments_with_questions

            pattern = re.compile(r'\b(\d+)\s+(day|week|month|year)s?\s+ago\b', re.IGNORECASE)
            info_span = soup.select_one('#info-container yt-formatted-string')
            if info_span:
                matches = pattern.findall(info_span.get_text())
                if matches:
                    for match in matches:
                        str = match[0], match[1] + " ago"
                        list2.append(str)
                        # print(match[0], match[1] + " ago")  # Print the matched value and unit (day/week/month/year)
                    dataframe['Date'] = list2
            
            dataframe.to_excel("MYURL.xlsx")
    # print(comments_with_questions)
    # print(title,comment_list)

if __name__ == "__main__":

    urls = [
        'https://www.youtube.com/watch?v=26YgjGYlvOQ',
        'https://www.youtube.com/watch?v=OFQVBdR93tM',
        'https://www.youtube.com/watch?v=FdFSPe2zuqs',
        'https://www.youtube.com/watch?v=PQoEa7WhBwg',
        'https://www.youtube.com/watch?v=9DHecZfvsuM',
        'https://www.youtube.com/watch?v=1Vj4gglxUH4',
        'https://www.youtube.com/watch?v=ES8JZVLwXJM',
        'https://www.youtube.com/watch?v=AU9FGQw6iAY',
        'https://www.youtube.com/watch?v=W9mgbudxOYY',
        'https://www.youtube.com/watch?v=G-bOXCt_t00',
        'https://www.youtube.com/watch?v=iYZrDoSVqNs',
        'https://www.youtube.com/watch?v=YUaFUUUGmpg',
        'https://www.youtube.com/watch?v=VhXNR575k7s',
        'https://www.youtube.com/watch?v=u3jH5GI4uss',
        'https://www.youtube.com/watch?v=za_hCt2CPBQ',
        'https://www.youtube.com/watch?v=LS2AFnx3zHI',
        'https://www.youtube.com/watch?v=CH62LmyiMz0',
        'https://www.youtube.com/watch?v=vDEuM24j2YE',
        'https://www.youtube.com/watch?v=HW2doTGNZAY',
        'https://www.youtube.com/watch?v=JNj5DDfrl9Q',
        'https://www.youtube.com/watch?v=FtK_8AAlFfE',
        'https://www.youtube.com/watch?v=Il6hmU1F7YE',
        'https://www.youtube.com/watch?v=MvaZ2ODk1RU',
        'https://www.youtube.com/watch?v=UAFk_r_3gkY',
        'https://www.youtube.com/watch?v=R6MOT7UvnwQ',
        'https://www.youtube.com/watch?v=algH8CFyhe4',
        'https://www.youtube.com/watch?v=jx5KsneAzyM',
        'https://www.youtube.com/watch?v=itofF7b1t-w',
        'https://www.youtube.com/watch?v=XSDe-Oi4gLQ',
        'https://www.youtube.com/watch?v=K6gOiJCPYKI',
        'https://www.youtube.com/watch?v=9p9ToP9GPiw',
        'https://www.youtube.com/watch?v=eJekyaHJ_xA',
        'https://www.youtube.com/watch?v=ERLaa_aUfOU',
        'https://www.youtube.com/watch?v=PI-_0gDyp6M',
        'https://www.youtube.com/watch?v=2KJ9FuVatZg',
        'https://www.youtube.com/watch?v=ffdIWfiXI5k',
        'https://www.youtube.com/watch?v=cZ4wAHJg_E4',
        'https://www.youtube.com/watch?v=dr-QMXpQRXc',
        'https://www.youtube.com/watch?v=H042YowkTyE',
        'https://www.youtube.com/watch?v=hN8kZO-Uht8',
        'https://www.youtube.com/watch?v=SYMnN7OsGbc',
        'https://www.youtube.com/watch?v=CO5UNXOomoI',
        'https://www.youtube.com/watch?v=GdXSiM0u3wk',
        'https://www.youtube.com/watch?v=9xNb9OX1yvM',
        'https://www.youtube.com/watch?v=Mjq1_PDUI6o',
        'https://www.youtube.com/watch?v=EaStGNDB8Hg',
        'https://www.youtube.com/watch?v=XG2ppnZa6IA',
        'https://www.youtube.com/watch?v=tyxi70dS8OI',
        'https://www.youtube.com/watch?v=ejdTb1QU48I',
        'https://www.youtube.com/watch?v=9hGJVlwKI5g',
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
        'https://www.youtube.com/watch?v=51ulX-s8eKM',
        'https://www.youtube.com/watch?v=RcD-_p-LXGY',
        'https://www.youtube.com/watch?v=2-0ann2-cog',
        'https://www.youtube.com/watch?v=p3CUnGqY9_c',
        'https://www.youtube.com/watch?v=YTcui-yZkEs',
        'https://www.youtube.com/watch?v=9AuafXkjof0',
        'https://www.youtube.com/watch?v=D0QeGFRe0kU',
        'https://www.youtube.com/watch?v=QGjBdn3v5q4',
        'https://www.youtube.com/watch?v=shSzswpMFwE',
        'https://www.youtube.com/watch?v=zIvVGykap_0',
        'https://www.youtube.com/watch?v=vpQ0I-GgBZY',
        'https://www.youtube.com/watch?v=nMZQ1usXwTg',
        'https://www.youtube.com/watch?v=w1tNlxGnG6s',
        'https://www.youtube.com/watch?v=Rsl-_Ko6FsU',
        'https://www.youtube.com/watch?v=wqqPSncpIHY',
        'https://www.youtube.com/watch?v=Q-UAEteQ7N8',
        'https://www.youtube.com/watch?v=5aecsmeg1jo',
        'https://www.youtube.com/watch?v=q4DKJa9jnU8',
        'https://www.youtube.com/watch?v=3dACTAiXfH0',
        'https://www.youtube.com/watch?v=n6hY0LTVAwU',
        'https://www.youtube.com/watch?v=MUbQBYLWu5Y',
        'https://www.youtube.com/watch?v=rvMqzFwJXuY',
        'https://www.youtube.com/watch?v=1G6xsd3522k',
        'https://www.youtube.com/watch?v=74XKgLWNsho',
        'https://www.youtube.com/watch?v=RakZVMs4y6Q',
        'https://www.youtube.com/watch?v=aHoxZGHkFMs',
        'https://www.youtube.com/watch?v=JU9rSFUnvDM',
        'https://www.youtube.com/watch?v=rEf7eSOf7c4',
        'https://www.youtube.com/watch?v=3oy6rpNCprk',
        'https://www.youtube.com/watch?v=h38H_OLs8aM',
        'https://www.youtube.com/watch?v=8hZed5RaGhs',
        'https://www.youtube.com/watch?v=lBo63mzrw8U',
        'https://www.youtube.com/watch?v=JZrfIx6DjpQ',
        'https://www.youtube.com/watch?v=n2PRffyGCeI',
        'https://www.youtube.com/watch?v=3ICGhWPbqL8',
        'https://www.youtube.com/watch?v=pjUG51GrQ3M',
        'https://www.youtube.com/watch?v=yt0OZ_9sgTw',
        'https://www.youtube.com/watch?v=-I2giiWJV4o',
        'https://www.youtube.com/watch?v=hs6_3NMhY5g',
        'https://www.youtube.com/watch?v=UR7b8UudZHg',
        'https://www.youtube.com/watch?v=1tJ2gekq50g',
        'https://www.youtube.com/watch?v=iq2SV1aZMVM',
        'https://www.youtube.com/watch?v=NAmNHqABAD8',
        'https://www.youtube.com/watch?v=eydmTnSQ0yE',
        'https://www.youtube.com/watch?v=gkdYgGjNr_o',
        'https://www.youtube.com/watch?v=QQF4eja2JqE',
        'https://www.youtube.com/watch?v=YdJbylX5RWk',
        'https://www.youtube.com/watch?v=NtK9VgE-uDc',
        'https://www.youtube.com/watch?v=iaUOksYxGAM',
        'https://www.youtube.com/watch?v=5gn8_wW8LUM',
        'https://www.youtube.com/watch?v=MqdR0UCbYdU',
        'https://www.youtube.com/watch?v=3V1004gk6Ac',
        'https://www.youtube.com/watch?v=Z57FkXuLsh8',
        'https://www.youtube.com/watch?v=dhiiLKEZALc',
        'https://www.youtube.com/watch?v=83DehjR2-9w',
        'https://www.youtube.com/watch?v=uIZ1exl5Ac0',
        'https://www.youtube.com/watch?v=Bq-rsm06noA',
        'https://www.youtube.com/watch?v=AyD4jioIWfk',
        'https://www.youtube.com/watch?v=dypH7s5L6lU',
        'https://www.youtube.com/watch?v=yo07jkJVV-8',
        'https://www.youtube.com/watch?v=dtQs8afuCZ4',
        'https://www.youtube.com/watch?v=rN5TY05ZQ9U',
        'https://www.youtube.com/watch?v=fellXn9hle8',
        'https://www.youtube.com/watch?v=gqfnZJ2Gg7M',
        'https://www.youtube.com/watch?v=huUxkxNcLdo',
        'https://www.youtube.com/watch?v=8E4jyaZDgDk',
        'https://www.youtube.com/watch?v=Ppk2bcNg-Ek',
        'https://www.youtube.com/watch?v=4t-_pUPQ54A',
        'https://www.youtube.com/watch?v=6vBIctAlWI0',
        'https://www.youtube.com/watch?v=MMcZcLjH7Ho',
        'https://www.youtube.com/watch?v=p4JyX4Vpacw',
        'https://www.youtube.com/watch?v=PENTANWGSlk',
        'https://www.youtube.com/watch?v=ghKf9Ubp7SA',
        'https://www.youtube.com/watch?v=CJ7N6vK56Jw',
        'https://www.youtube.com/watch?v=1eRjzihiOEs',
        'https://www.youtube.com/watch?v=-8iNrMeIg44',
        'https://www.youtube.com/watch?v=SNj5t6NBfxk',
        'https://www.youtube.com/watch?v=ZRiwP1jd-YE',
        'https://www.youtube.com/watch?v=6Fjh12yTD_8',
        'https://www.youtube.com/watch?v=xLgneXll9CI',
        'https://www.youtube.com/watch?v=tsBZLZk-2Hc',
        'https://www.youtube.com/watch?v=7YJ2fTxFFK4',
        'https://www.youtube.com/watch?v=YUfX4go9DSA',
        'https://www.youtube.com/watch?v=Jm46Ype91c0',
        'https://www.youtube.com/watch?v=9vlu9831zsw',
        'https://www.youtube.com/watch?v=nZ-a-DoDLdM',
        'https://www.youtube.com/watch?v=0dfPLSWh4aI',
        'https://www.youtube.com/watch?v=c5boDJ82u9Y',
        'https://www.youtube.com/watch?v=clSJ8pndTrg',
        'https://www.youtube.com/watch?v=j7bSS0mMIU0',
        'https://www.youtube.com/watch?v=J-Y2lhMSIXc',
        'https://www.youtube.com/watch?v=IHZunEzZMSM',
        'https://www.youtube.com/watch?v=whW6OfTQ6X8',
        'https://www.youtube.com/watch?v=86xSHLpbZ7M',
        'https://www.youtube.com/watch?v=pShVR5dyOLI',
        'https://www.youtube.com/watch?v=GFO46bTvl_4',
        'https://www.youtube.com/watch?v=T2l_3FknG4A',
        'https://www.youtube.com/watch?v=KjNkHr8vsNQ',
        'https://www.youtube.com/watch?v=XFMrWk5hCQ0',
        'https://www.youtube.com/watch?v=OdkdAav8J5s',
        'https://www.youtube.com/watch?v=uTYJhFS4sfI',
        'https://www.youtube.com/watch?v=aRLTx_E1RVY',
        'https://www.youtube.com/watch?v=-uuh_UNBHmE',
        'https://www.youtube.com/watch?v=FiA6E6Yrndg',
        'https://www.youtube.com/watch?v=NFcroWkIG0k',
        'https://www.youtube.com/watch?v=jQtB41Q1H9c',
        'https://www.youtube.com/watch?v=rBAZaLX5m8c',
        'https://www.youtube.com/watch?v=8APxOM9LBM4',
        'https://www.youtube.com/watch?v=UFP_PBckJfA',
        'https://www.youtube.com/watch?v=ejtfSjbGr0M',
        'https://www.youtube.com/watch?v=rpg5di7djf4',
        'https://www.youtube.com/watch?v=YA0vRLnJIEE',
        'https://www.youtube.com/watch?v=lkFD-3DxcYY',
        'https://www.youtube.com/watch?v=XW4tmxQNW-A',
        'https://www.youtube.com/watch?v=7fqn2RhI23E',
        'https://www.youtube.com/watch?v=gOAh8j0p-vA',
        'https://www.youtube.com/watch?v=Ov-smAv4Flk',
        'https://www.youtube.com/watch?v=VfG08_7CmwU',
        'https://www.youtube.com/watch?v=F_5oIgK2Qw4',
        'https://www.youtube.com/watch?v=h1kwrcY6mvc',
        'https://www.youtube.com/watch?v=Zlu9xcOdBhw',
        'https://www.youtube.com/watch?v=ETvsqzgYTo8',
        'https://www.youtube.com/watch?v=px3jcH249GU',
        'https://www.youtube.com/watch?v=TG82-VuDNmc',
        'https://www.youtube.com/watch?v=_k-cIguhnv4',
        'https://www.youtube.com/watch?v=6XFDAFBrgAI',
        'https://www.youtube.com/watch?v=0djFVbZMIsQ',
        'https://www.youtube.com/watch?v=I2UcqJ44VNo',
        'https://www.youtube.com/watch?v=_olbAAjbQnA',
        'https://www.youtube.com/watch?v=hcJIwdDnQPI',
        'https://www.youtube.com/watch?v=p2-DVl8wNDA',
        'https://www.youtube.com/watch?v=dXk5gwU157k',
        'https://www.youtube.com/watch?v=KKknN2m8KRI',
        'https://www.youtube.com/watch?v=WbjWY-rr0lw',
        'https://www.youtube.com/watch?v=xXfkJqs6ND4',
        'https://www.youtube.com/watch?v=eNTNZcIBKdI',
        'https://www.youtube.com/watch?v=0DA5aqiYhCU',
        'https://www.youtube.com/watch?v=_nwphBlZ4eo',
        'https://www.youtube.com/watch?v=SSuPpgirDvc',
        'https://www.youtube.com/watch?v=Gb0PLClB9pI',
        'https://www.youtube.com/watch?v=LjDXPNr3wLA',
        'https://www.youtube.com/watch?v=dIxPVvZAB68',
        'https://www.youtube.com/watch?v=7m5hcZ0up9Y',
        'https://www.youtube.com/watch?v=tyU9cGvUTFw',
        'https://www.youtube.com/watch?v=7bqglALbLb8',
        'https://www.youtube.com/watch?v=8hKvesouYpA',
        'https://www.youtube.com/watch?v=_U29QkWGVm4',
        'https://www.youtube.com/watch?v=eedsUni4wCo',
        'https://www.youtube.com/watch?v=MnHKOwO37Eg',
        'https://www.youtube.com/watch?v=NPCIr4H62JI',
        'https://www.youtube.com/watch?v=xtESt-J3e2s',
        'https://www.youtube.com/watch?v=W3RN1km5IKI',
        'https://www.youtube.com/watch?v=aymUm7lpoBQ',
        'https://www.youtube.com/watch?v=CykQsfDpEAY',
        'https://www.youtube.com/watch?v=9tNGqmN2aj0',
        'https://www.youtube.com/watch?v=8k-yjzMm4GA',
        'https://www.youtube.com/watch?v=TcNPf7ALNfo',
        'https://www.youtube.com/watch?v=o8osxW-kkHE',
        'https://www.youtube.com/watch?v=6iQOhazzGQI',
        'https://www.youtube.com/watch?v=Ty4vhio1Zs4',
        'https://www.youtube.com/watch?v=Of57DU912ko',
        'https://www.youtube.com/watch?v=r3yBt_2D8UI',
        'https://www.youtube.com/watch?v=nUlfHK48CTg',
        'https://www.youtube.com/watch?v=oNEKNG3ELTs',
        'https://www.youtube.com/watch?v=A4hBpylPu3g',
        'https://www.youtube.com/watch?v=GLg-iapGwBs',
        'https://www.youtube.com/watch?v=cVunITq9UKA',
        'https://www.youtube.com/watch?v=8rZLPNVw-6E',
        'https://www.youtube.com/watch?v=rVLElHV609Q',
        'https://www.youtube.com/watch?v=iirTJ56RRwA',
        'https://www.youtube.com/watch?v=6fnNF-fv7sg',
        'https://www.youtube.com/watch?v=z9oG5hOsAU8',
        'https://www.youtube.com/watch?v=gqftZOCOh40',
        'https://www.youtube.com/watch?v=rq22lPAGVus',
        'https://www.youtube.com/watch?v=AQljxZtp-oU',
        'https://www.youtube.com/watch?v=hV4VISJJ7uA',
        'https://www.youtube.com/watch?v=N2Y9T_pyofs',
        'https://www.youtube.com/watch?v=8OnluazdzM4',
        'https://www.youtube.com/watch?v=-pIFXbtQdRI',
        'https://www.youtube.com/watch?v=NE8ifdpTZ2g',
        'https://www.youtube.com/watch?v=4rPI_AeNOrI',
        'https://www.youtube.com/watch?v=QMUeZm6gEYs',
        'https://www.youtube.com/watch?v=359lawwLNQQ',
        'https://www.youtube.com/watch?v=VpBmps9MvY8',
        'https://www.youtube.com/watch?v=hVj2tomsd-Q',
        'https://www.youtube.com/watch?v=f2KH5GNNKsY',
        'https://www.youtube.com/watch?v=_lp6cAt1wZE',
    ]
    for url in urls:
        ScrapComment(url)