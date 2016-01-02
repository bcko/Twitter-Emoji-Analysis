import os
import re

class Tweet:
	def __init__(self, user, tweets):
		self.user = user
		self.tweets = tweets
	# percent of message that have emoticon per user.
	def stats(self, unicodeEmojiList):
		print("user id, number of tweets, minimum number of tweets, 
		print("user id : " + self.user)
		print("number of tweets : " + str(len(self.tweets)))
		print("minimum number of tweets : " + str(len(min(self.tweets, key=len))))
		print("maximum number of tweets : " + str(len(max(self.tweets, key=len))))

	def unicodeStats(self, unicodeEmojiList):
		emojiCount = 0
		for unicodeEmoji in unicodeEmojiList:
			emojiCount += self.tweets.count(unicodeEmoji.emoji)		
		print(emojiCount)

class UnicodeEmoji:
	def __init__(self, emoji, descr, unicodeType):
		self.emoji = emoji
		self.descr = descr
		self.unicodeType = unicodeType

def readTweets(directory):
	tweet_list = []
	for file in os.listdir(directory):
		infile = open(directory + "/" + file)
		corpus = infile.read()
		infile.close()
		pattern = r"<Text_Begin> (.*) <Text_End>"
		result = re.findall(pattern, corpus)
		tweet_list.append(Tweet(file, result))
	return tweet_list	

def readUnicode(directory):
	unicodeList = []
	for file in os.listdir(directory):
		infile = open(directory + "/" + file)
		for line in infile:
			line = line.rstrip("\n")
			line = line.lstrip(" ")
			lineList = line.split(' ', 1)
			unicodeList.append(UnicodeEmoji(lineList[0], lineList[1], file))
	return unicodeList

def countUnicode(unicodeEmojiList, tweetList):
	pass

def main():
	# directory names
	dirTop = os.getcwd()
	dirTweet = dirTop + "/Tweets"
	dirAnalysis = dirTop + "/Analysis"
	dirEmoji = dirTop + "/Emoji"

	# create a list of tweets
	koreanTweetsList = readTweets(dirTweet + "/Korea")
	"""	
	japanTweetsList = readTweets(dirTweet + "/Japan")
	usTweetsList = readTweets(dirTweet + "/US")
	canadaTweetsList = readTweets(dirTweet + "/Canada")
	"""	
	unicodeEmojiList = readUnicode(dirEmoji + "/Unicode")
	print(koreanTweetsList.stats(unicodeEmojiList))



main()
