from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from langdetect import detect
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://facebook.com")
    return driver


def enter_username_password_login_fb(driver, username, password):
    username_input_bar = driver.find_element_by_id("email")
    username_input_bar.send_keys(username)

    password_input_bar = driver.find_element_by_id("pass")
    password_input_bar.send_keys(password)

    fb_login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")
    fb_login_button.click()


def turn_off_popup(driver, wait):
    check_popup = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "_3ixn"))
    )

    if check_popup:
        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.ESCAPE)
        actions.key_up(Keys.ESCAPE)
        actions.perform()


def enter_keyword_to_search_on_fb(driver, wait, keyword):
    search_keyword_bar = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]"))
    )

    if search_keyword_bar:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]").send_keys(keyword)

    search_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button"))
    )

    if search_button:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button"
        ).click()

    tag_post_fb = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a'))
    )

    if tag_post_fb:
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a').click()

    tag_your_group_and_pages = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]'))
    )
    if tag_your_group_and_pages:
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[4]").click()


def get_all_posts_and_comments(driver, wait, all_id_en_posts, all_content_en_posts, total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts):

    all_id_posts = []
    all_content_posts = []
    all_en_posts_selected = []
    find_which_post_have_comments = []
    all_total_comments_each_post = []
    language_on_each_post = []

    first_post = driver.find_elements_by_class_name("_6-e5")

    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.END)
    actions.key_up(Keys.END)
    actions.perform()

    last_post = driver.find_elements_by_class_name("_6-e5")

    while len(first_post) < len(last_post):
        first_post = driver.find_elements_by_class_name("_6-e5")

        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.END)
        actions.key_up(Keys.END)
        actions.perform()

        last_post = driver.find_elements_by_class_name("_6-e5")

    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.END)
    actions.key_up(Keys.END)
    actions.perform()

    time.sleep(2)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    all_tag_div_contain_posts = soup.find_all("div", {"class": "_6-e5"})
    all_tag_a_contain_total_comments_each_post = soup.find_all(
        "a", {"class": "_3hg- _42ft"})

    # lay tat cac cac id cua cac post
    for post in all_tag_div_contain_posts:
        all_id_posts.append(post.get('id'))

    # lay may tai the <a> chua comment
    for x in all_tag_a_contain_total_comments_each_post:
        find_which_post_have_comments.append(
            x.get_text())  # Lay chu so khong lay comment

    # Xem coi cai post nay co comment hay khong
    # Can phai sua lai lay so khong lay chu comment
    i = 0
    for x in all_id_posts:
        html_content_post = soup.find("div", {"id": x}).get_text()
        check_post_have_comments = html_content_post.find("Comment")
        if check_post_have_comments != -1:
            all_total_comments_each_post.append(
                find_which_post_have_comments[i])
            i += 1
        else:
            all_total_comments_each_post.append('0')

    # Lay noi dung may cai post
    for x in all_id_posts:
        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.END)
        actions.key_up(Keys.END)
        actions.perform()

        time.sleep(1)
        ele = driver.find_element_by_id(x)
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.click(ele)
        actions.perform()

        time.sleep(1)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        content_post = soup.find(
            "div", {"class": "_5pbx userContent _3576"})

        # lay noi dung cai post
        all_content_posts.append(content_post.get_text())

        # Xac dinh ngon ngu cua cai post
        language_on_each_post.append(detect(content_post.get_text()))

        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.ESCAPE)
        actions.key_up(Keys.ESCAPE)
        actions.perform()

        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.END)
        actions.key_up(Keys.END)
        actions.perform()

    en_posts = []
    all_total_comments_each_en_post = []
    for x in range(len(language_on_each_post)):
        if language_on_each_post[x] == "en":
            en_posts.append(language_on_each_post[x])
            all_id_en_posts.append(all_id_posts[x])
            all_content_en_posts.append(all_content_posts[x])
            all_total_comments_each_en_post.append(
                all_total_comments_each_post[x])

    for x in range(len(all_id_en_posts)):
        comment = {}
        comment["id"] = all_id_en_posts[x]
        comment["content_post"] = all_content_en_posts[x]
        comment["contain_comment"] = all_total_comments_each_en_post[x]
        comment["lang"] = en_posts[x]
        all_en_posts_selected.append(comment)

    for x in all_en_posts_selected:
        check_post_appear = wait.until(
            EC.presence_of_element_located(
                (By.ID, x["id"])))

        if check_post_appear:
            time.sleep(2)
            ele = driver.find_element_by_id(x["id"])
            actions = ActionChains(driver)
            actions.move_to_element(ele)
            actions.click(ele)
            actions.perform()

            if x["contain_comment"] != "0":
                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.END)
                actions.key_up(Keys.END)
                actions.perform()

                time.sleep(1)
                ele = driver.find_element_by_class_name("_4vn1")
                actions = ActionChains(driver)
                actions.move_to_element(ele)
                actions.click(ele)
                actions.perform()

                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.END)
                actions.key_up(Keys.END)
                actions.perform()

                while True:
                    try:
                        time.sleep(1)
                        driver.find_element_by_partial_link_text(
                            "View").click()

                        time.sleep(1)
                        actions = ActionChains(driver)
                        actions.key_down(Keys.END)
                        actions.key_up(Keys.END)
                        actions.perform()
                    except Exception:
                        pass
                        break

                while True:
                    try:
                        print("Replies")
                        time.sleep(1)
                        ele = driver.find_element_by_class_name(
                            "_4sxc _42ft")
                        print(ele.text)
                        time.sleep(5)
                        actions = ActionChains(driver)
                        actions.move_to_element(ele)
                        actions.click(ele)
                        actions.perform()
                        actions
                        time.sleep(5)
                        actions = ActionChains(driver)
                        actions.key_down(Keys.END)
                        actions.key_up(Keys.END)
                        actions.perform()
                    except Exception:
                        pass
                        break

                all_users_replied_recently_post = []
                all_comments_replied_recently_post = []
                total_users_comments_on_recently_post = []

                content = driver.page_source
                soup = BeautifulSoup(content, "html.parser")

                tag_html_users = soup.find_all("a", {"class": "_6qw4"})
                tag_html_replies = soup.find_all("span", {"class": "_3l3x"})
                tag_html_users_replies = soup.find_all(
                    "div", {"class": "_72vr"})

                for x in tag_html_users:
                    all_users_replied_recently_post.append(x.get_text())

                for x in tag_html_replies:
                    all_comments_replied_recently_post.append(x.get_text())

                for x in tag_html_users_replies:
                    total_users_comments_on_recently_post.append(x.get_text())

                all_en_users_replied_recently_post = []
                all_en_comments_replied_recently_post = []
                total_en_users_comments_on_recently_post = []
                # loc may cai comment su dung tieng anh
                for x in all_comments_replied_recently_post:
                    try:
                        lang = detect(x)

                        if lang == "en":
                            all_en_comments_replied_recently_post.append(x)
                    except Exception:
                        pass
                        continue
                # lay may ca user comment co chua commnet ting anh o dang tren
                m = ""
                for x in all_en_comments_replied_recently_post:
                    if m == "":
                        for y in total_users_comments_on_recently_post:
                            if y.find(x) != -1:
                                total_en_users_comments_on_recently_post.append(
                                    y)
                                m = y
                                break
                    else:
                        for m in total_users_comments_on_recently_post:
                            if m.find(x) != -1:
                                total_en_users_comments_on_recently_post.append(
                                    m)
                                m = m
                                break

                m = ""
                for x in total_en_users_comments_on_recently_post:
                    if m == "":
                        for y in all_users_replied_recently_post:
                            if x.find(y) != -1:
                                all_en_users_replied_recently_post.append(y)
                                m = y
                                break

                    else:
                        for m in all_users_replied_recently_post:
                            if x.find(m) != -1:
                                all_en_users_replied_recently_post.append(
                                    m)
                                m = m
                                break

                total_en_comment_each_en_posts.append(
                    len(all_en_comments_replied_recently_post))
                all_users_replied_en_comment_each_en_posts.append(
                    all_en_users_replied_recently_post)
                all_content_en_comment_each_en_posts.append(
                    all_en_comments_replied_recently_post)

                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.ESCAPE)
                actions.key_up(Keys.ESCAPE)
                actions.perform()

                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.END)
                actions.key_up(Keys.END)
                actions.perform()

            else:
                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.ESCAPE)
                actions.key_up(Keys.ESCAPE)
                actions.perform()

                time.sleep(1)
                actions = ActionChains(driver)
                actions.key_down(Keys.END)
                actions.key_up(Keys.END)
                actions.perform()


