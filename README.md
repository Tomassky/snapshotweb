<h1 align="center">snapshotweb</h1>

<p align="center">
🔥 Take a snapshot for the website and search it
</p>

## feature

- wechat official account and telegram bot
- sqlite to store information
- can deploy in source、docker or k8s
- many fault tolerance mechanisms
- and .....

## API

### web_api

- `/index`, is used to display the application work
- `/files/readfile`, is used to read the file remotely
- `/files/list`, is used to list the mhtml file in mhtmlfiles directory
- `/files/saveasmhtml`, is used to transform the url to mhtml file
- `/files/downloadfile`, is used to download the mhtml file
- `/wx`, is used for wechat official account

### tg_api

- `/start`, is used to test the connection
- `/url2mhtml`, like the interface `/files/saveasmhtml`
- `/search4mhtml`, is used to search for the input content is exist in the mhtmlfiles directory

## Source Install

### Install(ubuntu22.04-Jammy + Python 3.10.12)

```
mkdir /root/
git clone https://github.com/Tomassky/snapshotweb.git

# Dependeny
apt-get update
apt-get install -y libatk-bridge2.0-0 libgtk-3.0 libasound2 libatk1.0-0 libgbm-dev libnss3-dev

# Python Dependency
pip install -r requirements.txt/python3 setup.py install

# Chrome Kenerl and Chromedriver
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chrome-headless-shell-linux64.zip -P /root/
unzip -o /root/chrome-headless-shell-linux64.zip -d /root/
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip -P /root/
unzip -o /root/chromedriver-linux64.zip -d /root/
```

remember to replace file `config.py` or insert the os env

![](/images/images-1.png)

the you can run the command `python3 app.py`, the service will be start

## Docker Install

There is a Dockerfile in the directory, and you can use the below command to build or run it

```
mkdir /root/
git clone https://github.com/Tomassky/snapshotweb.git

# Sync the time
ntpdate -u time.pool.aliyun.com

# Clean the cache(maybe is unnecessary)
sudo docker system prune -a --force
sudo docker system df

# Build it
sudo docker build -t snapshotweb:v1 .

# Run it
sudo docker run -d -p 5000:5000 -v /root/snapshotweb/mhtmlfiles/:/root/snapshotweb/mhtmlfiles/ -v /root/snapshotweb/db/:/root/snapshotweb/db/ -e BOTTOKEN=x snapshotweb:v1
```

The below image show the container run and the builed container

![](/images/images-3.png)

![](/images/images-2.png)

## K8S deploy

There is a directory called k8s, include two pvc, one secret, one deployment and one service yame files, remember to replace the secret file with the BOTTOKEN variables

![](/images/images-5.png)

![](/images/images-4.png)

or you can deploy it in GUI k8s controller like kubesphere

the pod, include two pvc

![](/images/images-6.png)

the service, to expose the port 31888 use the NodePort

![](/images/images-7.png)

also you should push the container to the container hub

```
docker login
docker images
docker tag imagesID tomassky/snapshotweb-v1
docker pull tomassky/snapshotweb-v1:latest
docker inspect tomassky/snapshotweb-v1
```

![](/images/images-12.png)

## Note

The default port is 5000, you can change it as you want

![](/images/images-8.png)

![](/images/images-9.png)

The Telegram bot has three commands

![](/images/images-11.png)

![](/images/images-10.png)

## Bug

This project is simple and just use one method to save the webpage, maybe have many bugs, you can issue me or contract me with the email(tomassky7@gmail.com)

Finally, thans the project(https://github.com/arnaudrevel/MHTMLconverter), i use his/her codes

emmm....英语写得有点烂，第一次尝试，见谅见谅


