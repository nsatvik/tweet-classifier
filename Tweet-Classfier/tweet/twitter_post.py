'''
Created on Mar 10, 2013

@author: Satvik
'''
import re
#
#A class that indicates each twitter post.
#
#
class Tweet:
    t_id = '' #Indicates the ID of the tweet
    t_class = '' #Indicates the class of the tweet Politics or Sports or (Unknown for Validation/Test tweets)
    t_text = '' #The tweet text as it appears
    t_words = [] #Words that appear in the tweet text after removing usernames, tags, links.
    t_tags = [] # #Tags that appear in the tweet
    t_link = [] # Links that appear in the tweet. These are not used for training
    t_user_names = [] #Usernames in the tweet. These are not used.
    t_probability = 0.0
    def __init__(self,tweet_text,is_validation_data):
        #Check the type of data Validation/Training and extract the information
        if is_validation_data:
            info = re.search('([^ \t\n]+) ([^$]+)',tweet_text)
            self.t_class = 'Unknown'
        else:
            info = re.search('([^ \t\n]+) ([^ ]+) ([^$]+)',tweet_text)
            self.t_class = info.group(2)
    
        self.t_id =  info.group(1)
        if not(self.t_class =='Sports' or self.t_class =='Politics' or self.t_class == 'Unknown'):
            print 'Parse Error'
        self.t_text = info.group(3-is_validation_data)
        self.extract_links()
        self.extract_tags()
        self.extract_usernames()
        self.extract_words()
        self.remove_repeated_info()
    def remove_repeated_info(self):
        for user in self.t_user_names:
            if user in self.t_words:
                self.t_words.remove(user)
        '''
        for tag in self.t_tags:
            if tag in self.t_tags:
                self.t_tags.remove(tag)    
        '''
        
    #Method to extract all the links in the tweet using regex    
    def extract_links(self):
        self.t_link = re.findall(r'(http:[^ ]+)',self.t_text)
    
    #Method to extract all the words in the tweet using regex
    def extract_words(self):
        self.t_words = re.findall(r'(\w+)',self.t_text.lower())
    
    #Method to extract all the usernames in the tweet using regex
    def extract_usernames(self):
        self.t_user_names = re.findall(r'@([\w]+)',self.t_text.lower())
    #Method to extract all the tags in the tweet using regex
    def extract_tags(self):
        self.t_tags = re.findall(r'#([\w]+)',self.t_text.lower())
    #return the classification class.
    def get_class(self):
        return self.t_class
    
    #sets the class of the tweet to Class.
    def set_class(self, Class):
        self.t_class = Class
    
    #This method returns the tweet text
    def get_text(self):
        return self.t_text
    
    #this method returns the tags
    def get_tags(self):
        return self.t_tags
    #this method return words in the tweet text
    def get_words(self):
        return self.t_words
    def get_info_all(self):
        return self.t_id+' '+self.t_class+' '+self.t_text+'\n'
    #Used for outputting the tweet instance variables.(for Debugging) 
    def print_out(self):
        print 'Tags : ',self.t_tags,' words : ',self.t_words,' Usernames: ',self.t_user_names
    
    #Returns a string of the form 'ID tweet_class' (For writing to the file)    
    def get_id_class(self):
        return self.t_id+' '+self.t_class+'\n'
    def has_tags(self):
        return len(self.t_tags)>0
    def set_probability(self, p):
        self.t_probability = p

    def get_probability(self):
        return self.t_probability
        