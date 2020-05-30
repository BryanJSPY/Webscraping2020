import random
import string
import re
import pandas as pd
import time

from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import twitter_samples, stopwords
from nltk.stem.wordnet import WordNetLemmatizer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from langdetect import detect
from bs4 import BeautifulSoup


class ScrapingFacebook:
    def setUp(self):
        self.driver = driver = webdriver.Chrome(
            ChromeDriverManager().install())


# init driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")

# login fb
driver.find_element_by_id("email").send_keys("dct99002@gmail.com")
driver.find_element_by_id("pass").send_keys("vmax21399")
driver.find_element_by_id("u_0_b").click()

# turn off popup
wait = WebDriverWait(driver, 10)
wait_popup = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3ixn")))
driver.find_element_by_class_name("_3ixn").click()

# enter keyword to search
wait_search_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]")))

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]").send_keys(
    "ncovid19")

# click button search
wait_search_btn = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button")))
driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button').click()

# click Post tag
wait_pos_tag = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a")))
if wait_pos_tag:
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]/a").click()


# click Your Groups and Pages
    time.sleep(3)
    driver.find_element_by_link_text(
        "Your Groups and Pages").click()

# show all posts in the page
first_post = driver.find_elements_by_class_name("_6-e5")
time.sleep(3)
action = ActionChains(driver)
action.key_down(Keys.END)
action.key_down(Keys.END)
action.perform()
last_post = driver.find_elements_by_class_name("_6-e5")

while len(first_post) < len(last_post):
    first_post = driver.find_elements_by_class_name("_6-e5")
    time.sleep(3)
    action = ActionChains(driver)
    action.key_down(Keys.END)
    action.key_down(Keys.END)
    action.perform()
    last_post = driver.find_elements_by_class_name("_6-e5")

time.sleep(3)
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
total_posts = soup.find_all("div", {"class": "_6-e5"})

total_id = []
for x in total_posts:
    total_id.append(x.get('id'))

# print(total_id)

total_posts_contain_comment = soup.find_all(
    "a", {"class": "_3hg- _42ft"})
total_comments_each_post_contain_comments = []
for x in total_posts_contain_comment:
    total_comments_each_post_contain_comments.append(x.get_text())

# print(total_comments_each_post_contain_comments)
total_comments_each_post = []
content_posts = []
lang_content = []
i = 0

time.sleep(3)
actions = ActionChains(driver)
actions.key_down(Keys.HOME)
actions.key_up(Keys.HOME)
actions.perform()

for x in total_id:

    time.sleep(1)
    ele = driver.find_element_by_id(x)
    action = ActionChains(driver)
    action.move_to_element(ele)
    action.click(ele)
    action.perform()

    time.sleep(3)
    actions = ActionChains(driver)
    actions.key_down(Keys.END)
    actions.key_up(Keys.END)
    actions.perform()

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    html_post_content = soup.find(
        "div", {"class": "_5pbx userContent _3576"}).get_text()
    content_posts.append(html_post_content)
    lang_content.append(detect(html_post_content))

    html_comment = soup.find("div", {"class": "_4vn1"}).get_text()
    check_comment = html_comment.find("Comment")

    if check_comment != -1:
        total_comments_each_post.append(
            total_comments_each_post_contain_comments[i])
        i += 1
    else:
        total_comments_each_post.append('0')

    time.sleep(1)
    action = ActionChains(driver)
    action.key_down(Keys.ESCAPE)
    action.key_down(Keys.ESCAPE)
    action.perform()

    time.sleep(1)
    action = ActionChains(driver)
    action.key_down(Keys.END)
    action.key_down(Keys.END)
    action.perform()

print(total_comments_each_post)
print(content_posts)
print(lang_content)

time.sleep(3)
actions = ActionChains(driver)
actions.key_down(Keys.HOME)
actions.key_up(Keys.HOME)
actions.perform()

# filter eng posts

en_total_id = []
en_content = []
en_post_have_comment = []

print(total_comments_each_post)

for x in range(len(lang_content)):
    if lang_content[x] == 'en':
        en_total_id.append(total_id[x])
        en_content.append(content_posts[x])
        en_post_have_comment.append(total_comments_each_post[x])

