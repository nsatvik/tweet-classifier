
'''
Created on Mar 10, 2013

@author: Satvik
'''
import sys
import re
from tweet import twitter_post
from tweet_classifier import rule_based_classifier,Bayes_Classifier

def write_to_outputfile(tweets,file_path):
    f = open(file_path,'w')
    for tweet in tweets:
        f.write(tweet.get_id_class())
    f.close()
def write_to_file(tweets,file_path):
    f = open(file_path,'w')
    for tweet in tweets:
        f.write(tweet.get_info_all())
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
    if len(sys.argv)<4 :
        print 'Usage python tweet_miner.py [training_file_path/file_name] [validation file_path/file_name] [test file_path/file_name]'
        exit()
    
    trainer_data = get_file_data(sys.argv[1])
    validation_data = get_file_data(sys.argv[2])
    test_data = get_file_data(sys.argv[3])
    training_tweets = []
    
    for tweet_data in trainer_data:
        training_tweets.append(twitter_post.Tweet(tweet_data,0))
    validation_tweets = []    
    for tweet_data in validation_data:
        validation_tweets.append(twitter_post.Tweet(tweet_data,1))

    test_tweets = []
    for tweet_data in test_data:
        test_tweets.append(twitter_post.Tweet(tweet_data,1))
    
    print 'Training in Progress!' 
    nb_classifier = Bayes_Classifier.Naive_Bayes_Classifier()
    nb_classifier.train(training_tweets)
    print 'Validation in Progress...'
    nb_classifier.classify(validation_tweets)
    for v_tweet in validation_tweets:
        if v_tweet.get_probability()>=0.80:
            training_tweets.append(v_tweet)
    print 'Validation Training in Progress...'
    nb_classifier.train(training_tweets)
    print 'Testing in Progress...'
    nb_classifier.classify(test_tweets)
    write_to_outputfile(test_tweets,'test_outputfile.txt')
    print 'Output written to test_outputfile.txt'
    #nb_classifier.show_important_features(1000)
    

if __name__=='__main__':
    main()