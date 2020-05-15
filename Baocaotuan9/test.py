from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/search/top/?q=ncovid19&epa=SEARCH_BOX")
