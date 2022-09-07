import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
# for ChromeDriver version 79.0.3945.16 or over:
options.add_argument("--disable-blink-features=AutomationControlled")  # other options ->
# -> https://peter.sh/experiments/chromium-command-line-switches/

# headless mode (фоновый режим)
# options.add_argument("--headless")  # or options.headless = True


service = Service(r"C:\PycharmProjects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    start_time = datetime.datetime.now()  # время начала выполнения программы

    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")

    # time.sleep(5)  # ожидание 5 сек
    driver.implicitly_wait(5)  # ожидание не более 5 сек

    items = driver.find_elements(By.XPATH, "//div[@data-marker='item']")
    items[0].click()
    # print(driver.window_handles)

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])  # перемещение по вкладкам
    print(f"Currently URL is: {driver.current_url}")

    # time.sleep(5)
    driver.implicitly_wait(5)

    username = driver.find_element(By.CLASS_NAME, "seller-info-name")
    print(f"User name is: {username.text}")
    print("#" * 20)

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.close()  # закрыть вкладку

    # после закрытия вкладки нужно обязательно перейти на основную стр, иначе ошибка
    driver.switch_to.window(driver.window_handles[0])
    print(f"Currently URL is: {driver.current_url}")

    # time.sleep(5)
    driver.implicitly_wait(5)

    items[1].click()

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    print(f"Currently URL is: {driver.current_url}")

    # time.sleep(5)
    driver.implicitly_wait(5)

    username = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"User name is: {username.text}")
    print("-" * 20)

    ad_date = driver.find_element(By.CLASS_NAME, "title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print("-" * 20)

    joined_date = driver.find_elements(By.CLASS_NAME, "seller-info-value")[1]
    print(f"User since: {joined_date.text}")
    print("#" * 20)

    # time.sleep(5)
    driver.implicitly_wait(5)

    finish_time = datetime.datetime.now()  # время завершения программы
    spent_time = finish_time - start_time  # время затраченное на выполнение программы
    print(spent_time)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# время выполнения с использованием sleep = 0:00:48.308311
# время выполнения с использованием _wait = 0:00:18.789547
