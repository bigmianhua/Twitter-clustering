import tweepy
import re
import nltk
from nltk.corpus import brown
import time
import sys




#Do preprocessing and save the new file to saveFile_result	
def preprocessing(list):
	text = []
	for item in list:
	#delete with http
		pattern_http=re.compile(r'http[^\s]+\s|http[^\s]+\n')
		if pattern_http.findall(str(item))!=[]:
		#delete http and replace data
			item=pattern_http.sub(r'',item)
	#delete friend names
		pattern_friends=re.compile(r'RT @[^\s]+\s|RT @[^\s]+\n|RT @[^\s]+\:|@[^\s]+\S|@[^\s]+\s|@[^\s]+\n')
		if pattern_friends.findall(str(item))!=[]:
			item=pattern_friends.sub(r'',item)
	#deal with hashtag '#'	
	#delete hashtag in the newfile and save it in hashtag file
	#save the result 
		text.append(str(item))
	return text


# coding=UTF-8






def main():
	userfile = open('360user.txt','r')
	user_list = []
	for line in userfile:
		line = line.strip('\n')
		user_list.append(line)
	success = 0
	i=166
#Use your own key here for authorization
	access_token = '3930632915-XIWJCFKopCwGA8HNB7px117mlF4Qs787YI9WrxO'
	access_token_secret = 'ajUCKjABOnr4JynJ4YNzmhj1XFeu07ky5S45zq8CWMTJ2'
	consumer_key = 'yJFVGMlRcPE1FCtGYrmnjd3Jl'
	consumer_secret = 'VixQjpspjDZgRYwPMKXZ15ftOCve3gYpEiVaL1G5e4kVyoi0JI'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)


	for a in range(i-1,len(user_list)-1):
		screenname = str(user_list[i-1])
		print screenname
		new_file = open('%d.txt'%(i), 'w')
		original_text = []
		preprocessed = []
		count = 0
		for tweet in tweepy.Cursor(api.user_timeline,id=screenname).items():
			if count < 90:
				original_text.append(tweet.text.encode("ascii", "ignore"))
				count = count + 1
			else:
				break
		preprocessed = preprocessing(original_text)	
		for line in preprocessed:
			new_file.write(line)
		i = i + 1
		success = success+1
		if success == 35:
			time.sleep(15*60)
			success=0






if __name__ == '__main__':
	main()
