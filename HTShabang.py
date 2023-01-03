import os
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import sys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
##for number values of input get largest possible as fallback 

#while()
#res_fallback["1080p", "720p", "480p", "360p", "240p", "144p"]
#video_fallback["mp4", "webm",]
#audio_fallback["mp3","mp4","webm","mp4a"]

MODE = ""
TYPE = ""
PATH = Path('~\\HTShabang\\').expanduser()
URL = ""


def init():
    global MODE
    global URL
    if len(sys.argv) == 1 :
        print("URL required as argument 1")
        raise Exception("URL required as argument 1")
    elif len(sys.argv) == 2 :
        MODE = "video"
        URL = sys.argv[1]
        input_type(URL)
    elif len(sys.argv) == 3 :
        URL = sys.argv[1]
        input_type(URL)
        MODE = sys.argv[2]
        if (str(MODE).lower != "audio") or (str(MODE).lower != "video") :
            print("Argument 2 should be \"video\" or \"audio\"")
            raise Exception("Argument 2 should be \"video\" or \"audio\"")

        
    if MODE == "playlist" :
        playlist()
    elif MODE == "video" :
        video()

def input_type(url):
    global TYPE
    if url.__contains__("playlist") :
        TYPE = "playlist"
    else :
        TYPE = "video"

def playlist():
    global URL
    o = Options()
    o.add_argument("--headless")
    driver = Firefox(options = o)
    driver.get(URL)
    driver.switch_to.window(driver.current_window_handle)
    driver.implicitly_wait(10)
    #i = 0
    for elem in video_elements :
        href = str(elem.get_attribute('href'))
        if (href != "None") :
            print(str(i))
            current_url = ("https://www.youtube.com" + href)
            get_current(current_url)
            #i = i + 1
        else :
            print('Skipping Empty Video Link')

def video():
    global URL
    o = Options()
    o.add_argument("--headless")
    driver = Firefox(options = o)
    driver.get(URL)
    driver.switch_to.window(driver.current_window_handle)
    driver.implicitly_wait(10)
    get_current(URL)

def get_current(url):
    global MODE
    #print(url)
    if(MODE == "video"):
        get_video(url)
    elif(MODE == "audio"):
        get_video(url)
    #print(video_streams)

def get_video(url):
    video = YouTube(url)
    video_streams = video.streams.filter(file_extension = 'mp4').get_by_itag(22)
    video_streams.download(filename = video.streams[0].title + ".mp4", output_path = PATH)
    print(video.streams[0].title + " Sucesfully Downloaded")
     
def get_audio(url):
    video = YouTube(url)
    audio_stream = video.streams.filter(only_audio=True).first()
    video_streams.download(filename = video.streams[0].title + ".mp3", output_path = PATH)
    print(video.streams[0].title + " Sucesfully Downloaded")
    
init()

