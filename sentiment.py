import numpy as np
import time
import numpy
import re

def readSentimentList(file_name):
    ifile = open(file_name, 'r')
    happy_log_probs = {}
    sad_log_probs = {}
    ifile.readline() #Ignore title row
    
    for line in ifile:
        tokens = line[:-1].split(',')
        happy_log_probs[tokens[0]] = float(tokens[1])
        sad_log_probs[tokens[0]] = float(tokens[2])

    return happy_log_probs, sad_log_probs

def classifySentiment(words, happy_log_probs, sad_log_probs):
    # Get the log-probability of each word under each sentiment
    happy_probs = [happy_log_probs[word] for word in words if word in happy_log_probs]
    sad_probs = [sad_log_probs[word] for word in words if word in sad_log_probs]
    # Sum all the log-probabilities for each sentiment to get a log-probability for the whole tweet
    tweet_happy_log_prob = np.sum(happy_probs)/100
    tweet_sad_log_prob = np.sum(sad_probs)/100
    print(tweet_happy_log_prob, tweet_sad_log_prob)
    # Calculate the probability of the tweet belonging to each sentiment
    prob_happy = np.reciprocal(np.exp(tweet_sad_log_prob - tweet_happy_log_prob) + 1)
    prob_sad = 1 - prob_happy

    return prob_happy, prob_sad

def main():
    happy_log_probs, sad_log_probs = readSentimentList('twitter_sentiment_list.csv')
    for i in range(166,351):
        f = open('file/file_%d.txt'%(int(i)),'r')
        line = f.readlines()
        words = line[0].split(' ')
        tweet_happy_prob, tweet_sad_prob = classifySentiment(words, happy_log_probs, sad_log_probs)
        print(tweet_happy_prob, tweet_sad_prob)
        if tweet_happy_prob > 0.9:
            filename = open('0.9/sentiment_%d.txt'%(int(i)), 'w')
            filename.write(str(line))
        elif 0.8<tweet_happy_prob <=0.9:
            filename = open('0.8_0.9/sentiment_%d.txt'%(int(i)), 'w')
            filename.write(str(line))
        elif 0<tweet_happy_prob <=0.8:
            filename = open('0_0.8/sentiment_%d.txt'%(int(i)), 'w')
            filename.write(str(line))

  
            
if __name__ == '__main__':
    main()
