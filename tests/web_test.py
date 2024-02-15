import app as flask_app
import pytest



xml_data1 = '''
<xml>
<ToUserName><![CDATA[gh_xxxx]]></ToUserName>  <FromUserName><![CDATA[xxxUpY]]></FromUserName> 
<CreateTime>1675747313</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Content><![CDATA[https://mp.weixin.qq.com/s?__biz=MjM5MTYxNjQxOA==&mid=2652889588&idx=1&sn=1afe95b49f1645407e4a218cf187fcba&chksm=bd599d398a2e142f7af13f39c79a7f08144649749a5ee959e851b4bac037cef3b0d69121a0f3#rd]]></Content>
</xml>
'''

xml_data2 = '''
<xml>
<ToUserName><![CDATA[gh_xxxx]]></ToUserName>  <FromUserName><![CDATA[xxxUpY]]></FromUserName> 
<CreateTime>1675747313</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Content><![CDATA[https://xz.aliyun.com/t/13102?time__1311=mqmxnDBDcD0A37KDsQoYK0%3DQG%3DKuDLTgTD]]></Content>
</xml>
'''

xml_data3 = '''
<xml>
<ToUserName><![CDATA[gh_xxxx]]></ToUserName>  <FromUserName><![CDATA[xxxUpY]]></FromUserName> 
<CreateTime>1675747313</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Content><![CDATA[https://csdnnews.blog.csdn.net/article/details/135891430?spm=1000.2115.3001.5927]]></Content>
</xml>
'''


@pytest.fixture()
def app():
  app = flask_app.main()
  yield app
  
@pytest.fixture()
def client(app):
  return app.test_client()

def test_index(app, client):
  response = client.post("/wx", data = xml_data1)
  assert response.status_code == 200
  #response = client.post("/wx", data = xml_data2)
  #assert response.status_code == 200
  #response = client.post("/wx", data = xml_data3)
  #assert response.status_code == 200