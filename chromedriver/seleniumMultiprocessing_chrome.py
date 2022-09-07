import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from multiprocessing import Pool


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
# for ChromeDriver version 79.0.3945.16 or over:
options.add_argument("--disable-blink-features=AutomationControlled")  # other options ->
# -> https://peter.sh/experiments/chromium-command-line-switches/

# headless mode (фоновый режим)
# options.add_argument("--headless")  # or options.headless = True

# список для первого варианта:
urls_list = ["https://stackoverflow.com", "https://instagram.com", "https://vk.com"]


# def get_data(url):  # первый вариант функции, результат в папке media
#     try:
#         service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
#         driver = webdriver.Chrome(service=service, options=options)
#
#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
# if __name__ == "__main__":
#     p = Pool(processes=3)
#     p.map(get_data, urls_list)


def get_data(url):
    try:
        service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url=url)
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "lazyload-wrapper").find_element(By.CLASS_NAME, "item-video-container").click()
        time.sleep(random.randrange(3, 10))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    # первый вариант:
    # p = Pool(processes=3)
    # p.map(get_data, urls_list)

    # второй вариант:
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)
