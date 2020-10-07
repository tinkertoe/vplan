from flask import Flask, request, url_for, redirect, render_template, send_from_directory, make_response, abort, flash
from set_vars import *
from secret_stuff import *
from read_files import *
import os
import time


# define commands
def reset_services():
    servicecount_file_write = open(filedir + 'count.txt', 'w')
    servicecount_file_write.write("0")


def reset_lastserve():
    lastserve_file_write = open(filedir + 'last_serve.txt', 'w')
    lastserve_file_write.write(str(time.time()))


def reset_screenshots():
    os.system('sudo rm /home/web/vplan/screenshots/*')


def check_command(command):
    # run commands
    if command == "r_services":
        reset_services()
        return redirect('http://vp.tinkertoe.net/db')
    if command == "r_lastserve":
        reset_lastserve()
        return redirect('http://vp.tinkertoe.net/db')
    if command == "r_screenshots":
        reset_screenshots()
        return redirect('http://vp.tinkertoe.net/db')
