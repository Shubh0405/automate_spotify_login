from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

print('Please enter your username:')
username = input()
print('Please enter your password:')
password = input()



driver = webdriver.Chrome(r"C:\Users\Shubh Gupta\Documents\python and django bootcamp\chromedriver.exe")
driver.maximize_window()

driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
username_field = driver.find_element_by_name("username")
username_field.clear()
username_field.send_keys(username)

password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys(password)

driver.find_element_by_id("login-button").send_keys(Keys.ENTER)

WebDriverWait(driver,15).until(cond.visibility_of_element_located((By.CLASS_NAME,'RootlistItem__link')))
playlist = driver.find_elements_by_class_name('RootlistItem__link')
if len(playlist)==0:
    print("you have no playlist")
else:
    print('enter the playlist number you want to play.')
    for i in range(len(playlist)):
        print(str(i) +' for '+playlist[i].text)
    a=int(input())
    playlist[a].click()
    time.sleep(5)
    driver.find_element_by_class_name('_11f5fc88e3dec7bfec55f7f49d581d78-scss').send_keys(Keys.ENTER)
