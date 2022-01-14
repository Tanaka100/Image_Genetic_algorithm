from selenium import webdriver
from time import sleep
import os
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# プラウザ起動（Chrome）
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) # chromedriver.exeを使う

# リストからURLをひとつづつ処理
print('file:///{}/tmp.png'.format(os.getcwd()))
driver.get('file:///{}/tmp.png'.format(os.getcwd()))

while True:
    sleep(1)
    driver.refresh()