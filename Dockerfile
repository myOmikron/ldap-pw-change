FROM python:3

WORKDIR /src
RUN apt update && apt install -y libldap2-dev libsasl2-dev ldap-utils && rm -rf /var/lib/apt/lists/*

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD gunicorn.conf.py .
ADD ldap_pw_change/ .

RUN groupadd -r python && useradd --no-log-init -r -g python python
USER python

EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 --access-logfile - --error-logfile - ldap_pw_change.wsgi
