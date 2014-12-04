import praw
import random
import time

# Current date and time

datetimenow = time.strftime("%c")


# Open the bot's log file for writing logs

log_file = open("bot_log.txt", "w")


# Open the comment and PM text files and read them
# Store them all in two lists and generate set of random comm & mess

comment_file = open("comment_replies.txt", "r")
message_file = open("pm_replies.txt", "r")
comm_list = []
mess_list = []
comm_list = comment_file.read().splitlines()
mess_list = message_file.read().splitlines()
rando_comm = random.choice(comm_list)
rando_list = random.choice(mess_list)


# Initialize connection w/ Reddit server, allows API access

test_instance = praw.Reddit('This is a test by A-Top'
							'This test will bot things, do stuff, etc')


# Log in as test account, please don't steal my hardcoded login info :(

test_user = 'atop_testbot_01'
test_user_pwd = 'testbot01'							
test_instance.login(test_user, test_user_pwd)
print "Login was successful? %s" % test_instance.is_logged_in()


# Choose the subreddit to check and the offender words/phrases

subreddit = test_instance.get_subreddit('test01_sub_slowc')
boringtopics = ['pulled pork', 'pulled']


# Needs a mechanism to make sure no multiple replies to the same OP!!!!

already_done = []
print already_done


# Infinite loop to run the bot foreverrr!

#while True:


# Loops to check the top 50 hot submissions (check hot BUT !!!new!!! too!)

for submission in subreddit.get_hot(limit = 50):
	optitle = submission.title.lower()
	
	# Check to see if any submissions contain the offending words/phrases
	if any(string in optitle for string in boringtopics):
		
		# Checks to make sure we haven't already done that submission!
		if not(any(string2 in optitle for string2 in already_done)):
			
			
			print "%s" % submission
			posters_username = submission.author
			print posters_username
			submission_karma = submission.score
			print submission_karma
			chopped_op = optitle [0:40] # OP title truncated to 40 characters
			
			# LET'S REPLY TO THIS LAME SUBMISSION!!!
			#print submission.add_comment("Your submission is so lame, /u/%s ! \
									#\nHow the hell did it even get %d karma? \
									#\n%s" % (posters_username, submission_karma, rando_comm))
									
			# LET'S SEND THAT LAMER A MESSAGE!
			#test_instance.send_message('%s' % posters_username, \
										#'RE: Your post in /r/slowcooking: %s... yada yada' % chopped_op, \
										#'Your submission could not have been more boring. \
										#This topic has been covered a bajillion times already, \
										#did you even bother searching the sub before posting? \
										#Shame on you, %s !' % posters_username)
			
			# Make sure optitle is a string for writing to lists
			optitle_str = str(optitle)
			 
			# Add the submission we just did to the list of done submissions							
			already_done.append(optitle_str)
			
			# Add log entry for the done submission, include title, date and time
			log_message = []
			time_of_sub_log = "%s in PST" % datetimenow
			log_message.append(time_of_sub_log)
			log_message.append(optitle_str)
			log_file.write("%r" % log_message)
			
print already_done
											

# Introduce a delay into the program, wait before running the bot again

#time.sleep(3600) # Wait an hour (3600 secs = 60 mins)

		
# Close the comment & PM text files after using them!

comment_file.close()
message_file.close()		
		
		
# Write a log of all the comments & messages sent, use a text file
