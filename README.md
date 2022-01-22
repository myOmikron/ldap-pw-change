# LDAP Password change tool

## Installation

```bash
apt install nginx python3 python3-pip python3-venv libldap2-dev libsasl2-dev ldap-utils
useradd -m -r -d /usr/sbin/ldap-pw-change -s /bin/bash ldap-pw-change
rm /etc/nginx/sites-available/default
rm /etc/nginx/sites-enabled/default
cp ldap-pw-change.nginx /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/ldap-pw-change.nginx /etc/nginx/sites-enabled/
cp -r ldap_pw_change/ /usr/sbin/ldap-pw-change/
cp requirements.txt /usr/sbin/ldap-pw-change/
chown -R ldap-pw-change: /usr/sbin/ldap-pw-change/
su - ldap-pw-change -c 'python3 -m venv venv'
su - ldap-pw-change -c 'venv/bin/python3 -m pip install -r requirements.txt'
mkdir /var/log/ldap-pw-change/
chown ldap-pw-change: /var/log/ldap-pw-change/
mkdir /etc/ldap-pw-change/
ln -s /usr/sbin/ldap-pw-change/ldap_pw_change/ldap_pw_change/settings.py /etc/ldap-pw-change/
cp gunicorn.conf.py /etc/ldap-pw-change/
cp ldap-pw-change.service /lib/systemd/system/
cp ldap-pw-change.socket /lib/systemd/system/
ln -s /lib/systemd/system/ldap-pw-change.service /etc/systemd/system/multi-user.target.wants/
ln -s /lib/systemd/system/ldap-pw-change.socket /etc/systemd/system/multi-user.target.wants/
systemctl daemon-reload
systemctl enable ldap-pw-change.socket ldap-pw-change.service
systemctl start ldap-pw-change.socket
systemctl start ldap-pw-change.service
systemctl reload nginx
```

## Configuration

In order to use the project following configurations has to be done:
`cp .env.dist ldap_pw_change/.env`

Edit the file and set all values.

In order to generate a `SECRET_KEY`, you can use the following:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

If you plan to use nginx as a reverse proxy, you can use the included nginx file as a reference.