# print(en_total_id)
# print(en_content)
# print(en_post_have_comment)

time.sleep(3)
actions = ActionChains(driver)
actions.key_down(Keys.HOME)
actions.key_up(Keys.HOME)
actions.perform()

en_content_comments_each_posts = []
en_total_comments = []
for x in range(len(en_total_id)):
    time.sleep(3)
    ele = driver.find_element_by_id(en_total_id[x])
    ele.click()

    if en_post_have_comment[x] != "0":

        time.sleep(1)
        actions = ActionChains(driver)
        actions.key_down(Keys.END)
        actions.key_up(Keys.END)
        actions.perform()

        wait_ele = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4vn1")))

        if wait_ele:
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
                    time.sleep(3)
                    driver.find_element_by_partial_link_text("View").click()

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
                    time.sleep(3)
                    ele = driver.find_element_by_class_name("_4sso _4ssp")
                    actions = ActionChains(driver)
                    actions.move_to_element(ele)
                    actions.click(ele)
                    actions.perform()

                    time.sleep(1)
                    actions = ActionChains(driver)
                    actions.key_down(Keys.END)
                    actions.key_up(Keys.END)
                    actions.perform()
                except Exception:
                    pass
                    break

            comments = []
            content = driver.page_source
            soup = BeautifulSoup(content, "html.parser")
            html_content_comments = soup.find_all("span", {"class": "_3l3x"})

            for x in html_content_comments:
                comments.append(x.get_text())

            en_comment = []
            count_en_comments = 0
            for x in comments:
                try:
                    if detect(x) == 'en':
                        en_comment.append(x)
                        count_en_comments += 1
                except Exception:
                    pass
                    continue

    en_content_comments_each_posts.append(en_comment)
    en_total_comments.append(count_en_comments)
    time.sleep(1)
    actions = ActionChains(driver)
    actions.key_down(Keys.ESCAPE)
    actions.key_up(Keys.ESCAPE)
    actions.perform()

# print(en_content_comments_each_posts)

time.sleep(5)
# shutdow
# driver.quit()

sentiment_total_en_comments = []


def remove_noise(tweet_tokens, stop_words=()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):

    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):

    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


stop_words = stopwords.words('english')

positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []

for tokens in positive_tweet_tokens:
    positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

for tokens in negative_tweet_tokens:
    negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

positive_tokens_for_model = get_tweets_for_model(
    positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(
    negative_cleaned_tokens_list)

positive_dataset = [(tweet_dict, "Positive")
                    for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                    for tweet_dict in negative_tokens_for_model]

dataset = positive_dataset + negative_dataset

random.shuffle(dataset)

train_data = dataset[0:len(dataset)]

classifier = NaiveBayesClassifier.train(train_data)

for x in en_content_comments_each_posts:
    sentiment_temp = []
    for y in x:
        comment_tokens = remove_noise(word_tokenize(y))
        print(y, classifier.classify(
            dict([token, True] for token in comment_tokens)))
        sentiment_temp.append((classifier.classify(
            dict([token, True] for token in comment_tokens))))
    sentiment_total_en_comments.append(sentiment_temp)

sentiment_en_content = []
for x in en_content:
    comment_tokens = remove_noise(word_tokenize(x))
    sentiment_en_content.append((classifier.classify(
        dict([token, True] for token in comment_tokens))))

print(sentiment_total_en_comments)
print(sentiment_en_content)

df = pd.DataFrame(
    {'Id': en_total_id, 'Post': en_content, "Sentiment": sentiment_en_content})
df.to_csv('fb_scraping.csv', index=False, encoding='utf-8')

duplicate_en_total_id = []

i = 0
for x in en_total_comments:
    temp = []
    if x:
        for y in range(x):
            temp.append(en_total_id[i])
    i += 1
    duplicate_en_total_id.append(temp)

i = 0
for x in en_total_comments:
    if x:
        file_name = "{}_en_comments.csv".format(en_total_id[i])
        df = pd.DataFrame(
            {'Id': duplicate_en_total_id[i], "Comments": en_content_comments_each_posts[i], "Sentiment": sentiment_total_en_comments[i]})
        df.to_csv(file_name, index=False, encoding='utf-8')
    i += 1
