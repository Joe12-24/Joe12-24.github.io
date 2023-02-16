import requests
import json

# 钉钉开放平台的应用信息
app_id = 'your_app_id'
app_secret = 'your_app_secret'

# 获取钉钉开放平台的 access_token
token_url = 'https://oapi.dingtalk.com/gettoken'
params = {'appkey': app_id, 'appsecret': app_secret}
response = requests.get(token_url, params=params)
access_token = response.json()['access_token']

# 构造请求消息
url = 'https://oapi.dingtalk.com/message/send_to_conversation'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
data = {
    'sender_userid': 'user_id_of_sender',  # 发送者用户 ID
    'cid': 'conversation_id',  # 会话 ID
    'msg': {
        'msgtype': 'text',
        'text': {'content': 'Hello, world!'}
    }
}

# 发送请求
response = requests.post(url, headers=headers, data=json.dumps(data))
