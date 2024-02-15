from flask import Blueprint, render_template, send_from_directory

import config

web_html = Blueprint('web_html', __name__)

@web_html.route('/<path:filename>') 
def get_image(filename): 
    return send_from_directory(config.HTMLFILES,filename) 