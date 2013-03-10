'''
Created on Mar 10, 2013

@author: Satvik
'''
class Class_Specific_Data:
    tweet_class = '' #Name of the class the tweet belongs to 
    tweet_words = {}
    tweet_tags = {}
    tweet_pos = {}
    
    def __init__(self):
        self.tweet_class = 'Unknown'
        self.tweet_words = {}
        self.tweet_class = {}

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