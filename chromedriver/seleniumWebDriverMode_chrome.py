import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# # disable webdriver mode:
# # for older ChromeDriver under version 79.0.3945.16:
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over:
options.add_argument("--disable-blink-features=AutomationControlled")  # other options ->
# -> https://peter.sh/experiments/chromium-command-line-switches/

service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
