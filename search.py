import tweepy

def authenticate():
	CONSUMER_KEY = open("Authentication/Consumer_Key.txt").read().rstrip("\n")
	CONSUMER_SECRET = open("Authentication/Consumer_Secret.txt").read().rstrip("\n")

	ACCESS_TOKEN = open("Authentication/Access_Token.txt").read().rstrip("\n")
	ACCESS_TOKEN_SECRET = open("Authentication/Access_Token_Secret.txt").read().rstrip("\n")
	
	oauth_handler = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	oauth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return oauth_handler

def main():
    authentication = authenticate()
    api = tweepy.API(authentication, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    print(tweepy.API.search(q="#박근혜", lang="ko"))

main()

