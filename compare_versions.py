import checksum
import os
from resetfiles import *


def compare_versions():
    # download vplans
    os.system(
        'wget https://www.barnim-gymnasium.de/fileadmin/schulen/barnim-gymnasium/Dokumente/Pl%C3%A4ne/vplan.pdf')
    os.system(
        'wget https://www.barnim-gymnasium.de/fileadmin/schulen/barnim-gymnasium/Dokumente/Pl%C3%A4ne/vplan1.pdf')

    # move vplans to filedir
    os.system('mv vplan.pdf ' + filedir + 'vplan.pdf')
    os.system('mv vplan1.pdf ' + filedir + 'vplan1.pdf')

    newVersion = False

    # DEBUG
    print("--------------------")

    # vplan
    new_checksum = str(checksum.get_for_file(filedir + "vplan.pdf"))
    old_checksum = open(filedir + "vplan.checksum", "r")
    old_checksum = old_checksum.read()

    # DEBUG
    print("VPLAN:")
    print("old_checksum: " + old_checksum)
    print("new_checksum: " + new_checksum)

    if new_checksum != old_checksum:
        newVersion = True

    # vplan1
    new_checksum = str(checksum.get_for_file(filedir + "vplan1.pdf"))
    old_checksum = open(filedir + "vplan1.checksum", "r")
    old_checksum = old_checksum.read()

    # DEBUG
    print("VPLAN1:")
    print("old_checksum: " + old_checksum)
    print("new_checksum: " + new_checksum)

    if new_checksum != old_checksum:
        newVersion = True

    # DEBUG
    print("--------------------")

    # delete pdfs
    resetfiles("pdf")

    return newVersion
