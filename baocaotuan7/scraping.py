from my_driver import init_driver
import login
import press_keys
from get_data_fb import get_all_posts_and_comments
from sentiment import sentiment_all_comments
from data_csv import write_all_posts_and_comments


def get_error_on_driver(driver):
    print("error")
    driver.quit()


def shut_down_driver(driver):
    print("done")
    driver.quit()


if __name__ == "__main__":
    while True:
        driver = init_driver()
        try:
            all_id_en_posts = []
            all_content_en_posts = []
            all_users_replied_en_comment_each_en_posts = []
            all_content_en_comment_each_en_posts = []
            total_en_comment_each_en_posts = []
            sentiment_all_en_comments = []

            login.enter_username_password_login_fb(
                driver, "dct99002@gmail.com", "vmax21399")

            login.turn_off_popup(driver)

            keyword = "ncovid19"
            login.enter_keyword_to_search_on_fb(driver, keyword)

            get_all_posts_and_comments(driver, all_id_en_posts, all_content_en_posts, total_en_comment_each_en_posts,
                                       all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts)
            shut_down_driver(driver)

            sentiment_all_comments(sentiment_all_en_comments,
                                   all_content_en_comment_each_en_posts)
            write_all_posts_and_comments(all_id_en_posts, all_content_en_posts,  total_en_comment_each_en_posts,
                                         all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts, sentiment_all_en_comments)
            break
        except Exception:
            pass
            get_error_on_driver(driver)
