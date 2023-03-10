# ext-python-EXTChatGPT

一个基于ChatGPT和WXEXT框架（微信易小天）的微信机器人。

## WXEXT介绍
> WXEXT（[微信易小天](https://github.com/wxext/wxext)）是一个基于微信PC端，使用HOOK技术的微信个人号开发框架，可以通过代码控制微信接收、发送各类消息。
* [微信官网下载安装PC微信](https://pc.weixin.qq.com/) 自动匹配支持最新版微信.
* [下载安装](https://www.wxext.cn/)运行后,访问 127.0.0.1:8203 查看[开发文档](https://github.com/wxext/wxext/tree/master/docs/home)及管理本机微信程序


## 插件运行环境
* python3.8
* 软件包websocket-client 1.4.2
* 软件包revChatGPT 3.1.8.2
* wxext框架 3.7.5.2
* 微信PC 3.7.5.23
* 其它版本请自行测试

## 插件使用方法
> 首先你要有openai账号，注册方法和api_key获取方法有很多教程，自行搜索查看。

### 编辑config.py文件
* chatroom_name_list -> list：聊天机器人生效的微信群名词列表
* plugin_info -> str：插件启动时机器人向文件助手发送的提示信息
* pid -> int: 聊天机器人在EXT框架里的pid
* api_key -> str: openai申请的api_key

### 发送问题
* 在 **chatroom_name_list** 中已设置好的群里，@群聊机器人后，在输入框输入问题，等待回复。

