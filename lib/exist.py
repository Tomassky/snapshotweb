import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import config
from lib import sqlite
from lib import save

log = logging.getLogger(__name__)

def url_is_exist(url):
  try:
    sql = '''SELECT id FROM url2html WHERE url = ?'''
    sql_result = sqlite.query_sql(sql, (url,))
    if sql_result:
      return True
    else:
      sql = '''INSERT INTO url2html(url) VALUES(?)'''
      sqlite.execute_sql(sql, (url,))
      return False
  except Exception as exp:
    log.error(exp)
    return False


def driver_title_is_exist(driver_title, url):
  try:
    sql = '''SELECT status FROM blacktitle WHERE title = ?'''
    sql_result = sqlite.query_sql(sql, (driver_title,))[0][0]
    if sql_result:
      sql = '''DELETE FROM url2html WHERE url = ?'''
      sqlite.execute_sql(sql, (url,))
      return True
  except Exception as exp:
    log.error(exp)
  return False        

   
def url_is_access(driver_title):
  try:
    sql = '''SELECT url FROM url2html WHERE title = ?'''
    """Note: 20240215 just get the first one, but maybe it has more than one url, so it need to be improved in the future."""
    url = sqlite.query_sql(sql, (driver_title,))[0][0]
    
    driver = config.driver_setting()
    driver.get(url) 
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
    driver_title_get = driver.title.replace('?', '').replace('|', '')
    
    if driver_title == driver_title_get:
      return url
  except Exception as exp:
    log.error(exp)
  return False