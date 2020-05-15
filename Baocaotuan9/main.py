from my_driver import init_driver
from login import enter_username_password_login_fb, turn_off_popup, enter_keyword_to_search_on_fb


def loginFB(user, pwd, key):
    driver = init_driver()
    enter_username_password_login_fb(driver, user, pwd)
    turn_off_popup(driver)
    enter_keyword_to_search_on_fb(driver, key)
    print("done")
    driver.quit()
