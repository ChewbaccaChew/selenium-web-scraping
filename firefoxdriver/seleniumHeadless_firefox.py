import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from auth_data import instagram_login, instagram_password


# options
options = webdriver.FirefoxOptions()

# change useragent
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)  # не работает?!

# headless mode (фоновый режим)
options.headless = True

service = Service(r"C:\Users\PycharmProjects\firefoxdriver\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    print("Passing authentication...")
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

    print("Going to the post...")
    video_post = driver.get("https://www.instagram.com/p/CCsYtgjn1mj/")
    print("Start watching the video...")
    time.sleep(5)

    print("Unmuting audio...")
    unmute_audio = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/span/div")
    unmute_audio.click()
    time.sleep(5)
    print("Finish watching the video...")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
