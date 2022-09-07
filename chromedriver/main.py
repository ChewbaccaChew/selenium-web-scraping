# https://chromedriver.storage.googleapis.com/index.html - drivers for chrome
# https://github.com/mozilla/geckodriver/releases - drivers for firefox

# https://peter.sh/experiments/chromium-command-line-switches/ - список опций Chromium
# библиотека fake-useragent:
# https://pypi.org/project/fake-useragent/
# https://github.com/hellysmile/fake-useragent

# https://proxy6.net/ - pay proxy


import time
# import random
# from selenium import webdriver  # pip
from seleniumwire import webdriver  # pip
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent  # pip
from proxy_auth_data import login, password


# url = "https://www.instagram.com/"

user_agent_list = [
    "hello_world",
    "best_of_the_best",
    "python_python",
    "abcdefg"
]

# options
options = webdriver.ChromeOptions()

# change useragent
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")
useragent = UserAgent()
options.add_argument(f"user-agent={useragent.opera}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")  # proxy без авторизации, либо привязанный к ip

# proxy с авторизацией
proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service, seleniumwire_options=proxy_options)

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
