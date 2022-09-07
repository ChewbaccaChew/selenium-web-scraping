import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# options
options = webdriver.FirefoxOptions()

# change useragent
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)  # не работает?!

service = Service(r"C:\Users\PycharmProjects\firefoxdriver\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
