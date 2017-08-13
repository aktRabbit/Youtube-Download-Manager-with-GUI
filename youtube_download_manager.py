import requests
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from bs4 import BeautifulSoup
from pytube import YouTube

app=QApplication(sys.argv)
song, ok=QInputDialog.getText(None,"Song","Enter the song :")
word_list=list(map(str,song.split(" ")))
got_song=""
co=0;
for i in word_list:
    got_song+=i
    co+=1
    if co!=len(word_list):
        got_song+='+'

url="https://www.youtube.com/results?search_query="
url+=got_song
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
title=[]
links=[]
dic={}
co=0
for link in soup.find_all('a' , class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link '):
    links.append(link.get("href"))
    title.append(link.text)
    dic[link.text]=co
    co+=1
item,okPressed =QInputDialog.getItem(None,"Videos","Select :",title,0,False)
if okPressed:
    print(item)
url1="https://www.youtube.com"
url1+=links[dic[item]]
print(url1)
video=YouTube(url1)
quality=video.get_videos()
qual=[]
akt={}
co=0
for i in range(len(quality)):
    ss=quality[i].extension+" "+quality[i].resolution
    qual.append(ss)
    akt[ss]=co
    co+=1
choice, ok=QInputDialog.getItem(None,"Video","Select the Resolutions :",qual,0,False)
download=QMessageBox.question(None,"Download Manager","Do you want to Start download",QMessageBox.Yes|QMessageBox.No)
if download==QMessageBox.Yes:
    QMessageBox.question(None,"Download Manager","Video downloading",QMessageBox.Ok)
    vi=video.get(quality[akt[choice]].extension,quality[akt[choice]].resolution)
    vi.download('/home/akt/Downloads')
    QMessageBox.question(None,"Download Manager","Download Complete",QMessageBox.Ok)

