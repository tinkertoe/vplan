import pdftotext
import os

from set_vars import *


def tag_pdf(pdf_name):


    # Load your PDF
    with open(filedir + pdf_name, "rb") as f:
        pdf = pdftotext.PDF(f)

    # Read all the text into one string
    pdf_text = "\n\n".join(pdf)
    pdf_text = pdf_text[:500]

    # tag day after day
    if 'Montag' in pdf_text:
        os.system('mv ' + filedir + 'temp.pdf' +
                  ' ' + filedir + 'Montag.pdf')
    if 'Dienstag' in pdf_text:
        os.system('mv ' + filedir + 'temp.pdf' +
                  ' ' + filedir + 'Dienstag.pdf')
    if 'Mittwoch' in pdf_text:
        os.system('mv ' + filedir + 'temp.pdf' +
                  ' ' + filedir + 'Mittwoch.pdf')
    if 'Donnerstag' in pdf_text:
        os.system('mv ' + filedir + 'temp.pdf' +
                  ' ' + filedir + 'Donnerstag.pdf')
    if 'Freitag' in pdf_text:
        os.system('mv ' + filedir + 'temp.pdf' +
                  ' ' + filedir + 'Freitag.pdf')
    os.system('rm ' + filedir + 'temp.pdf')
