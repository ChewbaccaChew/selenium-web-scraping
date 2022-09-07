import time
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.service import Service
from fake_useragent import UserAgent
from proxy_auth_data import login, password


# url = "https://www.instagram.com/"

# options
options = webdriver.FirefoxOptions()

# change useragent
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)

# set proxy
# без авторизации
# proxy = "138.128.91.65:8000"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
#
# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

# с авторизацией
proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

service = Service(r"C:\Users\PycharmProjects\firefoxdriver\geckodriver.exe")
# driver = webdriver.Firefox(service=service, options=options, proxy=proxy)
driver = webdriver.Firefox(service=service, seleniumwire_options=proxy_options)

try:
    # driver.get(url="http://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(5)

    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
