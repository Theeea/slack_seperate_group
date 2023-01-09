import sys
import json
import random

from slack_sdk import WebClient

class SlackAPI:
    """
    슬랙 API 핸들러
    """
    def __init__(self, token):
        # 슬랙 클라이언트 인스턴스 생성
        self.client = WebClient(token)
    # 채널에 글 쓰기
    def notice_vote(self, channel_id):
        self.client.chat_postMessage(channel=channel_id,text='<message>')

token = "<token>"
slack = SlackAPI(token)

channel_name = "testbot"

# 채널ID 파싱
channel_id = "<channel_id>"

slack.notice_vote(channel_id)
