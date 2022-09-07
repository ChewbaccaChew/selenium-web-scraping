import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


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
    driver.get("https://www.avito.ru/moskva/transport")
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])  # перемещение по вкладкам
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

    username = driver.find_element(By.CLASS_NAME, "seller-info-name")
    print(f"User name is: {username.text}")
    print("#" * 20)
    time.sleep(5)

    driver.close()  # закрыть вкладку

    # после закрытия вкладки нужно обязательно перейти на основную стр, иначе ошибка
    driver.switch_to.window(driver.window_handles[0])
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

    items[1].click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

    username = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"User name is: {username.text}")
    print("-" * 20)

    ad_date = driver.find_element(By.CLASS_NAME, "title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print("-" * 20)

    joined_date = driver.find_elements(By.CLASS_NAME, "seller-info-value")[1]
    print(f"User since: {joined_date.text}")
    print("#" * 20)

    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
