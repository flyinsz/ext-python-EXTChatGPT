# ext-python-EXTChatGPT
基于ChatGPT和EXT框架的微信机器人
## 运行环境
* python3.8
* websocket-client 1.4.2
* revChatGPT 3.1.8.2
* ext框架 3.7.5.2
* 微信PC 3.7.5.23
* 其它版本请自行测试

## 使用方法
> 首先你要有openai账号，注册方法和api_key获取方法有很多教程，自行搜索查看。

### 编辑config.py文件
* chatroom_name_list：聊天机器人生效的微信群名词列表
* plugin_info：插件启动时机器人向文件助手发送的提示信息
* pid: 聊天机器人在EXT框架里的pid
* api_key: openai申请的api_key

### 发送问题
* 在 **chatroom_name_list** 中已设置好的群里，@群聊机器人后，在输入框输入问题，等待回复。
