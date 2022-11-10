from Blog import Blog
from slack import SlackBot
import pymysql
from db import DB

def main(event, context) :
    db = DB()
    joyang_blog = Blog('조양', 'https://blog.naver.com/joyangmart', db)
    joyang_blog.save_wine_list()
    
    slack_bot = SlackBot(joyang_blog)
    slack_bot.post_messages()


