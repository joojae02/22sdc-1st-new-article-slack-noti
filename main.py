from blogs.JoyangBlog import JoyangBlog
from blogs.SmdcmartBlog import SmdcmartBlog
from slack import SlackBot
def main() :
    
    
    '''
    slack_token = "xoxb-4004765306050-4007235202500-K9XQWfc1Ia8cO3PqgkfeZvcG"
    slack_bot = SlackBot()
    slack_bot.post_message("Hello World!")
    '''
    joyang_blog = JoyangBlog('조양', 'https://blog.naver.com/joyangmart')
    joyang_blog.open_web_driver()
    joyang_blog.switch_to_frame('mainFrame')
    joyang_blog.open_first_post_table()
    joyang_blog.read_title_url_date_from_table()
    joyang_blog.open_second_next_post_table()
    joyang_blog.read_title_url_date_from_table()
    joyang_blog.print_title_url()
    joyang_blog.access_to_post()
    joyang_blog.read_content()
    joyang_blog.print_wine_list()

    smdcmart_blog = SmdcmartBlog('구판장', 'https://blog.naver.com/smdcmart')
    smdcmart_blog.open_web_driver()
    smdcmart_blog.switch_to_frame('mainFrame')
    smdcmart_blog.read_title_url_date_from_table()
    smdcmart_blog.print_title_url()
    smdcmart_blog.access_to_post()
    smdcmart_blog.read_content()
    smdcmart_blog.print_wine_list()
    
main()

