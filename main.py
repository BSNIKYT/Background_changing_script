from datetime import datetime
import time
from io import BytesIO
import requests
import os
first_path = os.getcwd()

import pytz
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

import logging

logger = logging.getLogger(__name__)

import logging

logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
logging.warning('This will get logged to a file')


def download_from_github(url):
    try:


        def download_file(url):
            local_filename = url.split('/')[-1]
            with requests.get(url, stream=True, allow_redirects=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return local_filename

        download_file(url)
        pass
    except Exception as err:
        print(err)
download_from_github('https://gist.githubusercontent.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98/raw/f5f9db4f1b287804fd07ffb3296ed0036292bc7a/countryinfo.py')


def time_gh():
    year = str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[0]).replace("-", ".")).split(".")[0]
    month  = str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[0]).replace("-", ".")).split(".")[1]
    day = str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[0]).replace("-", ".")).split(".")[2]
      
    s = str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[1]).split(".")[0]).split(":")[2]
    m = str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[1]).split(".")[0]).split(":")[1]
    h =str(str((str(datetime.now(pytz.timezone('Europe/Moscow')))).split()[1]).split(".")[0]).split(":")[0]
    times = f"{s}s : {m}m : {h}h"
    times2 = f"{day}.{month}.{year}"
    return times,times2


def changing(name_file):

  image = Image.open(name_file)
  w, h = image.size

  ft = 'fs-gravity.ttf'

  do = os.getcwd()
  os.chdir(first_path)
  font = ImageFont.truetype(f"{first_path}/fonts/{ft}", 50)
  os.chdir(do)
  
  drawer = ImageDraw.Draw(image)
  times,times2 = time_gh()
  drawer.text((int((80 * w)/100),80), f"{times2}", font=font, fill='white')
  drawer.text((int((80 * w)/100), 155), f"{times}", font=font, fill='white')
  os.chdir(first_path)
  try:
    image.save('new_img.jpg')
  except OSError:
      pass
  os.chdir(do)
  path = first_path + '\\'+ "new_img.jpg"


  return 'new_img.jpg', name_file

do = os.getcwd()
os.chdir(first_path)

#https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/fonts/Sprite_Graffiti.otf
fonts_name = ['fs-gravity.ttf','Sprite_Graffiti.otf']
if not os.path.exists(os.getcwd() + "/fonts"):
    os.mkdir("fonts")
    os.chdir(os.getcwd() + "/fonts")
    for name in fonts_name:
        download_from_github(f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/fonts/{name}')
else:
    pass



#path='C:\\Users\\Богдан\\Downloads\\anime\\'

import tkinter
import tkinter.filedialog
foldername = tkinter.filedialog.askdirectory()

path = foldername
import ctypes
import os

from ctypes  import *


import random

imgs = []
do = os.getcwd()
posle = path

with os.scandir(path) as listOfEntries: 
            for entry in  listOfEntries:
                if entry.is_file():
                    if (entry.name.endswith("jpg")) or (entry.name.endswith("png")) or (entry.name.endswith("gif")):
                        os.chdir(posle)
                        try:
                            im = Image.open(entry.name)
                            (width, height) = im.size
                            height = int(height)
                            width = int(width)
                            im.close()
                            if width > height:
                                imgs.append(entry.name)
                            else:
                                pass
                        except Exception as err:
                           print(err)
                           pass
import PIL

import time

w = windll.user32.GetSystemMetrics(0)
h = windll.user32.GetSystemMetrics(1)
print(f'''{"*"*80}

Параметры экрана
Высота:{w}
Ширина:{h}

{"*"*80}''')

while True:

            
        try:
            name_file = random.choice(imgs)
            os.chdir(posle)
            with open('name_file.txt', "w") as file_file:
                file_file.write(name_file)




            os.chdir(path)
            im = Image.open(f'{name_file}')
            (width, height) = im.size
            height = int(height)
            width = int(width)
            im.close()

            if width > height:
                global_file_name = name_file
                for i in range(10):
                    os.chdir(posle)
                    with open('name_file.txt') as file_file:
                        data = file_file.read()

                    os.chdir(do)
                    try:
                        os.chdir(posle)
                        #print(f'Path = {os.getcwd()}, name_file = {name_file}, data  = {data}')
                        if name_file != 'new_img.jpg':
                            pass
                        if name_file == 'new_img.jpg':
                            name_file  = data
                        os.chdir(posle)
                        img = Image.open(str(name_file).split("'")[0])

                        new_image = img.resize((int(w), int(h)))

                        new_image.save(str(str(name_file).split("'")[0]))
                        img.close()
                        name_file, do_name_file = changing(name_file)
                        path_img = str(first_path) + "\\"+ str(name_file)
                               
                        ctypes.windll.user32.SystemParametersInfoW(20, 0, path_img, 3)


                    except Exception as err:
                        logger.error(f'{do_name_file} - {err}')
                        pass
                continue
            else:
                pass
            pass

        except IndexError:
            print(f'''{"*"*80}
Не было найдено ни одного подходящего изображения!
Что скрипт смог найти: {imgs}
{"*"*80}''')
            
