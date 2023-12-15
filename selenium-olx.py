from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    username = '996166018'
    password = 'Bahrom1357'

    title = 'iphone 11 asdasd ad a'
    description = '''
    Bir marta kiring boldi kodiz ishl
    asa register qismini uchirib boshqa joyini ishlataver
    ing . Tekshirayotgan payt ochib quyasiz hammasini ishlaydi nasb 
    Like ni bilmadm lekn. Like shu clik qilsa boldida ishlaydi. Qolganini a
    kkountsiz qilishga harakat qilish kk. 
    Boshqa iloj yuq manimcha
    '''
    location = 'Ташкент, Яккасарайский район'

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://uz.login.olx.com/?cc=eyJjYyI6MCwiZ3JvdXBzIjoiIn0%3D&client_id=2s42fsas18c0kbs55g4cpjccvf&code_challenge=J7Zjh3TZMaJdr1_dyYmCIxxNB1-yUolz212G2S17h8E&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fwww.olx.uz%2Faccount%2Fcallback%2F&st=eyJzbCI6IjE4YmVkOTE3ZDU4eDUyNWQyNmU2IiwicyI6IjE4YzZkY2QyMGExeDYzNzE0MWY3IiwiY2MiOjAsImdyb3VwcyI6IiJ9&state=eyJyZWZlcnJlciI6Imh0dHBzOlwvXC93d3cub2x4LnV6XC9teWFjY291bnRcLyJ9')

    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-ypypxs'))
    )
    login_button.click()

    # Wait for the login process to complete (adjust the timeout as needed)
    WebDriverWait(driver, 10).until(EC.url_contains("www.olx.uz"))
    
    sleep(16)

    post_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-2txnih'))
    )
    post_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains("https://www.olx.uz/adding/?bs=myaccount_adding"))

    sleep(6)

    driver.find_element('id', 'title').send_keys(title)


    category_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'css-1272b3n'))
    )
    category_button.click()

    sleep(4)

    sub_categories_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-kfy9sk'))
        )
    
    sub_categories_button.click()

    sleep(3)

    sub_sub_categories_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-1grn515'))
        )
    
    sub_sub_categories_button.click()

    sleep(3)

    sub_sub_categories_button_final = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-7lx9dr'))
        )
    sub_sub_categories_button_final.click()
    sleep(3)


    driver.find_element('id', 'description').send_keys(description)


    price_free = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-1x4iwgr')))
    price_free.click()
    sleep(2)


    physical_person = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-19wrg31')))
    physical_person.click()
    sleep(2)


    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-6z56jw')))
    dropdown.click()
    sleep(2)


    item_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-10jahps')))
    item_select.click()
    sleep(2)


    item_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-10jahps')))
    item_select.click()
    sleep(2)


    status_bu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'css-19wrg31')))
    status_bu.click()
    sleep(2)


    driver.find_element('name', 'city_id').send_keys(location)




if __name__ == '__main__':
    main()
