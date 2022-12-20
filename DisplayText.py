#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import datetime
import random
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
mypicdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'mypic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd5in65f Demo")
    
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font24 = ImageFont.truetype(os.path.join(mypicdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(mypicdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(mypicdir, 'Font.ttc'), 30)
    font60 = ImageFont.truetype(os.path.join(mypicdir, 'Font.ttc'), 60)

#    logging.info("3.read bmp file")
#    Himage = Image.open(os.path.join(picdir, 'pix-p250.bmp'))
#    epd.display(epd.getbuffer(Himage))
#    time.sleep(10)

    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))


    filelist = []

    for path in os.listdir(picdir):
        if os.path.isfile(os.path.join(picdir, path)):
            filelist.append(path)

    print("Printing the list of images...")
    for x in filelist:
	print(x)

    for x in filelist:
        logging.info("1.Displaying Picture...")
        Himage = Image.open(os.path.join(picdir,x))
	print("Displaying Picture...",x)
        now = datetime.datetime.now()
        draw = ImageDraw.Draw(Himage)
        draw.text((0, 0), (now.strftime("%Y-%m-%d %H:%M:%S")), font = font24, fill = epd.WHITE)
        epd.display(epd.getbuffer(Himage))
        sleepytime = (random.randrange(1000,2000))
        print("Sleeping for ",sleepytime," seconds...")
        time.sleep(sleepytime)

#    epd.Clear()
#    logging.info("Goto Sleep...")
#    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in65f.epdconfig.module_exit()
    exit()
