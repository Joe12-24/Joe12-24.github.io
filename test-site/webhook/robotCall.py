import requests
import json

# 设置钉钉机器人的 Webhook 地址
webhook = "https://oapi.dingtalk.com/robot/send?access_token=96ea1e19b54531a2e156aaa3646832943bde7baf8df71192e4af4f64e1e1a1dc"
# message="@沈斌，这是测试";
# 设置要发送的消息内容，这里使用了一个Markdown格式的消息
# message = {
#     "msgtype": "markdown",
#     "markdown": {
#         "title": "@沈斌凌志消息提醒",
#         "text": "#### 消息提醒\n\n> 这是一条来自Python脚本的测试消息，详情请点击 [链接](http://www.example.com)\n"
#     }
# }
message = {
    "at": {
        "atMobiles":[
            "15737347107"
        ]
    },
    "text": {
        "content":"凌志：我就是我, @XXX 是不一样的烟火"
    },
    "msgtype":"text"
}
# 将消息转换成json格式
data = json.dumps(message)
# data = message.encode('utf-8');

# 发送POST请求，将消息推送到钉钉机器人
response = requests.post(url=webhook, data=data, headers={"Content-Type": "application/json"})

# 打印响应结果，如果发送成功则会返回 {"errcode": 0, "errmsg": "ok"}
print(response.content)
