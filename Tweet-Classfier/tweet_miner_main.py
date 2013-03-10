'''
Created on Mar 10, 2013

@author: Satvik
'''
import sys
import re
from tweet import twitter_post
import tweet_classifier

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
        exit()
    data = f.read().split('\n')
    del data[-1]
    f.close()
    return data


def main():
    print 'Welcome to Tweet Classifier'    
    if len(sys.argv)<3 :
        print 'Usage python tweet_miner.py [training_file_path/file_name] [validation file_path/file_name]'
    
    trainer_data = get_file_data(sys.argv[1])
    validation_data = get_file_data(sys.argv[2])
    training_tweets = []
    #print 'Training Data'
    for tweet_data in trainer_data:
        training_tweets.append(twitter_post.Tweet(tweet_data,0))

    validation_tweets = []    
    for tweet_data in validation_data:
        validation_tweets.append(twitter_post.Tweet(tweet_data,1))
        #validation_tweets[-1].print_out();
    '''
    t_classifier = tweet_classifier()
    t_classifier.train(training_tweets)
    t_classifier.stablize()
    t_classifier.validate(validation_tweets)
    #t_classifier.display_datastructures()
    write_to_outputfile(validation_tweets,'outputfile.txt')
    '''


if __name__=='__main__':
    main()