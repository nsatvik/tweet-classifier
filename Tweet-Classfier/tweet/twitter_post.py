'''
Created on Mar 10, 2013

@author: Satvik
'''
import re
class Tweet:
    '''
    classdocs
    '''
    t_id = ''
    t_class = ''
    t_text = ''
    t_words = []
    t_tags = []
    t_link = []
    t_user_names = []
    
    def __init__(self,tweet_text,is_validation_data):
        if is_validation_data:
            info = re.search('([^ \t\n]+) ([^$]+)',tweet_text)
            self.t_class = 'Unknown'
        else:
            info = re.search('([^ \t\n]+) ([^ ]+) ([^$]+)',tweet_text)
            self.t_class = info.group(2)
    
        self.t_id =  info.group(1)
        if not(self.t_class =='Sports' or self.t_class =='Politics' or self.t_class == 'Unknown'):
            print 'Error Error'
        self.t_text = info.group(3-is_validation_data)
        self.extract_links()
        self.extract_tags()
        self.extract_words()
        self.extract_words()
        
        
    #Method to extract all the links in the tweet using regex    
    def extract_links(self):
        self.t_link = re.findall(r'(http:[^ ]+)',self.t_text)
    
    #Method to extract all the words in the tweet using regex
    def extract_words(self):
        self.t_words = re.findall(r'(\w+)',self.t_text.lower())
    
    #Method to extract all the usernames in the tweet using regex
    def extract_usernames(self):
        self.t_user_names = re.findall(r'(@[^ ]+)',self.t_text)
    #Method to extract all the tags in the tweet using regex
    def extract_tags(self):
        self.t_tags = re.findall(r'#([^ ]+)',self.t_text)
    #return the classification class.
    def get_class(self):
        return self.t_class
    
    def set_class(self, Class):
        self.t_class = Class

    def get_text(self):
        return self.t_text

    def print_out(self):
        print 'ID : ',self.t_id,' Text : ',self.t_text,' Class: ',self.t_class
    def get_id_class(self):
        return self.t_id+' '+self.t_class+'\n'

        