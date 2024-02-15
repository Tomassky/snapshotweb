from flask import Flask
from pathlib import Path
from gevent import pywsgi
from flask_bootstrap import Bootstrap
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import multiprocessing
import os


from web_api.files import web_files
from web_api.html import web_html
from web_api.index import web_index
from web_api.wx import web_wx
from tg_api.start import tg_start
from tg_api.url2mhtml import tg_url2mhtml
from tg_api.search4mhtml import tg_search4mhtml
from lib import sqlite
import config



def flask_app():
  
  '''Note: 20240212 flask app, use gevent to serve the app, maybe sometimes it slower than flask'''
  app = Flask(__name__, template_folder='templates')
  Bootstrap(app)
  app.register_blueprint(web_index)
  app.register_blueprint(web_wx)
  app.register_blueprint(web_files, url_prefix='/files')
  app.register_blueprint(web_html, url_prefix='/htmlfiles')
  
  @app.template_filter()
  def file_filter(filefullname, file_name_part):
    if file_name_part == 1:
        return str(Path(filefullname).parent)
    if file_name_part == 2:
        return str(Path(filefullname).name)
  
  server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
  server.serve_forever()
  #app.run(debug=False, host='0.0.0.0', port=5000)

def tg_app():
  
  '''Note: 20240212 tg app, in the same account, the bot just run in a un concurrency way, it cause by the telegram'''
  application = ApplicationBuilder().token(config.BOTTOKEN).build()  
    
  start_handler = CommandHandler('start', tg_start)  
  url2mhtml_handler = CommandHandler('url2mhtml', tg_url2mhtml)
  search4mhtml_handler = CommandHandler('search4mhtml', tg_search4mhtml) 

  application.add_handler(start_handler)  
  application.add_handler(url2mhtml_handler)  
  application.add_handler(search4mhtml_handler)

  application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
  if not os.path.isfile(config.DBPATH): sqlite.init_table()
  import logging
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                      filename='logs.log', 
                      encoding='utf-8', 
                      datefmt='%d/%m/%Y %H:%M:%S',
                      level=logging.DEBUG)
  p1 = multiprocessing.Process(target=flask_app)
  p2 = multiprocessing.Process(target=tg_app)
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
    