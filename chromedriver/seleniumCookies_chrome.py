import time
import pickle
from selenium import webdriver
# from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from auth_data import vk_phone, vk_password


# options
options = webdriver.ChromeOptions()

# useragent = UserAgent()
# options.add_argument(f"user-agent={useragent.random}")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    # driver.get("https://vk.com/")
    # time.sleep(5)
    #
    # email_input = driver.find_element(By.ID, "index_email")
    # email_input.clear()
    # email_input.send_keys(vk_phone)
    # time.sleep(3)
    #
    # password_input = driver.find_element(By.ID, "index_pass")
    # password_input.clear()
    # password_input.send_keys(vk_password)
    # time.sleep(3)
    #
    # driver.find_element(By.ID, "index_expire").click()  # press on mark
    # time.sleep(3)
    #
    # # driver.find_element(By.ID, "index_login_button").click()  # press on login
    # password_input.send_keys(Keys.ENTER)  # press on Enter
    # time.sleep(10)
    #
    # driver.find_element(By.ID, "l_nwsf").click()  # press news
    # time.sleep(5)
    #
    # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{vk_phone}_cookies", "wb"))

    driver.get("https://vk.com/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{vk_phone}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
