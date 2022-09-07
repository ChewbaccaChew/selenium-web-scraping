import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from auth_data import instagram_login, instagram_password


# options
options = webdriver.FirefoxOptions()

# change useragent
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

service = Service(r"C:\Users\PycharmProjects\firefoxdriver\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(instagram_login)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(instagram_password)
    time.sleep(5)

    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # cookies
    pickle.dump(driver.get_cookies(), open(f"{instagram_login}_cookies", "wb"))

    # подгружаем куки
    # driver.get("https://www.instagram.com/")
    # time.sleep(5)
    #
    # for cookie in pickle.load(open(f"{instagram_login}_cookies", "rb")):
    #     driver.get_cookies(cookie)
    #
    # time.sleep(5)
    # driver.refresh()
    # time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
