
# -*- coding: utf-8 -*-
import time
import urllib.request

from editor import *
from remi.gui import *
from remi import start, App
from music import *
import datetime
from playsound import playsound
import pygame



class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        # if not 'editing_mode' in kwargs.keys():
        super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})
        self.strsong=""
        self.strsinger=""
        self.answ=""
        self.stroth=""
        self.state = True
        pygame.mixer.init()


    def main(self):
        return untitled.construct_ui(self)

    @staticmethod
    def construct_ui(self):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        self.container0 = Container()
        self.container0.attr_class = "Container"
        self.container0.attr_editor_newclass = False
        self.container0.css_background_image = "url('D:\pythonProject13\editor\1.jpg')"
        self.container0.css_height = "960px"
        self.container0.css_left = "200px"
        self.container0.css_position = "absolute"
        self.container0.css_top = "0px"
        self.container0.css_width = "1080px"
        self.container0.variable_name = "container0"
        self.label0 = Label()
        self.label0.attr_class = "Label"
        self.label0.attr_editor_newclass = False
        self.label0.css_background_color = "rgb(0,255,255)"
        self.label0.css_color = "rgb(129,0,119)"
        self.label0.css_font_size = "21px"
        self.label0.css_font_style = "italic"
        self.label0.css_font_weight = "bolder"
        self.label0.css_height = "30.0px"
        self.label0.css_left = "42%"
        self.label0.css_position = "absolute"
        self.label0.css_text_align = "center"
        self.label0.css_top = "5%"
        self.label0.css_width = "180.0px"
        self.label0.text = "在线听歌网页端"
        self.label0.variable_name = "label0"
        self.container0.append(self.label0, 'label0')
        self.label1 = Label()
        self.label1.attr_class = "Label"
        self.label1.attr_editor_newclass = False
        self.label1.css_background_color = "rgb(255,255,0)"
        self.label1.css_border_color = "rgb(0,0,0)"
        self.label1.css_color = "rgb(0,0,0)"
        self.label1.css_font_size = "15px"
        self.label1.css_font_weight = "bold"
        self.label1.css_height = "30px"
        self.label1.css_left = "89.46249389648438px"
        self.label1.css_position = "absolute"
        self.label1.css_text_align = "center"
        self.label1.css_top = "30%"
        self.label1.css_width = "100px"
        self.label1.text = "歌曲名"
        self.label1.variable_name = "label1"
        self.container0.append(self.label1, 'label1')
        self.textinput0 = TextInput()
        self.textinput0.attr_class = "TextInput"
        self.textinput0.attr_editor_newclass = False
        self.textinput0.css_background_color = "rgb(255,255,255)"
        self.textinput0.css_border_color = "rgb(0,255,255)"
        self.textinput0.css_border_radius = "2px"
        self.textinput0.css_border_style = "solid"
        self.textinput0.css_border_width = "2px"
        self.textinput0.css_height = "30px"
        self.textinput0.css_left = "276.4624938964844px"
        self.textinput0.css_position = "absolute"
        self.textinput0.css_top = "30%"
        self.textinput0.css_width = "100px"
        self.textinput0.text = "请输入歌曲名"
        self.textinput0.variable_name = "textinput0"
        self.container0.append(self.textinput0, 'textinput0')
        self.textinput1 = TextInput()
        self.textinput1.attr_class = "TextInput"
        self.textinput1.attr_editor_newclass = False
        self.textinput1.css_border_color = "rgb(255,255,0)"
        self.textinput1.css_border_radius = "2px"
        self.textinput1.css_border_style = "solid"
        self.textinput1.css_border_width = "2px"
        self.textinput1.css_color = "rgb(0,0,0)"
        self.textinput1.css_height = "30px"
        self.textinput1.css_left = "276px"
        self.textinput1.css_position = "absolute"
        self.textinput1.css_top = "40%"
        self.textinput1.css_width = "100px"
        self.textinput1.text = "请输入歌手名"
        self.textinput1.variable_name = "textinput1"
        self.container0.append(self.textinput1, 'textinput1')
        self.label2 = Label()
        self.label2.attr_class = "Label"
        self.label2.attr_editor_newclass = False
        self.label2.css_background_color = "rgb(0,255,0)"
        self.label2.css_font_weight = "bold"
        self.label2.css_height = "30px"
        self.label2.css_left = "89px"
        self.label2.css_position = "absolute"
        self.label2.css_text_align = "center"
        self.label2.css_top = "40%"
        self.label2.css_width = "100px"
        self.label2.text = "歌手"
        self.label2.variable_name = "label2"
        self.container0.append(self.label2, 'label2')
        self.button0 = Button()
        self.button0.attr_class = "Button"
        self.button0.attr_editor_newclass = False
        self.button0.css_height = "30px"
        self.button0.css_left = "46%"
        self.button0.css_position = "absolute"
        self.button0.css_top = "80%"
        self.button0.css_width = "100px"
        self.button0.text = "搜索"
        self.button0.variable_name = "button0"
        self.container0.append(self.button0, 'button0')
        self.date0 = Date()
        self.date0.attr_class = "date"
        self.date0.set_value(str(datetime.date.today()))
        self.date0.attr_editor_newclass = False
        self.date0.css_height = "30px"
        self.date0.css_left = "46%"
        self.date0.css_position = "absolute"
        self.date0.css_top = "15%"
        self.date0.css_width = "100px"
        self.date0.variable_name = "date0"
        self.date0.onchange.connect(self.puthis)
        self.container0.append(self.date0, 'date0')
        self.link0 = Link()
        self.link0.attr_class = "Link"
        self.link0.attr_editor_newclass = False
        self.link0.attr_href = "https://space.bilibili.com/628363349"
        self.link0.css_color = "rgb(255,0,0)"
        self.link0.css_height = "30px"
        self.link0.css_left = "46%"
        self.link0.css_position = "absolute"
        self.link0.css_text_align = "center"
        self.link0.css_top = "90%"
        self.link0.css_width = "100px"
        self.link0.text = "欢迎关注"
        self.link0.variable_name = "link0"
        self.container0.append(self.link0, 'link0')
        self.label3 = Label()
        self.label3.attr_class = "Label"
        self.label3.attr_editor_newclass = False
        self.label3.css_border_color = "rgb(0,0,255)"
        self.label3.css_border_radius = "2px"
        self.label3.css_border_style = "solid"
        self.label3.css_border_width = "2px"
        self.label3.css_height = "100px"
        self.label3.css_left = "690px"
        self.label3.css_overflow = "scroll"
        self.label3.css_position = "absolute"
        self.label3.css_top = "35.5%"
        self.label3.css_width = "150px"
        self.label3.text = "输出结果"
        self.label3.variable_name = "label3"
        self.label3.css_white_space = "pre-line"
        self.container0.append(self.label3, 'label3')
        self.button1 = Button()
        self.button1.attr_class = "Button"
        self.button1.attr_editor_newclass = False
        self.button1.css_height = "30px"
        self.button1.css_left = "900px"
        self.button1.css_position = "absolute"
        self.button1.css_top = "30%"
        self.button1.css_width = "100px"
        self.button1.text = "播放"
        self.button1.variable_name = "button1"
        self.container0.append(self.button1, 'button1')
        self.button2 = Button()
        self.button2.attr_class = "Button"
        self.button2.attr_editor_newclass = False
        self.button2.css_height = "30px"
        self.button2.css_left = "900px"
        self.button2.css_position = "absolute"
        self.button2.css_top = "40%"
        self.button2.css_width = "100px"
        self.button2.text = "停止"
        self.button2.variable_name = "button2"
        self.container0.append(self.button2, 'button2')
        self.button3 = Button()
        self.button3.attr_class = "Button"
        self.button3.attr_editor_newclass = False
        self.button3.css_height = "30px"
        self.button3.css_left = "900px"
        self.button3.css_position = "absolute"
        self.button3.css_top = "50%"
        self.button3.css_width = "100px"
        self.button3.text = "暂停"
        self.button3.variable_name = "button3"
        self.container0.append(self.button3, 'button3')
        self.textinput3 = TextInput()
        self.textinput3.attr_class = "TextInput"
        self.textinput3.attr_editor_newclass = False
        self.textinput3.css_border_color = "rgb(255,0,255)"
        self.textinput3.css_border_radius = "2px"
        self.textinput3.css_border_style = "solid"
        self.textinput3.css_border_width = "2px"
        self.textinput3.css_height = "30px"
        self.textinput3.css_left = "276px"
        self.textinput3.css_position = "absolute"
        self.textinput3.css_top = "50%"
        self.textinput3.css_width = "100px"
        self.textinput3.text = "请输入其它可选信息"
        self.textinput3.variable_name = "textinput3"
        self.container0.append(self.textinput3, 'textinput3')
        self.label4 = Label()
        self.label4.attr_class = "Label"
        self.label4.attr_editor_newclass = False
        self.label4.css_background_color = "rgb(255,160,255)"
        self.label4.css_font_weight = "bold"
        self.label4.css_height = "30px"
        self.label4.css_left = "89px"
        self.label4.css_position = "absolute"
        self.label4.css_text_align = "center"
        self.label4.css_top = "50%"
        self.label4.css_width = "100px"
        self.label4.text = "可选补充"
        self.label4.variable_name = "label4"
        self.container0.append(self.label4, 'label4')
        self.label5 = Label()
        self.label5.attr_class = "Label"
        self.label5.attr_editor_newclass = False
        self.label5.css_background_color = "rgb(0,255,255)"
        self.label5.css_font_weight = "bold"
        self.label5.css_height = "30px"
        self.label5.css_left = "46%"
        self.label5.css_position = "absolute"
        self.label5.css_text_align = "center"
        self.label5.css_top = "57%"
        self.label5.css_width = "100px"
        self.label5.text = "搜索历史"
        self.label5.variable_name = "label5"
        self.container0.append(self.label5, 'label5')
        self.label6 = Label()
        self.label6.attr_class = "Label"
        self.label6.attr_editor_newclass = False
        self.label6.css_border_color = "rgb(0,255,255)"
        self.label6.css_border_radius = "2px"
        self.label6.css_border_style = "solid"
        self.label6.css_border_width = "2px"
        self.label6.css_height = "100px"
        self.label6.css_left = "23%"
        self.label6.css_overflow = "scroll"
        self.label6.css_position = "absolute"
        self.label6.css_top = "63%"
        self.label6.css_width = "600px"
        self.label6.text = ""
        self.label6.css_white_space = "pre-line"
        self.label6.variable_name = "label6"
        self.container0.append(self.label6, 'label6')
        self.button3.onclick.connect(self.pause)
        self.button1.onclick.connect(self.play)
        self.button0.onclick.connect(self.sear)
        self.button2.onclick.connect(self.stop)

        return self.container0

    def sear(self, emitter):
        self.label3.set_text("查询中，请稍候...")
        self.strsong = "" if self.textinput0.get_text()=="请输入歌曲名" else self.textinput0.get_text()
        self.strsinger = "" if self.textinput1.get_text()=="请输入歌手名" else self.textinput1.get_text()
        self.stroth = "" if self.textinput3.get_text()=="请输入其它可选信息" else self.textinput3.get_text()
        self.answ=getmusic(self.strsong, self.strsinger, self.stroth)
        if self.answ:
            self.label3.set_text("查询完成，点击播放即可\n")
            with open("./history.txt", "a+", encoding='utf-8') as f:
                if str(datetime.date.today())+"\n" not in f.readlines():
                    f.write(str(datetime.date.today())+"\n")
                f.write(str(datetime.datetime.now())[11:] + " 查询 " + " 歌曲名 " + self.strsong + " 歌手 " + self.strsinger + "\n地址 " + self.answ + "\n\n")
        else:
            self.label3.set_text("看来曲库中并没有查询到相关信息\n")

    def play(self, emitter):
        if not os.path.exists("./temp"):
            os.mkdir("./temp")
        strsong = "" if self.textinput0.get_text()=="请输入歌曲名" else self.textinput0.get_text()
        strsinger = "" if self.textinput1.get_text()=="请输入歌手名" else self.textinput1.get_text()
        filename=strsong+"-"+strsinger+".mp3"
        dl=[]
        for _,_,a in os.walk(os.getcwd()+"\\temp"):
            if len(a)!=0:
                for i in a:
                    dl.append(i)
        print(dl)
        if filename in dl:
            pass
        else:
            if self.strsong != strsong or self.strsinger != strsinger:
                self.label3.set_text("请先搜索此歌：\n"+strsong+'-'+strsinger)
                return
            self.label3.set_text("正在下载：\r\n" + filename)
            urllib.request.urlretrieve(self.answ, "./temp/"+filename)
        self.label3.set_text("正在播放："+chr(13) + chr(10)+filename+"\n若对解析结果不满意，可使用MV搜索")
        pygame.mixer.music.load(os.getcwd()+"\\temp\\"+filename)
        pygame.mixer.music.play()

    def stop(self, emitter):
        self.label3.set_text("停止播放：\n")
        pygame.mixer.music.stop()

    def pause(self, emitter):
        self.state= not self.state
        if self.state:
            self.label3.set_text("继续播放：\n")
            pygame.mixer.music.unpause()
        else:
            self.label3.set_text("暂停播放：\n")
            pygame.mixer.music.pause()

    def puthis(self,emitter, value):
        tmp=False
        deststr=""
        with open("./history.txt", "r", encoding='utf-8') as f:
            line=f.readlines()
        print(line)
        if self.date0.get_value()+"\n" not in line:
            self.label6.set_text("暂无历史")
            return
        for i in line:
            if i==self.date0.get_value()+"\n":
                tmp=True
                print("i:",i)
                continue
            if "-" in i and i[4]=="-" and i[7]=="-":
                print(i)
                tmp=False
            if tmp:
                print(i)
                deststr+=i
        print("deststr:",deststr)
        self.label6.set_text(deststr)

#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
