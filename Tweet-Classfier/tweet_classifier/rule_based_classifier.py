'''
Created on Mar 10, 2013

@author: Satvik
'''
import data_holder
class RuleBasedClassifier(object):
    '''
    classdocs
    '''
    tweet_data_store = data_holder.Tweet_Data_Store()

    def __init__(self,params):
        '''
        Constructor
        '''
        print 'Rule Based Classifier Class cosn!'
    
    def train(self, tweets):
        for tweet in tweets:
            try:
                self.classes[tweet.get_class()].add(tweet.get_text())
            except KeyError:
                pass
                #self.classes[tweet.get_class()] = data_class(tweet.get_text())
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
