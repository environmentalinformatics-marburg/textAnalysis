'''
This script performs an unsupervised clustering of Dressler (2007).
'''

import gensim
import jsonpickle
import nltk
import pyLDAvis.gensim
import re
import string

if __name__ == '__main__':
    filepath = "C:/Users/tnauss/permanent/dvlp/textAnalysis/dressler_2007.txt"
    
    with open(filepath, "r") as f:
       d = f.read()
    
    # Tokenize text
    d = d.split(".")
    d = [word.split() for word in d]
    d = [[word.lower() for word in sentence] for sentence in d]
    
    tknzr = nltk.tokenize.word_tokenize
    for i in range(len(d)):
        d[i] = tknzr.tokenize(d[i])
    len(d)
    len(set([word for sentence in d for word in sentence]))
    d[1]
    d_sw[1]    

    # Remove stopwords
    sw = nltk.corpus.stopwords.words('german')
    d_sw = [[word for word in sentence if word not in sw] for sentence in d]
    nltk.FreqDist([word for sentence in d_sw for word in sentence])

    # Lemmatize
    porter = nltk.stem.porter.PorterStemmer()
    d_sw_lm = [[porter.stem(word) for word in sentence] for sentence in d_sw]
    len(d_sw_lm )
    len(set([word for sentence in d_sw_lm for word in sentence]))
    nltk.FreqDist([word for sentence in d_sw_lm for word in sentence])
    
    # Exclude punctuation
    ep = set(string.punctuation) 
    d_sw_lm_ep = [[word for word in sentence if word not in ep] for sentence in d_sw_lm]
    len(d_sw_lm_ep )
    len(set([word for sentence in d_sw_lm_ep for word in sentence]))
    nltk.FreqDist([word for sentence in d_sw_lm_ep for word in sentence])

    # Exclude numbers
    d_sw_lm_ep_edig =  [[word for word in sentence if not word.isnumeric()] for sentence in d_sw_lm_ep]
    len(set([word for sentence in d_sw_lm_ep for word in sentence]))
    nltk.FreqDist([word for sentence in d_sw_lm_ep for word in sentence])
        
    # Create dictionary
    d_clean = d_sw_lm_ep_edig  
    dict = gensim.corpora.Dictionary(d_clean)
    len(dict)
    
    # Filter out words extreme frequencies of words.
    dict.filter_extremes(no_below=0.2, no_above=0.5)
    len(dict)
    print(dict)    
    
    # Create corpus
    corpus = [dict.doc2bow(sentence) for sentence in d_clean]

    # Compute lda
    num_topics = 3
    chunksize = 2000
    passes = 20
    iterations = 400
    eval_every = None  # Don't evaluate model perplexity, takes too much time.
    id2word = dict
    d_model = gensim.models.LdaModel(corpus=corpus, id2word=id2word, chunksize=chunksize,
                                     alpha='auto', eta='auto', 
                                     iterations=iterations, num_topics=num_topics, 
                                     passes=passes, eval_every=eval_every)
    d_model 
    d_model.top_topics(corpus, num_words=3)

    d_top_topics = d_model.top_topics(corpus, num_words=5)
    
    d_info = pyLDAvis.gensim.prepare(d_model, corpus, dict)
    pyLDAvis.save_html(d_info, "C:/Users/tnauss/permanent/dvlp/textAnalysis/d.html")
    