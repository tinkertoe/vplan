from flask import Flask, request, url_for, redirect, render_template, send_from_directory, make_response, abort, flash
import os
import time
import psutil
from random import randint


from dl_vplans import *
from resetfiles import *
from decrypt import *
from tag_pdf import *
from convert_pdf import *
from read_files import *
from set_vars import *
from secret_stuff import *
from readout import *
from db_commands import *
from compare_versions import *


app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key


@app.route('/login')
def login():
    return render_template('login.html', count=read_servicecount())


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():

    pw = request.form['pw']
    resp = make_response(redirect('http://vp.tinkertoe.net'))
    resp.set_cookie('pw', pw, max_age=99999999)
    return resp


@app.route('/')
@app.route('/index')
def index():


    # check pw
    if request.cookies.get('pw') == pdf_password or request.cookies.get('pw') == admin_pw:
        return render_template('index.html', count=read_servicecount())
    else:
        print('WRONG PASSWORD ENTERED AT INDEX')
        return redirect('http://vp.tinkertoe.net/display_flash/login/Falsches%20Passwort!')


@app.route('/vp/<school_class>')
def display_info(school_class):

    print("LAST SERVE: " + str(read_lastserve()))

    # check pw cookie & string length
    if request.cookies.get('pw') == pdf_password and len(school_class) > 0 and len(school_class) <= 4:

        if read_lastserve() < 3:
            return redirect('http://vp.tinkertoe.net/display_flash/index/Geduld,%20bitte%20warte%20mindestens%203sek!')
            return abort(404)

        # CALL FUNCTIONS

        do_update = compare_versions()

        if do_update:
            print("----------------")
            print("UPDATING")
            print("----------------")

            # download vplans
            resetfiles("pdf")
            dl_vplans()

            # decrypt downlaoded vplan
            decrypt_pdf('vplan.pdf')
            # rename pdf afer weekday
            tag_pdf('temp.pdf')

            # decrypt downlaoded vplan
            decrypt_pdf('vplan1.pdf')
            # rename pdf afer weekday
            tag_pdf('temp.pdf')

            # check if pdf is new

            # convert pdf into csv
            resetfiles("csv")
            convert_csv()

        # search for entries with school_class
        return readout(school_class)

    else:
        # PASSWORD ERROR
        if request.cookies.get('pw') != pdf_password:
            print('WRONG PASSWORD ENTERED AT VP INFO')
            return redirect('http://vp.tinkertoe.net/display_flash/login/Falsches%20Passwort!')
        # STRING ERROR
        else:
            return redirect('http://vp.tinkertoe.net/display_flash/index/Das%20ist%20keine%20Klasse!')


@app.route('/credits')
def credits():
    return render_template('credits.html')


@app.route('/display_flash/<func>/<mess>')
def display_flash(func, mess):

    flash(mess)

    if func == 'index':
        return redirect('http://vp.tinkertoe.net')
    else:
        return redirect(url_for(func))


@app.route('/db')
def db():

    if request.cookies.get('pw') == admin_pw:
        return render_template('stats.html', service_count=read_servicecount(), last_serve=read_lastserve(), file_count=count_img())
    else:
        return redirect('http://vp.tinkertoe.net/display_flash/index/Seite%20nicht%20gefunden!')


@app.route('/db/<command>')
def db_command(command):
    if request.cookies.get('pw') == admin_pw:
        return check_command(command)
    else:
        return redirect('http://vp.tinkertoe.net/display_flash/index/Seite%20nicht%20gefunden!')


@app.route('/vp_dls/<filename>', methods=['GET', 'POST'])
def download_files(filename):
    uploads = '/home/web/vplan/screenshots/'
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)


@app.errorhandler(404)
def not_found(error):
    url = str(request.url)
    if url[-1] == "/":
        url = url[0:-1]
        print('LAST URL CHAR IS /')
        print('REDIRECTING TO ' + url)
        return redirect(url)
    else:
        print('PAGE NOT FOUND')
        return redirect('http://vp.tinkertoe.net/display_flash/index/Seite%20nicht%20gefunden!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
