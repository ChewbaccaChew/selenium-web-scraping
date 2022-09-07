import time
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
# for ChromeDriver version 79.0.3945.16 or over:
options.add_argument("--disable-blink-features=AutomationControlled")  # other options ->
# -> https://peter.sh/experiments/chromium-command-line-switches/

# headless mode (фоновый режим)
options.add_argument("--headless")  # or options.headless = True


service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    print("Passing authentication...")
    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys(vk_phone)
    time.sleep(3)

    password_input = driver.find_element(By.ID, "index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)

    driver.find_element(By.ID, "index_expire").click()  # press on mark
    time.sleep(3)

    # driver.find_element(By.ID, "index_login_button").click()  # press on login
    password_input.send_keys(Keys.ENTER)  # press on Enter
    time.sleep(10)

    print("Going to the profile page...")
    driver.find_element(By.ID, "l_pr").click()  # press profile page
    time.sleep(5)

    print("Start watching the video...")
    driver.find_element(By.CLASS_NAME, "page_post_sized_thumbs").click()
    time.sleep(5)
    print("Finish watching the video...")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
