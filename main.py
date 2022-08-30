from blogs.JoyangBlog import JoyangBlog
from blogs.SmdcmartBlog import SmdcmartBlog
from slack import SlackBot
import project_info
import pymysql

def main() :

    joyang_blog = JoyangBlog('조양', 'https://blog.naver.com/joyangmart')
    joyang_blog.save_wine_list()
    smdcmart_blog = SmdcmartBlog('구판장', 'https://blog.naver.com/smdcmart')
    smdcmart_blog.save_wine_list()
    
    slack_bot = SlackBot(joyang_blog, project_info.oauth_token, project_info.channel_name)
    slack_bot.post_message()

    slack_bot1 = SlackBot(smdcmart_blog, project_info.oauth_token, project_info.channel_name)
    slack_bot1.post_message()


    
main()


