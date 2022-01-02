import praw

reddit = praw.Reddit(client_id='tITRA-SCfzWIriTSD3wIcQ',
                     client_secret='HPoudCDIErCzBwxlgNvlLQX3E5ixNg',
                     user_agent='reddit bot to try',
                     username='zooshat',
                     password='blackhatworld',
                     check_for_async=False)
                     
import random
import time
def karma():
  try:
    messages = ["Upvoted, upvote in return?", "Great post, care to share the upvotes!"]
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
  except:
    time.sleep(70)
    karma()
karma()
