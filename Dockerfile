FROM python:slim

ADD blackduck-scan.py /blackduck-scan.py
#RUN wget -O detect.sh https://detect.synopsys.com/detect7.sh
RUN curl -s -L https://detect.synopsys.com/detect7.sh -o detect.sh

RUN pip install --upgrade pip
#RUN pip install PyGithub

WORKDIR /app

ENTRYPOINT ["/blackduck-scan.py"]
