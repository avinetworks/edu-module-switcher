FROM alpine:latest
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install avisdk python-owasp-zap-v2.4 jupyter
EXPOSE 6789
CMD ./start.sh