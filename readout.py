from flask import Flask, request, url_for, redirect, render_template, send_from_directory, make_response, abort, flash
import os
import time
from read_files import *
from service_counter import *
from img_gen import *
from set_vars import *


def readout(school_class):
    # replace _ with /
    school_class = school_class.replace('_', '/')
    # print debug for current class
    print('---------')
    print('Searching for ' + school_class)
    print('---------')

    # define return output
    output = []

    # check every csv file
    for csv_file in os.listdir(filedir):
        if csv_file.endswith('.csv'):

            # set tile from file name
            matching = [csv_file[:-4]]

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
                        # add list item to local matching list
                        matching.append(line)

            # set output (every local matching combined)
            output.append(matching)

    # COUNT SERVICE!
    service_counter()
    print(output)

    last_serve_file = open(filedir + 'last_serve.txt', 'w')
    last_serve_file.write(str(time.time()))

    return render_template('info.html', output=output, count=read_servicecount(), school_class=school_class, file_link=img_gen(school_class))
