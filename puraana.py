 # comment_section = driver.find_element(By.XPATH, '//*[@id="comments"]')
    # driver.execute_script("arguments[0].scrollIntoView();",comment_section)
    # time.sleep(7)

    # last_height = driver.execute_script('return document.documentElement.scrollHeight')

    # while True:
    #     driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

    #     time.sleep(2)

    #     new_height = driver.execute_script('return document.documentElement.scrollHeight')

    #     if new_height == last_height:
    #         break

    #     last_height = new_height

    # driver.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")

    # comment_elems = driver.find_elements(By.XPATH,'//*[@id="content-text"]/span[0]')
    # print(comment_elems)