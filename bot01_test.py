import time
import praw

# Initialize connection w/ Reddit server, allows API access
test_instance = praw.Reddit('This is a test by A-Top'
							'This test will bot things, do stuff, etc')
					
test_user = 'atop_testbot_01'
test_user_pwd = 'testbot01'							
test_instance.login(test_user, test_user_pwd)
print "Login was successful? %s" % test_instance.is_logged_in()

already_done = [] #ignore this for now

prawWords = ['city', 'lane']

#while True:
	#subreddit = test_instance.get_subreddit('vancouver')
	#for submission in subreddit.get_hot(limit = 10):
		##Do something here if shit gets found!

		#op_text = submission.selftext.lower()
		#has_praw = any(string in op_text for string in prawWords)
		
		#print has_praw
		
		#if submission.id not in already_done and has_praw:
			#msg = '[Testing Van bot](%s)' % submission.short_link
			#test_instance.send_message('jobsingovernment', 'bot test', msg)
			#already_done.append(submission.id)
		#time.sleep(30)
	
