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
    # 최근 o 눌린 유저 아이디
    def get_eating_memers_id(self, channel_id):
        result_conversation_history = self.client.conversations_history(channel=channel_id)
        if (result_conversation_history.get('ok')):
            get_messages = result_conversation_history.get('messages')
            for i in get_messages:
                if i.get('reactions'):
                    reactions = i.get('reactions')
                    for j in reactions:
                        if j['name'] == 'o':
                            return j['users']    
    #user name 가져오기
    def get_user_name(self, user_id):
        a = self.client.users_info(user=user_id)
        if (a['ok']):
            return a['user']['real_name']
    # 채널에 글 쓰기
    def notice_eating_member(self, channel_id, text, group):
        str1 = ""
        str1 += group
 
        # traverse in the string
        for ele in text:
            str1 += ele
            str1 += " "
 
        self.client.chat_postMessage(channel=channel_id,text=str1)

token = "<token>"
slack = SlackAPI(token)

channel_name = "testbot"

# 채널ID 파싱
channel_id = "<channel_id>"

# 최근대화 불러오기 -> 리액션 o인 사람 유저 이름 가져오기
eating_members = slack.get_eating_memers_id(channel_id)
random.shuffle(eating_members)
seperate_idx = len(eating_members) // 2

a_member = list()
b_member = list()

for i, member in enumerate(eating_members, start=0):
    if (i < seperate_idx):
        a_user_name = slack.get_user_name(member)
        a_member.append(a_user_name)
    if (i >= seperate_idx):
        b_user_name = slack.get_user_name(member)
        b_member.append(b_user_name)
slack.notice_eating_member(channel_id, a_member, 'A group: ')
slack.notice_eating_member(channel_id, b_member, 'B group: ')
