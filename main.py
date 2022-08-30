from blogs.JoyangBlog import JoyangBlog
from blogs.SmdcmartBlog import SmdcmartBlog
from slack import SlackBot
def main() :

    joyang_blog = JoyangBlog('조양', 'https://blog.naver.com/joyangmart')
    joyang_blog.save_wine_list()
    joyang_blog.print_wine_list()

   

    smdcmart_blog = SmdcmartBlog('구판장', 'https://blog.naver.com/smdcmart')
    smdcmart_blog.save_wine_list()
    smdcmart_blog.print_wine_list
     slack_bot = SlackBot(joyang_blog)
'''
    slack_bot = SlackBot(joyang_blog)
    slack_bot.post_message()

    slack_bot1 = SlackBot(smdcmart_blog)
    slack_bot1.post_message()
'''
    
main()

