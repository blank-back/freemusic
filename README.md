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
