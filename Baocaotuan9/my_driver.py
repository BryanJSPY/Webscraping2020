from selenium import webdriver
import time


def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://facebook.com")
    return driver


def find_id_send_keys(driver, id, key_words):
    time.sleep(1)
    ele = driver.find_element_by_id(id)
    ele.send_keys(key_words)


def find_xpath_send_keys(driver, xpath, key_words):
    time.sleep(1)
    ele = driver.find_element_by_xpath(xpath)
    ele.send_keys(key_words)


def find_xpath_click(driver, xpath):
    time.sleep(1)
    ele = driver.find_element_by_xpath(xpath)
    ele.click()


def find_partial_link_text_click(driver, text):
    time.sleep(1)
    ele = driver.find_element_by_partial_link_text(text)
    ele.click()
