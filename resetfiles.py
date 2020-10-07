import os

from set_vars import *


def resetfiles(ending):
    for pdf_file in os.listdir(filedir):
        if pdf_file.endswith("." + ending):
            os.system('sudo rm ' + filedir + pdf_file)
