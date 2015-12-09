import re
from collections import defaultdict
import statistics


class Tweet:
	def __init__(self, regex_split):
		self.user = regex_split[0]
		self.text = regex_split[1]

def make_emoji_list(filename):
	infile = open(filename)
	emoji_string = infile.read()
	infile.close()
	emoji_list = []
	for emoji in emoji_string:
		emoji_list.append(emoji)
	emoji_list.pop()
	return emoji_list
	
def read_tweets(filename):
	infile = open(filename)
	corpus = infile.read()
	infile.close()
	
	pattern = r"<Text_Begin ID=([a-zA-Z0-9_]+)>(.*)<Text_End>"
	result = re.findall(pattern, corpus)
	
	tweets = []
	for r in result:
		tweets.append(Tweet(r))
	return tweets	
	
def read_user_id(filename):
	infile = open(filename)
	user_id_list = []
	for user_id in infile:
		user_id_list.append(user_id.rstrip('\n'))		
	infile.close()
	return user_id_list	



def print_stats(tweets, emoji_list):
	tweet_count = 0
	word_count = 0
	emoji_count = 0
	users = defaultdict(int)
	vocab = defaultdict(int)
	
	
	
	for tweet in tweets:
		tweet_count += 1
		users[tweet.user]+=1
		clean_text = re.sub("[\.,]", " ", tweet.text)
		for word in clean_text.split():
			vocab[word] +=1
			word_count += 1
			
		for emoji in emoji_list:
			str_tweet = str(tweet.text)
			#print(str_tweet.count(emoji))
			emoji_count += str_tweet.count(emoji)
	
	print("Num tweets", tweet_count)
	print("Num Users", len(users))
	print("Max tweets/user", max(users.values()))
	print("Average tweets/user", sum(users.values())/ float(len(users)))
	print("Min tweets/user", min(users.values()))
	print("Median tweets", statistics.median(users.values()) )
	print("Total emoji count", emoji_count)

def emoji_test():
	emoji_list = make_emoji_list("Emoji/emoji.txt")
	
	emoji_str = ""
	emoji_count = 0
	for emoji in emoji_list:
		emoji_str +=emoji
		
	for emoji in emoji_list:
		print(emoji_str.count(emoji))


def main():
	emoji_list = make_emoji_list("Emoji/emoji.txt")
	
	# "Japan_id.txt" "US_id.txt" "Korea_id.txt"
	user_id_list = read_user_id("Screen_name/US_id.txt")
	tweets = read_tweets("Tweets/US_tweets.txt")
	print_stats(tweets, emoji_list)

main()
