from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import re
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://facebook.com")

wait = WebDriverWait(driver, 10)

user_ip_fb = driver.find_element_by_id("email")
user_ip_fb.send_keys("dct99002@gmail.com")

pwd_ip_fb = driver.find_element_by_id("pass")
pwd_ip_fb.send_keys("vmax21399")

login_btn_fb = driver.find_element_by_id("u_0_b")
login_btn_fb.click()

pop_up = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3ixn"))
)

if pop_up:
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.ESCAPE)
    actions.key_up(Keys.ESCAPE)
    actions.perform()

search_ip_fb = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]"))
)

if search_ip_fb:
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]").send_keys("ncovid19")

search_btn_fb = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button"))
)

if search_btn_fb:
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button"
    ).click()

post_tag_fb = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a'))
)

if post_tag_fb:
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a').click()

public_tag_fb = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]"))
)

if public_tag_fb:
    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]").click()
i = 0
while i < 100:
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.END)
    actions.key_up(Keys.END)
    actions.perform()
    i+=1
    
ele = driver.find_elements_by_class_name("_6-e5")
print("There are {} element".format(len(ele)))
