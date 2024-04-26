import requests
import json

from core.constants import DATA, OAUTH_URL, QUESTION_URL


class GigaChat:

    def __init__(self, auth, rq):
        self.auth = auth
        self.rqUID = rq
        self.get_token()
        self.communication = []

    def get_token(self):
        url = OAUTH_URL
        headers = {
            'Authorization': f'Bearer {self.auth}',
            'RqUID': self.rqUID,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = DATA
        response = self.get(url, headers, data,)
        self.access_token = json.loads(response.text)['access_token']

    def get(self, url, headers, data, verify=False, json=False):
        if json:
            return requests.post(
                url, headers=headers, json=data, verify=verify,
            )
        else:
            return requests.post(
                url, headers=headers, data=data, verify=verify,
            )

    def ask_a_question(self, question):
        url = QUESTION_URL
        headers = {
            'Content-Type': '`application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        self.communication.append({'role': 'user', 'content': question})
        data = {
            'model': 'GigaChat:latest',
            'messages': self.communication,
        }
        response = self.get(url, headers, data, json=True).json()
        if response['choices']:
            content = response['choices'][0]['message']['content']
            self.communication.append(
                {'role': 'assistant', 'content': content},
            )
            return content

    def reset(self):
        self.communication.clear()
