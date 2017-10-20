import tweepy, auth
from textblob import TextBlob

# Step 1 - Authenticate

authent = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
authent.set_access_token(auth.access_token, auth.access_token_secret)

api = tweepy.API(authent)

#Step 3 - Retrieve Tweets
trends1 = api.trends_place(2295411) #WOEID for Mumbai
data = trends1[0]
trends = data['trends']
names = [trend['name'] for trend in trends]


for trend in names:
    print(trend)
    m=1
    public_tweets = api.search(q=trend)
    m=m+1
    n=1
    for tweet in public_tweets:
        print(n)
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        print("")
        n=n+1
    if m == 11:     #Specifying that we want the top ten trends
        break
