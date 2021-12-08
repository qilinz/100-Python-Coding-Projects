from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# Bot setting
TIMEOUT = 300  # [seconds] how long do you want the program to run?
DURATION = 5   # [seconds] how long do you want to check the store?


# start webdriver
s = Service("/Users/karin/Documents/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def get_store_item():
    """
    Check what's in the store
    :return: a dict of store items
    """
    store_data = driver.find_element(By.ID, "store")
    store_list = store_data.text.split("\n")
    store_dict = {}
    for i in range(len(store_list)//2):
        product_list = store_list[2 * i].split(" - ")
        store_dict[i] = {
            "item": product_list[0],
            "value": int(product_list[1].replace(",", ""))
        }
    return store_dict


def buy_best_item(store_dict):
    """
    Check the most expensive item that is affordable and buy it.
    Max buy one.
    :param store_dict: the dictionary of the store items
    """
    # let the driver wait implicitly
    driver.implicitly_wait(5)
    # get the cookie count
    cookies = driver.find_element(By.ID, "money")
    cookie_count = int(cookies.text.replace(",", ""))

    # check what can be bought from the most expensive one
    for _ in range(len(store_dict) - 1, -1, -1):
        if cookie_count > store_dict[_]["value"]:
            click_id = f"buy{store_dict[_]['item']}"
            # prevent click before the item is loaded on the website
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.ID, click_id)))
            driver.find_element(By.ID, click_id).click()
            break


# Basic info
cookie = driver.find_element(By.ID, "cookie")
store = get_store_item()

# Start the timer
timeout_start = timeout_repeat = time.time()
while time.time() < timeout_start + TIMEOUT:
    # click the cookie
    cookie.click()
    # try buy items in store every 5 seconds
    while time.time() - timeout_repeat > DURATION:
        buy_best_item(store)
        timeout_repeat = time.time()


# Print the result
speed = driver.find_element(By.ID, "cps").text
print(speed.title())



