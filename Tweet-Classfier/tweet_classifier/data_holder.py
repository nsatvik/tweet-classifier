'''
Created on Mar 10, 2013

@author: Satvik
'''
from tweet import twitter_post
import math

class Class_Specific_Data:
    tweet_class = '' #Name of the class the tweet belongs to 
    tweet_words = {}
    tweet_tags = {}
    tweet_pos = {}
    n = 0
    
    def __init__(self,classname):
        self.tweet_class = classname
        self.tweet_words = {}
        self.tweet_class = {}
        self.n = 0
    def add(self,tweet):
        self.n += 1
        for tag in tweet.get_tags():
            try:
                self.tweet_tags[tag] += 1
            except KeyError:
                self.tweet_tags[tag] = 1
        for word in tweet.get_words():
            try:
                self.tweet_words[word] += 1
            except KeyError:
                self.tweet_words[word] = 1
    def get_prob(self,word):
        probability = 0
        try:
            probability = -math.log10(float(self.tweet_words[word])/(1+self.n))
        except KeyError:
            pass
        return probability
    def get_prob_tag(self,tag):
        probability = 0
        try:
            probability = math.log10(float(self.tweet_tags[tag])/(1+self.n))
        except KeyError:
            pass
        return probability
        
    def classify(self,tweet):
        prob_tags = 0
        for tag in tweet.get_tags():
            prob_tags += self.get_prob_tag(tag)
        prob_words = 0
        for word in tweet.get_words():
            prob_words += self.get_prob(word)
               
        return prob_tags+prob_words
    
    def get_words_list(self):
        return self.tweet_words.keys()
    
    def remove_words(self,words):
        m = max(self.tweet_words.values())
        n = min(self.tweet_words.values())
        a = (m+n)/4
        for word in words:
            try:
                if self.tweet_words[word]<a:
                    del self.tweet_words[word]
            except KeyError:
                pass
            
    

class Tweet_Data_Store:
    '''
    classdocs
    '''
    tweet_classes = {} # This is a hash-map of class to Class_specific data

    def __init__(self,params):
        '''
        Constructor
        '''
        print 'Global Data Holder!'