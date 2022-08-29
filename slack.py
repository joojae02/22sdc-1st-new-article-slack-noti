import requests
import json

class SlackBot :
    def __init__(self, blog) :
        self.url = "https://hooks.slack.com/services/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"
        self.blog = blog
        self.content_list = self.blog.get_wine_list()
            
    def post_message(self):
        text = ' '.join(str(s) for s in self.content_list)
        data = {'text':text}
        resp = requests.post(url=self.url, json=data)
        return resp
                            
