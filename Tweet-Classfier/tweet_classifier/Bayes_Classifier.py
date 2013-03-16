'''
Created on Mar 10, 2013

@author: Satvik
'''
from nltk.classify import NaiveBayesClassifier,PositiveNaiveBayesClassifier
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords
class Naive_Bayes_Classifier(object):
    '''
    classdocs
    '''
    nb_classifier = None
    tag_map = {}
    common_tags = []
    def __init__(self):
        '''
        Constructor
        '''
        self.tag_map['Politics'] = []
        self.tag_map['Sports'] = []
        self.common_tags = []
        
        
        
    def bag_of_words(self,words):
        return dict([(word,True) for word in words])
    def bag_of_words_not_in_the_set(self,words,badwords):
        return self.bag_of_words(set(words)-set(badwords))
    def bag_of_non_stopwords(self,words,stopfile='english'):
        badwords = stopwords.words(stopfile)
        return self.bag_of_words_not_in_the_set(words, badwords)
    
    def get_bag_of_non_stop_bigram_words(self,tweet):
        words = tweet.get_words()
        bigram_finder = BigramCollocationFinder.from_words(words, 2)
        #trigram_finder = BigramCollocationFinder.from_words(words, 4)
        bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq,200)
        #trigrams = trigram_finder.nbest(BigramAssocMeasures.chi_sq,200)
        return self.bag_of_non_stopwords(words+bigrams)
        
    
    def show_important_features(self,n=30):
        return self.nb_classifier.show_most_informative_features(n) 
        
        
    def add_tag(self,tweet):
        tags = tweet.get_tags()
        c = tweet.get_class()
        for tag in tags:          
            if tag not in self.tag_map[c]:
                self.tag_map[c].append(tag)
         
    def train(self,tweets):
        train_set = []
        
        for tweet in tweets:
            features_dic = self.get_bag_of_non_stop_bigram_words(tweet)
            if tweet.has_tags():
                self.add_tag(tweet)
                              
            train_set.append((features_dic,tweet.get_class()))
        sprts_tags = self.tag_map['Sports']
        for tag in self.tag_map['Politics']:
            if tag in sprts_tags:
                self.common_tags.append(tag)
            
        #print 'Common Tags: ',self.common_tags    
        self.nb_classifier = NaiveBayesClassifier.train(train_set)
        
    def classify(self,tweets):
        
        for tweet in tweets:
            found = False
            if tweet.has_tags():
                for cls in self.tag_map.keys():
                    for tag in tweet.get_tags():
                        if tag in self.common_tags:
                            continue
                        if tag in self.tag_map[cls]:
                            tweet.set_class(cls)
                            tweet.set_probability(1)
                            found = True
                            break                
            if not found:                
                feature_set = self.get_bag_of_non_stop_bigram_words(tweet)
                probs = self.nb_classifier.prob_classify(feature_set)
                tweet.set_class(probs.max())
                tweet.set_probability(probs.prob(probs.max()))
                if probs.prob(probs.max())>0.75:
                    self.add_tag(tweet)