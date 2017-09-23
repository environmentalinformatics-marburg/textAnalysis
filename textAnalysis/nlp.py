'''
This script tests some nlp.
'''

import jsonpickle
import nltk

# =====================================================================

def read_twitter_json(filepath):
    '''
    Read twitter tweets from json formatted file.
    '''
    tweets = []
    with open(filepath, "r") as f:
        for line in f:
            tweets.append(jsonpickle.decode(line))
    return(tweets)

# =====================================================================
# Example using "Gott"
if __name__ == '__main__':
    filepath = "C:/Users/tnauss/permanent/dvlp/textAnalysis/tweets_HJ_OR_HG.txt"
    tweets = read_twitter_json(filepath)

    print("Number of tweets:", len(tweets))

    tweets[1].keys()
    tweets[1]["text"]
    tweets[1]["user"]["name"]
    tweets[1]["user"]["id"]
    tweets[1]["user"]["location"]

    t1 = tweets[1]["text"]

    text = [t["text"] for t in tweets]
    
    tj = " ".join(text)
    
    tjt = nltk.word_tokenize(tj)
    tjtnt = nltk.Text(tjt)
    tjtnt .concordance("God")
    tjtnt .similar("God")
    tjtnt.common_contexts(["Harvey", "God"])
    tjtnt.dispersion_plot(["Harvey", "God", "Jesus", "Lord", "Trump"])

    sw = nltk.corpus.stopwords.words('english')
    tjts = [t for t in tjt if t not in sw]
    for t in tjts:
        porter.stem(t)

    porter = nltk.stem.porter.PorterStemmer()
    tjtslp = []
    for w in tjts:
        tjtslp.append(porter.stem(w))
    tjtslp[1]
    
    tjtslpnt = nltk.Text(tjtslp)
    tjtslpnt.concordance("God")

    # from nltk.stem.snowball import SnowballStemmer
    # from nltk.stem.wordnet import WordNetLemmatizer
    # porter = PorterStemmer()
    # snowball = SnowballStemmer('english')
    # wordnet = WordNetLemmatizer()
    # ...snowball.stem(word)
    # ...wordnet.lemmatize(word)
