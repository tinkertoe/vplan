from set_vars import *
import os
import time


def read_lastserve():

    last_serve_file = open(filedir + 'last_serve.txt', 'r')
    last_serve = time.time() - float(last_serve_file.read())
    return last_serve


def read_servicecount():
    # read count
    count_file = open(filedir + 'count.txt', 'r')

    # str to int
    count = str(count_file.read())

    return count


def count_img():
    img_count = 0
    for img in os.listdir('/home/web/vplan/screenshots/'):
        img_count = img_count + 1
    return str(img_count)
