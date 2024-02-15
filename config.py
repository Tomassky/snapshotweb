from sre_constants import SUCCESS
from selenium import webdriver
import os
from datetime import datetime
import logging

import config
from mhtmlconvert import mhtml

log = logging.getLogger(__name__)

HTMLFILES = "/root/snapshotWeb/htmlfiles/"
MHTMLFILES = "/root/snapshotWeb/mhtmlfiles/"

SCROLLTOPJS = '''{
  let he=setInterval(()=>{
    document.documentElement.scrollTop+=50;
    if(document.documentElement.scrollTop>=(document.documentElement.scrollWidth)){
      clearInterval(he);
      console.log(\"停止\")
    }
  },100);
}'''

SCROLLHIGHT = "return document.documentElement.scrollHeight"

SCROLLWIDTH = "return document.documentElement.scrollWidth"

SUCCESSCONTENT = f"OK! You can get or download it to access the website wait for a moment\n"

HTTPFAILCONTENT = f"Sorry, you provied a wrong URL, please try again later or contact the administrator"

BOTTOKEN = os.getenv('BOTTOKEN', 'default_token')

ROOTPATH = os.path.dirname(__file__)

DBPATH = ROOTPATH + "/db/snapshotweb.db"

TIME = datetime.now().strftime( '%c' )


def driver_setting():
    options = webdriver.ChromeOptions()
    options.binary_location = "/root/chrome-headless-shell-linux64/chrome-headless-shell"
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    '''In Container should add this option to avoid the error'''
    options.add_argument("--disable-dev-shm-usage")
    driver_path = r"/root/chromedriver-linux64/chromedriver"
    service = webdriver.ChromeService(executable_path = driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def transform_mhtml_to_html(driver_title):
    mhtml_prefix = MHTMLFILES
    html_prefix = HTMLFILES
    mhtml.mhtml_to_html(mhtml_prefix + driver_title + ".mhtml", html_prefix + driver_title + ".html", "./" + driver_title +"/")
    
def return_user(xml_dict, content):
  log.info(xml_dict)
  from_user_name = xml_dict.get("FromUserName")
  to_user_name = xml_dict.get("ToUserName")
  return_string = f'''
  <xml>
    <ToUserName><![CDATA[{from_user_name}]]></ToUserName>
    <FromUserName><![CDATA[{to_user_name}]]></FromUserName>
    <CreateTime>123456</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{content}]]></Content>
  </xml>
    '''
  return return_string