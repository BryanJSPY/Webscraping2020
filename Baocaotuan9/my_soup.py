from bs4 import BeautifulSoup
import time


def get_soup(driver):
    time.sleep(2)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_all(soup, html_element, attribute_html, name):
    list_ele = soup.find_all(html_element, {attribute_html: name})
    return list_ele


def find(soup, html_element, attribute_html, name):
    ele = soup.find(html_element, {attribute_html: name})
    return ele


def get_text(ele):
    return ele.get_text()
