import json
import threading
import time

from revChatGPT.V3 import Chatbot
import config


class ChatManger:
    def __init__(self):
        self.bot = Chatbot(api_key=config.api_key)
        self.ws = None
        self.pid = config.pid

    @staticmethod
    def __get_ask_info(msg):
        t = msg.split('\u2005')
        return t[1]

    # 过滤原始消息，筛选符合要求的应答信息
    def _filter_msg(self, raw_wx_msg):
        # 来自群里的文本消息
        if raw_wx_msg['type'] == 1 and \
                raw_wx_msg['data']['nickName'] in config.chatroom_name_list and \
                '在群聊中@了你' in raw_wx_msg['data']['des']:
            # 需要处理这条消息,返回群id，@相关信息
            ret = {
                'chatroom_id': raw_wx_msg['data']['fromid'],
                'user_id': raw_wx_msg['data']['memid'],
                'ask': self.__get_ask_info(raw_wx_msg['data']['msg'])
            }
            if len(ret['ask']) == 0:
                return False
            else:
                return ret
        else:
            return False

    # 封装一个基本的发送过程
    def _send_message(self, wxid, atid, message):
        p = {
            "method": "sendText",
            "wxid": wxid,
            "msg": message,
            "atid": atid,
            "pid": self.pid
        }
        self.ws.send(json.dumps(p))

    # 在群里回复消息
    def _reply_message(self, raw_wx_msg, reply_msg):
        wxid = raw_wx_msg['data']['fromid']
        atid = raw_wx_msg['data']['memid']
        if wxid and atid and reply_msg:
            self._send_message(wxid, atid, reply_msg)

    # 机器人接到符合的消息后，添加任务

    def on_message(self, ws, message):
        self.ws = ws
        message = json.loads(message)
        filter_msg = self._filter_msg(message)
        if filter_msg:
            if len(filter_msg['ask']) > 2000:
                self._reply_message(message, '问题字数不能超过2000字，精简一下重新提问吧！')
            else:
                ret = self.start_ask(filter_msg)
                if ret['status'] == 0:
                    self._reply_message(message, '问题已发送，耐心等待机器人答复吧。')
                else:
                    self._reply_message(message, ret['msg'])

    def on_open(self, ws):
        self.ws = ws
        plugin_info = config.plugin_info
        p = {'method': 'sendText',
             'wxid': 'filehelper',
             'msg': plugin_info,
             'pid': 0}
        self.ws.send(json.dumps(p))

    # 这是一个耗时操作，需要放到线程里,结果返回之后，直接发送信息给微信
    def start_ask(self, filter_message):
        def th_def(retry=3):
            try:
                result = self.bot.ask(filter_message['ask'], convo_id=filter_message['user_id'])
                self._send_message(filter_message['chatroom_id'], filter_message['user_id'], result)
            except Exception as e:
                if retry == 0:
                    self._send_message(filter_message['chatroom_id'], filter_message['user_id'], str(e))
                else:
                    retry -= 1
                    time.sleep(3)
                    th_def(retry)

        t = threading.Thread(target=th_def)
        t.start()
        return {'status': 0, 'msg': 'success'}
