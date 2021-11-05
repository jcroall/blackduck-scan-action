FROM blackducksoftware/detect:7-buildless

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

ADD blackduck-scan.py /blackduck-scan.py

WORKDIR /app

ENTRYPOINT python3 /blackduck-scan.py