def write_all_posts_and_comments(all_id_en_posts, all_content_en_posts,  total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts):

    df = pd.DataFrame(
        {'Id': all_id_en_posts, 'Post': all_content_en_posts})
    df.to_csv('fb_scraping.csv', index=False, encoding='utf-8')

    all_id_en_posts_to_csv = []

    for x in range(len(total_en_comment_each_en_posts)):
        i = 0
        all_id_en_post_to_csv = []
        if total_en_comment_each_en_posts[x] != 0:
            while i < total_en_comment_each_en_posts[x]:
                all_id_en_post_to_csv.append(all_id_en_posts[x])
                i += 1
            all_id_en_posts_to_csv.append(all_id_en_post_to_csv)
        else:
            all_id_en_posts_to_csv.append(all_id_en_post_to_csv)

    for x in range(len(total_en_comment_each_en_posts)):
        a = total_en_comment_each_en_posts[x]
        b = all_id_en_posts_to_csv[x]
        if a == b:
            print(x)
            
    for x in range(len(all_users_replied_en_comment_each_en_posts)):
        if all_users_replied_en_comment_each_en_posts[x]:
            file_name = "id_user_comment_{}.csv".format(x)
            df = pd.DataFrame(
                {'Id': all_id_en_posts_to_csv[x], 'Users': all_users_replied_en_comment_each_en_posts[x], 'Comments': all_content_en_comment_each_en_posts[x]})
            df.to_csv(file_name, index=True, encoding='utf-8')


def get_error_on_driver(driver):
    print("error")
    driver.quit()


def shut_down_driver(driver):
    print("done")
    driver.quit()


def main():
    all_id_en_posts = []
    all_content_en_posts = []
    all_users_replied_en_comment_each_en_posts = []
    all_content_en_comment_each_en_posts = []
    total_en_comment_each_en_posts = []

    driver = init_driver()
    wait = WebDriverWait(driver, 10)
    keyword = "ncovid19"

    enter_username_password_login_fb(
        driver, "dct99002@gmail.com", "vmax21399")
    turn_off_popup(driver, wait)
    enter_keyword_to_search_on_fb(driver, wait, keyword)
    get_all_posts_and_comments(driver, wait, all_id_en_posts,
                               all_content_en_posts, total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts)
    shut_down_driver(driver)
    write_all_posts_and_comments(all_id_en_posts, all_content_en_posts,
                                 total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts)


main()
