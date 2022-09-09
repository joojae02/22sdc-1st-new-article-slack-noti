
from Blog import Blog
from slack import SlackBot
import pymysql
from db import DB

def main(event, context) :
    db = DB()
    smdcmart_blog = Blog('구판장', 'https://blog.naver.com/smdcmart', db)
    smdcmart_blog.save_wine_list()
        
    slack_bot = SlackBot(smdcmart_blog)
    slack_bot.post_messages()

