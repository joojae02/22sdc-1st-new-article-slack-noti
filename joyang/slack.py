import os
import requests
import json
from slack_sdk import WebClient

class SlackBot :
    def __init__(self, blog) :
        self.blog = blog
        self.blog_name = self.blog.get_name()
        self.not_exist_title_list = self.blog.get_not_exist_title_list()
        self.title_content_dic = self.blog.get_title_content_dic()
        self.channel_name = os.environ['channel_name']
        self.client = WebClient(token = os.environ['oauth_token'])
    def post_messages(self) :
        channel_id = self.channel_name
        for title in self.not_exist_title_list :
            self.post_message(title, channel_id, self.title_content_dic[title])

    def post_message(self, title, channel_id, content):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        text = self.blog_name + ' : '+ title + ' \n' + content
        
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text
        )
        return result
