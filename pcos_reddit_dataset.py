import pandas as pd
import praw
import reddit_secrets_praw as praw


def get_subreddit_df(subreddit_name):
    reddit = praw.Reddit(client_id=secrets['client_id '],
                         client_secret=secrets['client_secret'],
                         user_agent=secrets['user_agent'])
    subreddit = reddit.subreddit(subreddit_name)

    pcos_dict = {"title": [],
                 "subreddit": [],
                 "score": [],
                 "id": [],
                 "url": [],
                 "comms_num": [],
                 "created": [],
                 "body": [],
                 "flair": [],
                 "post_type": []}

    hot_posts = subreddit.hot(limit=4000)
    new_posts = subreddit.new(limit=4000)
    top_posts = subreddit.top(limit=4000)
    rising_posts = subreddit.rising(limit=4000)

    post_types = [hot_posts, new_posts, top_posts, rising_posts]

    for post_kind in post_types:
        for submission in post_kind:
            pcos_dict["title"].append(submission.title)
            pcos_dict['subreddit'].append(submission.subreddit)
            pcos_dict["score"].append(submission.score)
            pcos_dict["id"].append(submission.id)
            pcos_dict["url"].append(submission.url)
            pcos_dict["comms_num"].append(submission.num_comments)
            pcos_dict["created"].append(submission.created)
            pcos_dict["body"].append(submission.selftext)
            pcos_dict['flair'].append(submission.link_flair_text)
            pcos_dict['post_type'].append('new')

    subreddit_df = pd.DataFrame(pcos_dict)

    return subreddit_df

def concat_subreddits():
    pcos_df = get_subreddit_df('PCOS')
    pcosrecipes_df = get_subreddit_df('PCOSRECIPES')
    pcosloseit_df = get_subreddit_df('PCOSloseit')
    pcoscico_df = get_subreddit_df('PCOS_CICO')
    pcospregnant_df = get_subreddit_df('PCOSandPregnant')
    ttc_df = get_subreddit_df('TTC_PCOS')
    lean_df = get_subreddit_df('LeanPCOS')
    folks_df = get_subreddit_df('PCOS_Folks')

    full_df = pd.concat(
        [pcos_df, pcosrecipes_df, pcosloseit_df, pcoscico_df, pcospregnant_df, ttc_df, lean_df, folks_df], axis=0,
        ignore_index=True)

    return full_df

def total_reddit_pcos(): #running this a dew times every few days would continue adding to the dataset
    df = pd.read_csv('all_pcos_subreddits.csv')
    new_data = concat_subreddits()
    concat_dfs = pd.concat([df, new_data], axis = 0, ignore_index = True).drop_duplicates()
    concat_dfs.to_csv('all_pcos_subreddits.csv')
    return concat_dfs
