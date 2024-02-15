from flask import Blueprint, render_template, request
import xmltodict
import logging
import config

from lib import save, exist

log = logging.getLogger(__name__)
web_wx = Blueprint('web_wx', __name__)

@web_wx.route("/wx", methods=["GET","POST"])
def index():
  signature = request.args.get('signature')
  timestamp = request.args.get('timestamp')
  nonce = request.args.get('nonce')
  echostr = request.args.get('echostr')
  try:
    xml_to_dct = xmltodict.parse(request.data)
    xml_dict = xml_to_dct.get("xml")
    
    url = xml_dict.get("Content")
    if url and url.startswith('http') and url.count('://') == 1:
      if exist.url_is_exist(url): return config.return_user(xml_dict, config.SUCCESSCONTENT)
      save.save_page(url)
      return ""
    else:
      return config.return_user(xml_dict, config.HTTPFAILCONTENT)
  except Exception as Argument:
      log.error(Argument)
      return config.return_user(xml_dict, config.HTTPFAILCONTENT)
