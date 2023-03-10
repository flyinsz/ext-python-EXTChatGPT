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

### 安装依赖包
* pip install websocket-client
* pip install revChatGPT

### 使用前的准备工作
* 易小天安装完成并成功运行后，打开 **管理面板**
* 在 管理面板 **页面展示** 页面，点击 **启动一个新微信** 按钮，按照提示扫码、连接、授权，记录微信的 **pid** 
* 回到 管理面板**个人中心** 页面，找到插件 **EXTChatGPT** 点击添加
* 重新回到易小天软件的运行窗口，打开 **插件目录**,会看到软件自动生成了一个名为 **EXTChatGPT** 的文件夹
* 把本项目里的main.py、plugin.py、config.py三个文件保存到 **EXTChatGPT** 文件夹中

### 编辑config.py文件
* chatroom_name_list -> list：聊天机器人生效的微信群名称列表
* plugin_info -> str：插件启动时机器人向文件助手发送的提示信息
* pid -> int: 聊天机器人在EXT框架里的pid，如果只使用一个微信，填0也可以
* api_key -> str: openai申请的api_key

### 启动插件
* 回到 **管理面板** -> **个人中心** ,点击 **EXTChatGPT** 插件的启动按钮，状态显示2表示启动成功
* 查看微信的文件助手消息，如果收到 **plugin_info** 信息说明插件已开始正常工作
* 如未正常启动，回到易小天软件的运行窗口，点击日志目录按钮，查看运行日志排查问题所在

### 发送问题
* 在 **chatroom_name_list** 中已设置好的群里，@群聊机器人后，在输入框输入问题，等待回复。

![微信截屏](https://github.com/lovexingqiba/ext-python-EXTChatGPT/raw/main/images/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20230310165435.jpg)
