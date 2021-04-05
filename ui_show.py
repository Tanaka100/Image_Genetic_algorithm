from selenium import webdriver
from time import sleep
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# プラウザ起動（Chrome）
driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=options) # chromedriver.exeを使う

# リストからURLをひとつづつ処理
print('file:///{}/tmp.png'.format(os.getcwd()))
driver.get('file:///{}/tmp.png'.format(os.getcwd()))

while True:
    sleep(1)
    driver.refresh()