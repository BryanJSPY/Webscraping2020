from press_keys import ESC, END, CLICK
from my_soup import get_soup, find_all, find, get_text
from langdetect import detect
from my_wait import wait_find_id
from my_driver import find_partial_link_text_click


def get_all_posts_and_comments(driver, all_id_en_posts, all_content_en_posts, total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts):

    show_all_posts(driver)

    soup = get_soup(driver)
    all_tag_div_contain_posts = find_all(soup, "div", "class", "_6-e5")
    all_tag_a_contain_total_comments_each_post = find_all(
        soup, "a", "class", "_3hg- _42ft")

    all_id_posts = get_all_id_posts(all_tag_div_contain_posts)
    all_total_comments_each_post = get_total_comment_each_posts(
        soup, all_id_posts, all_tag_a_contain_total_comments_each_post)

    all_content_posts = get_all_content_posts(driver, all_id_posts)
    language_on_each_post = get_language_on_each_post(all_content_posts)

    en_posts = []
    all_total_comments_each_en_post = []
    get_all_en_things(language_on_each_post, en_posts, all_id_en_posts, all_id_posts, all_content_en_posts,
                      all_content_posts, all_total_comments_each_en_post, all_total_comments_each_post)

    all_en_posts_selected = get_all_en_things_dict(
        all_id_en_posts, all_content_en_posts, all_total_comments_each_en_post, en_posts)

    get_all_comment_in_all_en_posts_selected(driver, all_en_posts_selected, total_en_comment_each_en_posts,
                                             all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts)


def open_all_tag_view(driver):
    while True:
        try:
            find_partial_link_text_click(driver, "View")
            END(driver)

        except Exception:
            pass
            break


def open_all_tag_reply(driver):
    while True:
        try:
            ele = driver.find_element_by_class_name(
                "_4sxc _42ft")
            CLICK(driver, ele)
            END(driver)
        except Exception:
            pass
            break


def get_all_comment_in_all_en_posts_selected(driver, all_en_posts_selected, total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts):
    for x in all_en_posts_selected:
        check_post_appear = wait_find_id(driver, 10, x["id"])

        if check_post_appear:
            ele = driver.find_element_by_id(x["id"])
            CLICK(driver, ele)

            if x["contain_comment"] != "0":
                END(driver)
                ele = driver.find_element_by_class_name("_4vn1")
                CLICK(driver, ele)
                END(driver)

                open_all_tag_view(driver)
                open_all_tag_reply(driver)

                soup = get_soup(driver)
                tag_html_users = find_all(soup, "a", "class", "_6qw4")
                tag_html_replies = find_all(soup, "span", "class", "_3l3x")
                tag_html_users_replies = find_all(
                    soup, "div", "class", "_72vr")

                all_users_replied_recently_post = get_text_from_html(
                    tag_html_users)

                all_comments_replied_recently_post = get_text_from_html(
                    tag_html_replies)

                total_users_comments_on_recently_post = get_text_from_html(
                    tag_html_users_replies)

                all_en_comments_replied_recently_post = get_all_en_comments_replied_recently_post(
                    all_comments_replied_recently_post)

                total_en_users_comments_on_recently_post = get_total_en_users_comments_on_recently_post(
                    all_en_comments_replied_recently_post, total_users_comments_on_recently_post)

                all_en_users_replied_recently_post = get_all_en_users_replied_recently_post(
                    total_en_users_comments_on_recently_post, all_users_replied_recently_post)

                total_en_comment_each_en_posts.append(
                    len(all_en_comments_replied_recently_post))
                all_users_replied_en_comment_each_en_posts.append(
                    all_en_users_replied_recently_post)
                all_content_en_comment_each_en_posts.append(
                    all_en_comments_replied_recently_post)
                ESC(driver)

                END(driver)
            else:
                ESC(driver)

                END(driver)


def get_all_content_posts(driver, all_id_posts):
    all_content_posts = []
    for x in all_id_posts:
        END(driver)
        ele = driver.find_element_by_id(x)
        CLICK(driver, ele)

        soup = get_soup(driver)
        content_post = find(soup, "div", "class", "_5pbx userContent _3576")

        all_content_posts.append(get_text(content_post))

        ESC(driver)
        END(driver)
    return all_content_posts


