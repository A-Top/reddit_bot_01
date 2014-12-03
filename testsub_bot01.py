import time
import praw

# Initialize connection w/ Reddit server, allows API access
test_instance = praw.Reddit('This is a test by A-Top'
							'This test will bot things, do stuff, etc')

# Log in as test account, please don't steal my hardcoded login info :(
					
test_user = 'atop_testbot_01'
test_user_pwd = 'testbot01'							
test_instance.login(test_user, test_user_pwd)
print "Login was successful? %s" % test_instance.is_logged_in()

# Check submission title for "pulled pork", and just "pulled" - other case
# Comment with usernamne and joke
# Comment on how much karma the post got
# Check the first two(50 posts) or three(75 posts) pages

subreddit = test_instance.get_subreddit('test01_sub_slowc')
boringtopics = ['pulled pork', 'pulled']

# Needs a mechanism to make sure no multiple replies to the same OP

for submission in subreddit.get_hot(limit = 50):
	optitle = submission.title.lower()
	
	#print "%s" % submission
	#print "%s" % optitle
	#print any(string in optitle for string in boringtopics)
	
	if any(string in optitle for string in boringtopics):
		print "%s" % submission
		submission_karma = submission.score
		print "How the hell did this submission get %s karma?!" % submission_karma
		# print "FUCK THAT BULLSHIT, LET'S REPLY TO THIS LAME SUBMISSION!"
		#print submission.add_comment("Your submission is so lame! \
								#\nHow the hell did it get %d karma?" % submission_karma)
		
		# print "FUCK THAT BULLSHIT, LET'S SEND THAT BITCH A MESSAGE!"
		posters_username = submission.author
		print posters_username
		#test_instance.send_message('%s' % posters_username, \
									#'RE: Your post in r/slowcooking: %s' chopped_op, \
									#'Your original post could not have been more boring. \
									#This topic has been covered a bajillion times already, \
									#did you even bother searching the sub before posting? \
									#Shame on you, %s' % posters_username)
		
	
