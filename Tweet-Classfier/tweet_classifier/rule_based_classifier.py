'''
Created on Mar 10, 2013

@author: Satvik
'''
from data_holder import Class_Specific_Data
from tweet_classifier.data_holder import Data_Store_RuleBsdClassifier

class RuleBasedClassifier(object):
    '''
    classdocs
    '''
    tweet_classes = {} #Dictionary to map class to class_specific data

    def __init__(self):
        '''
        Constructor
        '''
        #print 'Rule Based Classifier Class cosn!'
    
    def train(self, tweets):
        for tweet in tweets:
            try:
                self.tweet_classes[tweet.get_class()].add(tweet)
            except KeyError:
                pass
                self.tweet_classes[tweet.get_class()] = Data_Store_RuleBsdClassifier(tweet.get_class())
                
    def stablize(self):
        cs = self.tweet_classes.keys()
        wrds = []
        wrds.append(self.tweet_classes[cs[0]].get_words_list())
        wrds.append(self.tweet_classes[cs[1]].get_words_list())
        common = []
        for w in wrds[0]:
            if w in wrds[1]:
                common.append(w)
    
        self.tweet_classes[cs[0]].remove_words(common)
        self.tweet_classes[cs[1]].remove_words(common)

        del wrds
        '''
        tgs = []
        tgs.append(self.tweet_classes[cs[0]].getTagsList())
        tgs.append(self.tweet_classes[cs[1]].getTagsList())
        del common
        common = []
        for t in tgs[0]:
            if t in tgs[1]:
                common.append(t)
    
        print 'Common Tags : ',common
        self.tweet_classes[cs[0]].remove_words(common)
        self.tweet_classes[cs[1]].remove_words(common)
        '''




    #print 'Common Words Removed : ',common
    def display_tags(self):
        return dict([(c,self.tweet_classes[c].get_tags()) for c in self.tweet_classes.keys()])
    '''
    Method used to Validate the tweets
    '''
    def validate(self, tweets):
        for tweet in tweets:
            vals = []
            for cls in self.tweet_classes.keys():
                vals.append([self.tweet_classes[cls].classify(tweet),cls])
        #print tweet.get_text(),' ',vals[-1][0]
        
            if vals[0][0] >= vals[1][0]:
                tweet.set_class(vals[0][1])
            else:
                tweet.set_class(vals[1][1])
    '''
    This method is used to display the underlying datastructures while debugging.
    '''
    def display_datastructures(self):
        cs = self.tweet_classes.keys()
        for c in cs:
            print 'Class : ',c , ' ',self.classes[c].output()
            print '-----------------------------------------------------'
