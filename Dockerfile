FROM ubuntu:bionic
RUN apt-get update && apt-get install -y bash curl python-dev python-pip libssl-dev libffi-dev
RUN pip install pandas==0.21.0 gunicorn falcon ansible==2.9.14 ansible_runner avisdk avimigrationtools netaddr pyvmomi
RUN ansible-galaxy install avinetworks.avisdk avinetworks.aviconfig
RUN mkdir /opt/falcon_runner
COPY falcon_runner /opt/falcon_runner
RUN mkdir /opt/modules
COPY modules /opt/modules
EXPOSE 5000
RUN echo '#!/bin/bash' > /opt/falcon_runner/gunicorn.sh
RUN echo 'gunicorn app:api -b 0.0.0.0:5000 --timeout 1800 --chdir /opt/falcon_runner' >> /opt/falcon_runner/gunicorn.sh
RUN chmod a+x /opt/falcon_runner/gunicorn.sh
CMD ["/opt/falcon_runner/gunicorn.sh"]
