from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def main():
    
    username = '996166018'
    password = 'Bahrom1357'

    title = 'hyundai tucson'
   
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.olx.uz/')
    driver.find_element('id', 'search').send_keys(title)


    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-coyrj2'))
    )
    search.click()

    sleep(10)

    
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-coyrj2'))
    )
    search.click()

if __name__ == '__main__':
    main()