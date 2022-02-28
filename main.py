import pathlib
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def open_browser():
    options = webdriver.ChromeOptions()
    chrome_folder = pathlib.Path(__file__).parent.resolve()

    options.add_argument(f"--user-data-dir={os.path.join(chrome_folder, 'Cookie')}")


    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get("https://orteil.dashnet.org/cookieclicker/")
    
    return browser

def cookies_info(browser):
    cookies_text = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[15]/div[4]").text

    cookies_text = cookies_text.split("\n")
    cookies = cookies_text[0].replace(" cookies", "")
    cookies = int(cookies)

    per_second = cookies_text[1].replace("per second : ","")
    per_second = float(per_second)
    
    return cookies, per_second

def item_info(browser, item):
    xpath_item = (f'/html/body/div/div[2]/div[19]/div[3]/div[6]/div[{item}]/div[3]/div[3]')
    item_text = browser.find_element(By.XPATH, xpath_item).text
    if item_text.strip() == "":
        items = 0
    else:
        items = float(item_text)
    
    return items




browser = open_browser()
time.sleep(3)

while True:
    cookies, per_second = cookies_info(browser)

    print(f"Você tem: {cookies} cookies")
    print(f"Você faz novos {per_second} cookies por segundo")

    items = {"cursor": 2, "grandma": 3, "farm": 4}

    cursors = item_info(browser, items['cursor'])
    grandmas = item_info(browser, items['grandma'])
    farms = item_info(browser, items['farm'])

    print(f"Você tem {cursors} cursores")
    print(f"Você tem {grandmas} vovós")
    print(f"Você tem {farms} fazendas")
    
    time.sleep(2)
