'''
This script downloads twitter streams by keyword.
'''

import jsonpickle
import tweepy
from tweepy import OAuthHandler

# =====================================================================

def set_twitter_api():
    '''
    Set twitter api credentials and connect to api.
    '''
    
    consumer_key = "qJa6xBQDfc2uDmg4J5ffMaPkU"
    consumer_secret = "hO86KYvypa3SjMST8CKEIfK2VkrWBtWbEUuHq4RySeBHt0LD0m"
    access_token = "229765725-j1EagIXR6jrTEMKPv9LcjQ3idNZBkZAPRCzKueRS"
    access_token_secret = "Ors6Cq6LmSqjJz1q7dM6rsrj8iDO3y9HKzC2ZH8E8Un9k"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth) 
    
    return(api)



# =====================================================================

def retrieve_tweets(searchQuery, lat, lon, rad, lang = "en", filepath=None):
    '''
    Retrieve tweets by search term and location

    Script taken from "https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./"
    '''
    location = ",".join([lat, lon, rad])
    maxTweets = 10000000
    tweetsPerQry = 100
    sinceId = None
    
    max_id = -1
    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    with open(filepath, 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, geocode = location, lang = lang, count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery, geocode = location, lang = lang, count=tweetsPerQry,
                                            since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, geocode = location, lang = lang, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery, geocode = location, lang = lang, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, filepath))





# =====================================================================
# Example related to Harvey
if __name__ == '__main__':
    api = set_twitter_api()

    searchQuery = "(God) OR (Jesus) OR (Christ) OR (Gospel) OR (Worship) OR (Spirit) OR (Prayer) OR (Chruch) OR (Paptism) OR (Eucharist) OR (Sin) OR (Hell) OR (Devil) OR (Angels) OR (Miracle)"
    lat = "35.275145" 
    lon = "-80.872859"
    rad = "2000km"
    filepath = "C:/Users/tnauss/permanent/dvlp/textAnalysis/tweets_GJCGWHPCPESHDAM.txt"
    retrieve_tweets(searchQuery=searchQuery, lat=lat, lon=lon, rad=rad, filepath = filepath)

    tweets = []
    with open(filepath, "r") as f:
        for line in f:
            tweets.append(jsonpickle.decode(line))

    tweets[1].keys()
    tweets[1]["text"]
    tweets[1]["user"]["name"]
    tweets[1]["user"]["id"]
    tweets[1]["user"]["location"]

    for tweet in tweets:
        if tweet["lang"] == "de":
            print(tweet["text"])
    
    for tweet in tweets:
        if tweet["user"]["location"]:
            print(tweet["user"]["location"])
