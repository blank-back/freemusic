# freemusic

**本项目通过selenium实现对[免费音乐网站](https://www.shiyinren.com)的访问及解析外链的获取**




## 主要运行环境
*python 3.8，urllib3 1.26.2, selenium 3.141.0*
## 运行方法

*项目包含两个文件，即gui.py和music.py，gui.py为主文件，运行后将在浏览器打开交互界面（若未打开可自行访问localhost:8081）.*

> 注：若要运行请自行配置chrome webdriver环境

## 前端页面说明
使用[remi](https://github.com/rawpython/remi)进行搭建

## 其它说明
由于搜索页面和解析页面均为动态页面，urllib.request的方法无法获取到查询的具体内容，故改用selenium使用chrome webdriver访问，.

## V 1.0
完成了主要功能的实现，包括获取音乐解析外链，播放音乐，之后版本将以优化查询质量和前端界面视觉效果为主.
### V 1.1
增加了暂停和停止功能，音频播放由playsound改为使用pygame，删除隐式等待，提高了查询效率.
### V 1.2
增加了相关信息的搜索选项以提高搜索结果准确度，可通过改变日历查看对应日期的搜索历史，搜索历史包含时间、歌曲信息和解析地址.
## V 2.0
完成了界面背景的设置，可通过下拉栏切换本地背景，也可随机切换[网络来源](https://unsplash.com/)的风景图.
> 注：虽然随机背景加载较慢，但请勿使用VPN等工具，可能会引起SSL错误
