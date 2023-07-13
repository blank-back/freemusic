from urllib import request
from urllib import parse

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys
import os
import unicodedata as ucd
from retrying import retry
from selenium import webdriver
#https://www.shiyinren.com/so?q=+&nsid=4
rooturl="https://www.shiyinren.com/so?q="
weburl="https://www.shiyinren.com"
nsid="&nsid=4"

def get_html(url):
    head = {}
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    # 模拟浏览器，可以简单避免反爬虫
    '''
    response = requests.get(url, headers=head)
    html = response.text
    option = webdriver.ChromeOptions()
    option.add_argument('headless')'''
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    html1=driver.page_source
    with open('test.txt','w',encoding='utf-8') as f:
        f.write(html1)
    resoup = BeautifulSoup(html1, "html.parser")
    title = resoup.find(attrs={'class': 'result f s0'})
    iter1=0
    while not title and not(resoup.find(attrs={'class':'parselinks'}) and resoup.find(attrs={'class':'parselinks'}).has_attr('href')):
        iter1+=1
        if iter1%100==0:
            print("Waiting...Now iters:",iter1)
            if resoup.find(attrs={'class': 'parselinks'}):
                print("Find parselinks ele")
                if resoup.find(attrs={'class':'parselinks'}).has_attr('href'):
                    print("Find link")
        html1=driver.page_source
        resoup = BeautifulSoup(html1, "html.parser")
        driver.implicitly_wait(5)
    # 获取网页编码方式
    # charset = response.info().get_param('charset')
    # html = html.decode(charset)
    with open('test.txt','w',encoding='utf-8') as f:
        f.write(html1)
    driver.quit()
    return html1

def getmusic(song, singer):
    comurl=rooturl+song+'+'+singer+nsid
    print(comurl)
    resoup = BeautifulSoup(get_html(comurl), "html.parser")
    #print("resoup1:", resoup)
    '''title = resoup.find(attrs={'class': 'result f s0'})
    print("title1:",title)
    title = BeautifulSoup(title, "html.parser")'''
    title = resoup.select("div[id='results'] div[class='result f s0'] h3[class='c-title'] a")
    print("title1:",title)
    if len(title)==0:
        return
    desturl=weburl+str(title[0].attrs['href'])
    resoup = BeautifulSoup(get_html(desturl), "html.parser")
    title = resoup.find(attrs={'class': 'parselinks'})
    if len(title)==0:
        return
    print("title2:",title)
    finalurl=str(title.attrs['href'])
    return finalurl



