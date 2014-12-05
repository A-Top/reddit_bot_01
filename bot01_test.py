import praw
import random
import time

# Current date and time

datetimenow = time.strftime("%c")


# Open the comment and PM text files and read them
# Store them all in two lists and generate set of random comm & mess

comment_file = open("comment_replies.txt", "r")
message_file = open("pm_replies.txt", "r")
comm_list = []
mess_list = []
comm_list = comment_file.read().splitlines()
mess_list = message_file.read().splitlines()
comment_file.close()
message_file.close()


# Initialize connection w/ Reddit server, allows API access

test_instance = praw.Reddit('This is a pulled pork bot for the slowcooking sub'
							'This bot will mildly shame users who post about pulled pork')


# Log in to a reddit account, bot account is "quit_pulling_my_pork"

test_instance.login()
print "Login was successful? %s" % test_instance.is_logged_in()


# Choose the subreddit to check and the offender words/phrases

subreddit = test_instance.get_subreddit('slowcooking')
boringtopics = ['pulled pork']


# Needs a mechanism to make sure no multiple replies to the same OP!!!!

already_done = []
#print already_done


# Infinite loop to run the bot foreverrr!

while True:

	# Loops to check the top 50 hot submissions
	
	for submission in subreddit.get_hot(limit = 50):
		optitle = submission.title.lower()
		
		# Check to see if any submissions contain the offending words/phrases
		if any(string in optitle for string in boringtopics):
			
			# Checks to make sure we haven't already done that submission!
			if not(optitle in already_done):
								
				print "%s" % submission
				posters_username = submission.author
				#print posters_username
				submission_karma = submission.score
				#print submission_karma
				chopped_op = optitle [0:40] # OP title truncated to 40 characters
				
				rando_comm1 = random.choice(comm_list)
				rando_list1 = random.choice(mess_list)
				
				# LET'S REPLY TO THIS LAME SUBMISSION!!!
				print submission.add_comment("Your submission is so boring, /u/%s ! \
										\nHow the hell did it even get %d upvotes? \
										\n%s" % (posters_username, submission_karma, rando_comm1))
										
				# Make sure optitle is a string for writing to lists
				optitle_str = str(optitle)
				 
				# Add the submission we just did to the list of done submissions							
				already_done.append(optitle_str)
				
				# Add log entry for the done submission, include title, date and time
				with open("bot_log.txt", "a") as log_file:
					log_message = []
					time_of_sub_log = "%s in PST" % datetimenow
					log_message.append(time_of_sub_log)
					log_message.append(submission.id)
					log_message.append(optitle_str)
					log_file.write("%r\n" % log_message)
					
				log_file.close()
				
	#print already_done
	
	# Loops to check the top 25 new submissions
	
	for submission in subreddit.get_new(limit = 25):
		optitle2 = submission.title.lower()	
		
		# Check to see if any submissions contain the offending words/phrases
		if any(string in optitle2 for string in boringtopics):
			
			# Checks to make sure we haven't already done that submission!
			if not(optitle2 in already_done):
				
				print "%s" % submission
				posters_username = submission.author
				#print posters_username
				submission_karma = submission.score
				#print submission_karma
				chopped_op = optitle [0:40] # OP title truncated to 40 characters
				
				rando_comm2 = random.choice(comm_list)
								
				# LET'S REPLY TO THIS LAME SUBMISSION!!!
				print submission.add_comment("Your submission is so boring, /u/%s ! \
										\nHow the hell did it even get %d upvotes? \
										\n%s" % (posters_username, submission_karma, rando_comm2))
										
				# Make sure optitle is a string for writing to lists
				optitle2_str = str(optitle2)
				
				# Add the submission we just did to the list of done submissions							
				already_done.append(optitle2_str)
				
				# Add log entry for the done submission, include title, date and time
				with open("bot_log.txt", "a") as log2_file:
					log2_message = []
					time_of_sub_log = "%s in PST" % datetimenow
					log2_message.append(time_of_sub_log)
					log2_message.append(submission.id)
					log2_message.append(optitle2_str)
					log2_file.write("%r\n" % log2_message)
					
				log2_file.close()
				
	#print already_done										
	
	# Introduce a delay into the program, wait before running the bot again
	
	time.sleep(3600) # Wait one hour (3600 secs = 60 mins)
	print "Looped through once, going again!"


