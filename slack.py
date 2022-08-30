import requests
import json
from slack_sdk import WebClient

class SlackBot :
    def __init__(self, blog, oauth_token, channel_name) :
        self.blog = blog
        self.content_list = self.blog.get_wine_list()
        self.content_title = self.blog.get_content_title()
        self.channel_name = channel_name
        self.client = WebClient(token = oauth_token)

    def post_message(self):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        text = self.get_wine_list_to_str()
        channel_id = self.channel_name
            # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text
        )
        return result

    def get_wine_list_to_str(self) :
        text = '새로운 게시물 : ' + self.content_title + '\n'
        for s in self.content_list :
            text += s + '\n'
        return text