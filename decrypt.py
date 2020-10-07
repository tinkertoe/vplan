import os

from set_vars import *
from secret_stuff import *


def decrypt_pdf(pdf_name):
    # decrypt pdf
    command = 'qpdf --password=' + pdf_password + ' --decrypt ' + \
        filedir + pdf_name + ' ' + filedir + 'temp.pdf'
    os.system(command)

    # remove encrypted file
    os.system('rm ' + filedir + pdf_name)
