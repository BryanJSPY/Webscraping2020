from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time


def ESC(driver):
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.ESCAPE)
    actions.key_up(Keys.ESCAPE)
    actions.perform()


def HOME(driver):
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.HOME)
    actions.key_up(Keys.HOME)
    actions.perform()


def END(driver):
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.END)
    actions.key_up(Keys.END)
    actions.perform()


def CLICK(driver, ele):
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(ele)
    actions.click(ele)
    actions.perform()
