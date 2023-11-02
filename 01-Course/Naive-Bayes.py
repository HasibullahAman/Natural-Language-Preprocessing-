from utils import process_tweet, lookup

def count_tweets(result,tweet,ys):
    for y, tweet in zip(ys, tweet):
        for word in process_tweet(tweet):
            pair = (word, y)