def get_language_on_each_post(all_content_posts):

    language_on_each_post = []
    for x in all_content_posts:
        language_on_each_post.append(detect(x))
    return language_on_each_post


def get_all_en_things(language_on_each_post, en_posts, all_id_en_posts, all_id_posts, all_content_en_posts, all_content_posts, all_total_comments_each_en_post, all_total_comments_each_post):

    for x in range(len(language_on_each_post)):
        if language_on_each_post[x] == "en":
            en_posts.append(language_on_each_post[x])
            all_id_en_posts.append(all_id_posts[x])
            all_content_en_posts.append(all_content_posts[x])
            all_total_comments_each_en_post.append(
                all_total_comments_each_post[x])


def get_all_en_things_dict(all_id_en_posts, all_content_en_posts, all_total_comments_each_en_post, en_posts):

    all_en_posts_selected = []
    for x in range(len(all_id_en_posts)):
        comment = {}
        comment["id"] = all_id_en_posts[x]
        comment["content_post"] = all_content_en_posts[x]
        comment["contain_comment"] = all_total_comments_each_en_post[x]
        comment["lang"] = en_posts[x]
        all_en_posts_selected.append(comment)
    return all_en_posts_selected


def show_all_posts(driver):
    first_post = driver.find_elements_by_class_name("_6-e5")
    END(driver)
    last_post = driver.find_elements_by_class_name("_6-e5")

    while len(first_post) < len(last_post):
        first_post = driver.find_elements_by_class_name("_6-e5")
        END(driver)
        last_post = driver.find_elements_by_class_name("_6-e5")

    END(driver)


def get_all_id_posts(all_tag_div_contain_posts):

    all_id_posts = []
    for post in all_tag_div_contain_posts:
        all_id_posts.append(post.get('id'))

    return all_id_posts


def get_total_comment_each_posts(soup, all_id_posts, all_tag_a_contain_total_comments_each_post):

    find_which_post_have_comments = []
    all_total_comments_each_post = []

    for x in all_tag_a_contain_total_comments_each_post:
        find_which_post_have_comments.append(
            get_text(x))

    i = 0
    for x in all_id_posts:

        html_post = find(soup, "div", "id", x)
        html_content_post = get_text(html_post)

        check_post_have_comments = html_content_post.find("Comment")

        if check_post_have_comments != -1:
            all_total_comments_each_post.append(
                find_which_post_have_comments[i])
            i += 1
        else:
            all_total_comments_each_post.append('0')

    return all_total_comments_each_post


def get_text_from_html(tag_html):
    arr = []
    for x in tag_html:
        arr.append(get_text(x))
    return arr


def get_all_en_comments_replied_recently_post(all_comments_replied_recently_post):
    arr = []
    for x in all_comments_replied_recently_post:
        try:
            lang = detect(x)

            if lang == "en":
                arr.append(x)
        except Exception:
            pass
            continue
    return arr


def get_total_en_users_comments_on_recently_post(all_en_comments_replied_recently_post, total_users_comments_on_recently_post):
    arr = []
    m = ""
    for x in all_en_comments_replied_recently_post:
        if m == "":
            for y in total_users_comments_on_recently_post:
                if y.find(x) != -1:
                    arr.append(
                        y)
                    m = y
                    break
        else:
            for m in total_users_comments_on_recently_post:
                if m.find(x) != -1:
                    arr.append(
                        m)
                    m = m
                    break
    return arr


def get_all_en_users_replied_recently_post(total_en_users_comments_on_recently_post, all_users_replied_recently_post):
    arr = []
    m = ""
    for x in total_en_users_comments_on_recently_post:
        if m == "":
            for y in all_users_replied_recently_post:
                if x.find(y) != -1:
                    arr.append(y)
                    m = y
                    break

        else:
            for m in all_users_replied_recently_post:
                if x.find(m) != -1:
                    arr.append(
                        m)
                    m = m
                    break
    return arr
