import gevent
import os
import logging

import config
from lib import exist
from lib import sqlite


log = logging.getLogger(__name__)

def save_page(url):
    log.info("prepare to save the url: " + url)
    driver = config.driver_setting()
    driver.get(url) 
    
    width = driver.execute_script(config.SCROLLWIDTH)
    height = driver.execute_script(config.SCROLLHIGHT)
    driver.set_window_size(width, height)
    
    gevent.sleep(1)
    driver.execute_script(config.SCROLLTOPJS);
    gevent.sleep(10)

    res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
    driver_title = driver.title.replace('?', '').replace('|', '')
    
    if exist.driver_title_is_exist(driver_title, url): return ""   

    save_path = config.ROOTPATH + f'/mhtmlfiles/{driver_title}.mhtml'
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    with open(save_path, 'w', newline='') as sf:
        sf.write(res['data'])
    
    sql = '''UPDATE url2html SET title = ?, date = ?, savepath = ? WHERE url = ?'''
    sqlite.execute_sql(sql, (driver_title, config.TIME, save_path, url))
    
    log.info("Everything is Done for: " + url)
    driver.quit()


