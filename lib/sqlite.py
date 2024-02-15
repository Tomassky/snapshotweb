import sqlite3

import config

def execute_sql(sql, params=()):
  with sqlite3.connect(config.DBPATH) as conn:
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()

def query_sql(sql, params=()):
  with sqlite3.connect(config.DBPATH) as conn:
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

"""Note: 20240212, the execute_sql_script function is a simple way to execute a sql script for init_table function"""
def execute_sql_script(sql, params=()):
  with sqlite3.connect(config.DBPATH) as conn:
    conn.executescript(sql)
      
def init_table():
  sql_for_url_to_mhtml = '''
  create table if not exists url2html(
    id integer primary key autoincrement,
    url text,
    title text,
    date text,
    savepath text
  )
  '''
  sql_for_black_title = '''
  create table if not exists blacktitle(
    title text,
    status text
  );
  insert into blacktitle(title, status) values('微信公众号平台','true');
  insert into blacktitle(title, status) values('安全验证 - 知乎','true')
  '''
  execute_sql_script(sql_for_url_to_mhtml)
  execute_sql_script(sql_for_black_title)
  
