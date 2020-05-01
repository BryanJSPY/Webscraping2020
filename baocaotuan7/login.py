import my_driver
import my_wait
import press_keys


def enter_username_password_login_fb(driver, username, password):

    my_driver.find_id_send_keys(driver, "email", username)
    my_driver.find_id_send_keys(driver, "pass", password)
    my_driver.find_xpath_click(
        driver, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")


def turn_off_popup(driver):
    check_popup = my_wait.wait_find_class(driver, 10, "_3ixn")

    if check_popup:
        press_keys.ESC(driver)


def enter_keyword_to_search_on_fb(driver, keyword):

    search_keyword_bar = my_wait.wait_find_xpath(
        driver, 10, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]")

    if search_keyword_bar:
        my_driver.find_xpath_send_keys(
            driver, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]", keyword)

    search_button = my_wait.wait_find_xpath(
        driver, 10, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button")

    if search_button:
        my_driver.find_xpath_click(
            driver, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button")

    tag_post_fb = my_wait.wait_find_xpath(
        driver, 10, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a")

    if tag_post_fb:
        my_driver.find_xpath_click(
            driver, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a")

    tag_your_group_and_pages = my_wait.wait_find_xpath(
        driver, 10, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]")

    if tag_your_group_and_pages:
        my_driver.find_xpath_click(
            driver, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]")
