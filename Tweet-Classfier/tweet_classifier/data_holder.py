'''
Created on Mar 10, 2013

@author: Satvik
'''

import math

#This class holds the class specific data for all the tweets.
class Class_Specific_Data:
    tweet_class = '' #Name of the class all the tweet belongs to 
    tweet_words = {} #All the words that appear in tweet classified as tweet_class.
    tweet_tags = {} #All the tags that appear for a particular tweet_class
    tweet_pos = {} #Pos tags to word mapping.
    n = 0 #Total no. of tweets that belong to the tweet_class.
    
    def __init__(self,classname):
        self.tweet_class = classname
        self.tweet_words = {}
        self.tweet_class = {}
        self.n = 0
    
    #Add the tweet to the maintained instance variables and increment their corresponding count.
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
    #Returns the list of words that appear for a particular tweet_class.
    def get_words_list(self):
        return self.tweet_words.keys()

#This class inherits from the Class_Specific_Data class and implements 
#a few extra methods for using the Rule Based Classifier.
class Data_Store_RuleBsdClassifier(Class_Specific_Data):
    def __init__(self,class_label):
        self.tweet_class = class_label
    
    #Returns the probability    
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
    def get_tags(self):
        return self.tweet_tags.keys()
    
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
