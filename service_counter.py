import os

from set_vars import *


def service_counter():
    # read count
    count_file = open(filedir + 'count.txt', 'r')

    # str to int
    count = int(count_file.read())
    # add 1 to count
    count = count + 1

    # write new count to file
    count_file_write = open(filedir + 'count.txt', 'w')
    count_file_write.write(str(count))

    # debug count
    print('SERVICE COUNTER: ' + str(count))
