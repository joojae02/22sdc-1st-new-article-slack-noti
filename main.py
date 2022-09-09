from JoyangBlog import JoyangBlog
from SmdcmartBlog import SmdcmartBlog
from slack import SlackBot
import pymysql
from db import DB

def main(event, context) :
    db = DB()
    joyang_blog = JoyangBlog('조양', 'https://blog.naver.com/joyangmart', db)
    joyang_blog.save_wine_list()
    smdcmart_blog = SmdcmartBlog('구판장', 'https://blog.naver.com/smdcmart', db)
    smdcmart_blog.save_wine_list()
    
    slack_bot = SlackBot(joyang_blog)
    slack_bot.post_messages()

    slack_bot1 = SlackBot(smdcmart_blog)
    slack_bot1.post_messages()

