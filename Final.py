import tweepy
import nltk
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 to

API_key = 'Ekv1hRgtxK5XvVbV9xYCnSYpd'
API_secret = 'ETZg4Arr01QPggCfkK0KxD0ZL5kCC3GkIRkqHLbslZpoh2vGdM'
access_token = '1777612444514316288-ww2LMzF47PIUnwPje8oJOZaTsoDTf5'
access_token_secret = 'wa4vp1wRGX3yKJkpvNB4io4OepoLDDn02JFisxTR4p0ci'


authentication = tweepy.OAuthHandler(API_key, API_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)


def p_text(text):
    text = text.lower()
    word_tokenize(text)


def remove_stopwords(tokens):
    file_tokens = []
    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)
    return ' '.join(file_tokens)


def analyze_sentiment(cleaned_tweets):
    return [SentimentIntensityAnalyzer().polarity_scores(tweet)['compound'] for tweet in cleaned_tweets]


def plot_sent_distribution(sentiments):
    plt.hist(sentiments, bins=10, color='red', edgecolor='black')
    plt.xlabel('Score')
    plt.ylabel('label')
    plt.show()


def main():
    search_query = "#coding"
    tweets = api.search(q=search_query, count=50)

    if tweets is not None:
        try:

            cleaned_tweets = [preprocess_text(tweet.text) for tweet in tweets]

            sentiments = analyze_sentiment(cleaned_tweets)

            plot_sentiment_distribution(sentiments)
        except Exception as e:
            print("Error occurred:", e)
    else:
        print("No tweets found")


if __name__ == "__main__":
    main()