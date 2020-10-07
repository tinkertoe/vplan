from PIL import Image, ImageFont, ImageDraw
import datetime
import os

from set_vars import *


def img_gen(school_class):
    def readout_dl(school_class):
        school_class = school_class.replace('_', '/')
        # print debug for current class

        # define return output
        output = ''

        # check every csv file
        for csv_file in os.listdir(filedir):
            if csv_file.endswith('.csv'):

                # set tile from file name
                matching = '\n' + csv_file[:-4] + '\n'

                # open csv
                csv_raw = open(filedir + csv_file, 'r')

                # convert csv to list objects
                csv = csv_raw.read().splitlines()

                for line in csv:
                    # purge weired symbols
                    line = line.encode('iso-8859-1').decode('utf8')
                    if line[1:10].find(school_class) >= 0:

                        # check for blacklisted words
                        if line.find('Achtung') == -1 and line.find('Abwesende') == -1:
                            line = line.replace(',', ' ')
                            # if school_class occurs in list item of csv
                            # add list item to local matching list
                            matching = matching + line + '\n'

                # set output (every local matching combined)
                output = output + matching

        output = output + '\n' + 'Generiert mit vp.tinkertoe.net'
        return output

    school_class = school_class.replace("/", "_")
    time = str(datetime.datetime.now())
    time = time[:-7]
    file_name = school_class + '_' + time + '.png'
    file_name = file_name.replace(" ", "")
    file_link = domain + 'vp_dls/' + file_name
    file_link = file_link.replace(" ", "")

    fnt = ImageFont.truetype('/home/Century_Gothic.ttf', 15)

    temp_im = Image.new('RGB', (600, 600))
    temp_d = ImageDraw.Draw(temp_im)
    w, h = temp_d.textsize(readout_dl(school_class), fnt)
    w = w + 50
    h = h + 50

    img = Image.new('RGB', (w, h), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), readout_dl(school_class),
           font=fnt, fill=(0, 0, 0))
    img.save('/home/web/vplan/screenshots/' + file_name)

    return file_link
