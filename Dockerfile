FROM python:3.6

COPY entrypoint.sh requirements.txt src /usr/src/

WORKDIR /usr/src

RUN apt-get update && apt-get install -y chromium unzip --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/list/* && \
    pip install --no-cache-dir -r /usr/src/requirements.txt && \
    curl https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip -O && \
    unzip chromedriver_linux64.zip && \
    rm chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin

ENTRYPOINT [ "/usr/src/entrypoint.sh" ]
