FROM python:3.10.12
WORKDIR ./root/snapshotWeb
ADD . .
RUN apt-get update
RUN apt-get install -y libatk-bridge2.0-0 libgtk-3.0 libasound2 libatk1.0-0 libgbm-dev libnss3-dev
RUN pip install -r requirements.txt
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chrome-headless-shell-linux64.zip -P /root/
RUN unzip -o /root/chrome-headless-shell-linux64.zip -d /root/
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip -P /root/
RUN unzip -o /root/chromedriver-linux64.zip -d /root/

CMD ["python3", "app.py"]
