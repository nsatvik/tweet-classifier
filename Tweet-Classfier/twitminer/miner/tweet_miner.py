import re
import math
from NLPlib import *
import random
import sys


class tweet_class:
    n = 0
    t_tags = {}
    t_words = {}
    def __init__(self,text):
	print 'Tweet Class : Politics or Sports'
	self.t_tags = {}
	self.t_words = {}
	self.add(text)
	self.n = 0

    def add(self, tweet_text):
	tags = re.findall(r'(#[^ ]+)',tweet_text)
	self.n += 1
	for tag in tags:
	    try:
        	self.t_tags[tag] += 1
	    except KeyError:
		self.t_tags[tag] = 1
	words = tweet_text.split(' ')
	for word in words:
	    try:
		self.t_words[word] += 1
	    except KeyError:
		self.t_words[word] = 1
    def check(self,tweet):
	tags = re.findall(r'(#[^ ]+)',tweet)
	res = 0
	for tag in tags:
	    try:
		if self.t_tags[tag]:
		    #res += self.t_tags[tag]#math.log10(float(1+self.t_tags[tag])/self.n)
		    return 9999999999
	    except KeyError:
		pass
	


	words = tweet.split()
	resw = 0
	for word in words:
	    try:
		resw += -math.log10(float(self.t_words[word])/float(1+self.n))
		
	    except:
		pass
	return res+resw
    def remove_word(self, words_list):
    	m = max(self.t_words.values())
	n = min(self.t_words.values())
	a = (m+n)/4
	for word in words_list:
	    try:
		if self.t_words[word]<a:
			del self.t_words[word]
	    except KeyError:
		pass
    def remove_tags(self, tags):
	for tag in tags:
	    try:
		del self.t_tags[tag]
	    except KeyError:
		pass
    def getWordsList(self):
	#print 'Words : ', self.t_words.keys()
	return self.t_words.keys()
    def getTagsList(self):
	return self.t_tags.keys()
    def output(self):
	print 'Tags : ',self.t_tags
	print 'Words: ',self.t_words

		
	



class tweet_classifier:
    classes = {} 
    def __init__(self):
	print 'This is the tweet classifier'

    def train(self, tweets):
	for tweet in tweets:
	    try:
		self.classes[tweet.get_class()].add(tweet.get_text())
	    except KeyError:
		self.classes[tweet.get_class()] = tweet_class(tweet.get_text())
    def stablize(self):
	cs = self.classes.keys()
	wrds = []
	wrds.append(self.classes[cs[0]].getWordsList())
	wrds.append(self.classes[cs[1]].getWordsList())
	common = []
	for w in wrds[0]:
		if w in wrds[1]:
			common.append(w)
	
	self.classes[cs[0]].remove_word(common)
	self.classes[cs[1]].remove_word(common)

	del wrds
	tgs = []
	tgs.append(self.classes[cs[0]].getTagsList())
	tgs.append(self.classes[cs[1]].getTagsList())
	del common
	common = []
	for t in tgs[0]:
	    if t in tgs[1]:
		common.append(t)
	
	print 'Common Tags : ',common
	self.classes[cs[0]].remove_word(common)
	self.classes[cs[1]].remove_word(common)




	#print 'Common Words Removed : ',common
	'''
	for i in range(len(cs)):
	    for j in range(i+1,len(cs)):
		prevlist = self.classes[cs[j]].getWordsList();
		self.classes[cs[j]].remove_word(self.classes[cs[i]].getWordsList())
		self.classes[cs[i]].remove_word(prevlist)
	'''


    
    def validate(self, tweets):
	for tweet in tweets:
	    vals = []
	    for cls in self.classes.keys():
		vals.append([self.classes[cls].check(tweet.get_text()),cls])
		#print tweet.get_text(),' ',vals[-1][0]
		
	    if vals[0][0] >= vals[1][0]:
		tweet.set_class(vals[0][1])
	    else:
		tweet.set_class(vals[1][1])
    
    def display_datastructures(self):
	cs = self.classes.keys()
	for c in cs:
	    print 'Class : ',c , ' ',self.classes[c].output()
	    print '-----------------------------------------------------'
	
	


class tweet:
    t_id = ''
    t_class = ''
    t_text = ''
    t_tags = []
    t_link = []
    t_users = []
    
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




def write_to_outputfile(tweets,file_path):
	f = open(file_path,'w')
	for tweet in tweets:
	    f.write(tweet.get_id_class())
	f.close()
	
	
	
	

	
def get_file_data(file_path):
    try:
	f = open(file_path)
    except IOError:
	print 'IOError: File Not found'
	return ''
    data = f.read().split('\n')
    del data[-1]
    f.close()
    return data


def main():
    print 'Welcome to Tweet Classifier'	
    if len(sys.argv)<3 :
	print 'Usage python tweet_miner.py [training_file_path/file_name] [validation file_path/file_name]'
    else:
	trainer_data = get_file_data(sys.argv[1])
	validator_data = get_file_data(sys.argv[2])
	training_tweets = []
	#print 'Training Data'
	for tweet_data in trainer_data:
	    training_tweets.append(tweet(tweet_data,0))
	    if training_tweets[-1].get_class() == 'Politics':
		print training_tweets[-1].get_text()

	validation_tweets = []
	#print 'Validation data'
	
	for tweet_data in validator_data:
	    validation_tweets.append(tweet(tweet_data,1))
	    #validation_tweets[-1].print_out();
	'''
	t_classifier = tweet_classifier()
	t_classifier.train(training_tweets)
	t_classifier.stablize()
	t_classifier.validate(validation_tweets)
	#t_classifier.display_datastructures()
	write_to_outputfile(validation_tweets,'outputfile.txt')
	'''

def test():
    tweets = get_file_data(sys.argv[1])
    posts = []
    sys.path.append('/home/nsatvik/twitminer/miner')
    print '1-Sports 2-Politics'
    tagger = NLPlib()
    for t in tweets:
	posts.append(tweet(t,1))
	print posts[-1].get_text()
	a = input('1 to display tags')
	if a==1:
	    words = tagger.tokenize(posts[-1].get_text())
	    tags = tagger.tag(words)
	    for i in range(len(words)):
		print words[i],' ',tags[i]

	else:
	    continue
    #write_to_outputfile(posts,'testoutput.txt')

if __name__ == '__main__':
    main()	

