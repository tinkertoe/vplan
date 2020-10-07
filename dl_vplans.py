import os
import checksum

from set_vars import *


def dl_vplans():

    # download vplans
    os.system(
        'wget https://www.barnim-gymnasium.de/fileadmin/schulen/barnim-gymnasium/Dokumente/Pl%C3%A4ne/vplan.pdf')
    os.system(
        'wget https://www.barnim-gymnasium.de/fileadmin/schulen/barnim-gymnasium/Dokumente/Pl%C3%A4ne/vplan1.pdf')

    # move vplans to filedir
    os.system('mv vplan.pdf ' + filedir + 'vplan.pdf')
    os.system('mv vplan1.pdf ' + filedir + 'vplan1.pdf')

    # save checksum

    # remove old files
    for file in os.listdir(filedir):
        if file.endswith(".checksum"):
            os.system("sudo rm " + filedir + file)

    # create files
    os.system("sudo touch " + filedir + "vplan.checksum")
    os.system("sudo touch " + filedir + "vplan1.checksum")

    checksum_file = open(filedir + "vplan.checksum", "w")
    checksum_file.write(str(checksum.get_for_file(filedir + "vplan.pdf")))
    checksum_file.close()

    checksum_file = open(filedir + "vplan1.checksum", "w")
    checksum_file.write(str(checksum.get_for_file(filedir + "vplan1.pdf")))
    checksum_file.close()
