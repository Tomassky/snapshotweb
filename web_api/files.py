from flask import Blueprint, render_template, request, send_from_directory, url_for, redirect
from pathlib import Path
import os
import logging

import config
from lib import exist

log = logging.getLogger(__name__)


web_files = Blueprint('web_files', __name__)

@web_files.route('/readfile')
def read_file():
    filename_mhtml = request.args.get('filename', default = '*', type = str)
    filename = filename_mhtml[:-6]
    
    url = exist.url_is_access(filename)
    if url:
      log.info("website is still alive,can access to the url" + url)
      return redirect(url)
    else:
      log.info("website is not alive, so translate and read the file: " + filename_mhtml)
      config.transform_mhtml_to_html(filename)
      filename_html = "".join([filename, ".html"])
      return send_from_directory(config.HTMLFILES, filename_html)
  

@web_files.route('/downloadfile')
def download_file():
    filename_suffix = request.args.get('filename', default = '*', type = str)
    log.info("someone download the file: " + config.MHTMLFILES + filename_suffix)
    return send_from_directory(config.MHTMLFILES, filename_suffix)


@web_files.route('/list')
def list_file():
    file_ele_list = []
    dir_ele_list = []
    mhtml_files_list = "".join([config.ROOTPATH, '/mhtmlfiles/'])
    len_mhtml_files_list = len(mhtml_files_list)
    
    for f in Path(mhtml_files_list).iterdir():
      fullname = str(f).replace('\\', '/')
      filename = fullname[len_mhtml_files_list:]
      if f.is_file():
        file_ele_list.append({'is_dir': 0, 
                              'filesize': os.path.getsize(f) / 1000000,
                              'url': url_for('web_files.read_file', filename=filename), 
                              'fullname': fullname,
                              'download_url': url_for('web_files.download_file', filename=filename)})
      if f.is_dir():
        fullname = str(f).replace('\\', '/')
        dir_ele_list.append({'is_dir': 1, 
                              'filesize': 0, 
                              'url': url_for('web_files.list_file', files_dir=fullname),
                              'fullname': fullname})

    return render_template('dir_view.html', ele_list=dir_ele_list + file_ele_list)

'''Note: 20240127 I deprecate this route beacause i use the interface from wechat
@web_files.route("/saveasmhtml")
def save_as_mhtml():
    try:
      urls = request.args.get('url', default = '*', type = str)
      save.save_page(urls)
      return redirect(url_for('web_files.list_file'))
    except Exception as exp:
      return exp
'''




