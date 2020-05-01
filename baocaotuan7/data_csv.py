import pandas as pd


def write_all_posts_and_comments(all_id_en_posts, all_content_en_posts,  total_en_comment_each_en_posts, all_users_replied_en_comment_each_en_posts, all_content_en_comment_each_en_posts, sentiment_all_en_comments):

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

    for x in range(len(all_users_replied_en_comment_each_en_posts)):
        if all_users_replied_en_comment_each_en_posts[x]:
            file_name = "id_user_comment_{}.csv".format(x)
            df = pd.DataFrame(
                {'Id': all_id_en_posts_to_csv[x], 'Users': all_users_replied_en_comment_each_en_posts[x], 'Comments': all_content_en_comment_each_en_posts[x], 'Sentiment': sentiment_all_en_comments[x]})
            df.to_csv(file_name, index=True, encoding='utf-8')
