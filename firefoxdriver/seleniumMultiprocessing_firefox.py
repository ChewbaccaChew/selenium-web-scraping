import time
import random
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

# headless mode
# options.headless = True


def get_data(url):
    try:
        service = Service(r"C:\Users\PycharmProjects\firefoxdriver\geckodriver.exe")
        driver = webdriver.Firefox(service=service, options=options)

        driver.get(url=url)
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "lazyload-wrapper").find_element(By.CLASS_NAME, "item-video-container").click()
        time.sleep(random.randrange(3, 10))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)
