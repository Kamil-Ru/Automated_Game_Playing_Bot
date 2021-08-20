from selenium import webdriver
import time

chrome_driver_path = "C:\Chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)


def check_condition():
    money = int(driver.find_element_by_id("money").text.replace(',', ''))

    cursor = driver.find_element_by_id("buyCursor")
    cursor_cost = int(cursor.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    grandma = driver.find_element_by_id("buyGrandma")
    grandma_cost = int(grandma.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    factory = driver.find_element_by_id("buyFactory")
    factory_cost = int(factory.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    mine = driver.find_element_by_id("buyMine")
    mine_cost = int(mine.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    shipment = driver.find_element_by_id("buyShipment")
    shipment_cost = int(shipment.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    alchemy = driver.find_element_by_id("buyAlchemy lab")
    alchemy_cost = int(alchemy.find_element_by_css_selector("b").text.split()[3].replace(',', ''))

    portal = driver.find_element_by_id("buyPortal")
    portal_cost = int(portal.find_element_by_css_selector("b").text.split()[2].replace(',', ''))

    time = driver.find_element_by_id("buyTime machine")
    time_cost = int(time.find_element_by_css_selector("b").text.split()[3].replace(',', ''))

    if money > time_cost:
        time.click()
    elif money > portal_cost:
        portal.click()
    elif money > alchemy_cost:
        alchemy.click()
    elif money > shipment_cost:
        shipment.click()
    elif money > mine_cost:
        mine.click()
    elif money > factory_cost:
        factory.click()
    elif money > grandma_cost:
        grandma.click()
    elif money > cursor_cost:
        cursor.click()


cookie = driver.find_element_by_id("cookie")
timeout = time.time() + 60 * 5  # 5 minutes from now
check = time.time() + 5
test = 0
while True:
    cookie.click()

    if time.time() > timeout:
        break
    if time.time() > check:
        check_condition()
        check = time.time() + 5

cps = driver.find_element_by_id("cps").text
print(f"CPS = {cps}")
