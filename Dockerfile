FROM python:slim

ADD blackduck-scan.py /blackduck-scan.py
RUN wget -O detect.sh https://detect.synopsys.com/detect7.sh

RUN pip install --upgrade pip
#RUN pip install PyGithub

WORKDIR /app

ENTRYPOINT ["/blackduck-scan.py"]
