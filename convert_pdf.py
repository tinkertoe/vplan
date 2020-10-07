import tabula
import os
import os.path
import checksum

from set_vars import *


def convert_csv():
    # convert every pdf in filedir to csv
    for pdf_file in os.listdir(filedir):
        if pdf_file.endswith('.pdf'):

            # set paths
            input_path = filedir + pdf_file
            output_path = filedir + pdf_file[:-4] + '.csv'

            # convert file
            tabula.convert_into(input_path, output_path,
                                output_format="csv")



            # remove not needed pdf
            os.system('sudo rm ' + filedir + pdf_file)
