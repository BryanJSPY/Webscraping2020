from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_find_class(driver, time, class_name):
    wait = WebDriverWait(driver, time)

    ele = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name))
    )
    return ele


def wait_find_xpath(driver, time, xpath):
    wait = WebDriverWait(driver, time)

    ele = wait.until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return ele


def wait_find_id(driver, time, id):
    wait = WebDriverWait(driver, time)

    ele = wait.until(
        EC.presence_of_element_located((By.ID, id))
    )
    return ele
