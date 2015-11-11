import tweepy

def authenticate():

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

def print_home_timeline(api):
	public_tweets = api.home_timeline()
	# print timeline
	for tweet in public_tweets:
		print(tweet.text)

def read_user_id(filename):
	infile = open(filename)
	user_id_list = []
	for user_id in infile:
		user_id_list.append(user_id.rstrip('\n'))		
	infile.close()
	return user_id_list

def main():
	authentication = authenticate()	
	# Construct the API instance
	api = tweepy.API(authentication, 
					 wait_on_rate_limit = True,
					 wait_on_rate_limit_notify = True)
					 
	infilename = "US_id_1.txt"				 
	user_id_list = read_user_id(infilename)
	
	
	outfilename = "US_tweets_1.txt"
	outfile = open(outfilename, 'w')
	
	for user_id in user_id_list:
		for status in tweepy.Cursor(api.user_timeline, id=user_id).items(200):
			outstring = "<Text_Begin ID=" + user_id + ">" + status.text + "<Text_End>\n"
			outfile.write(outstring)


main()
