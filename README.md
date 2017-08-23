# README

## Requirements

* Ubuntu 16.04
* MySQL 5.7
* virtualenv

---

# Dev Setup

## Dependencies

```
sudo apt-get update
sudo apt-get install python-dev virtualenv build-essential libmysqlclient-dev
```

## MySQL

```
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
```

## Project Setup

```
git clone git clone ...
cd ems2s
virtualenv ve
. ve/bin/activate
pip install -r requirements.pip
```

## DB Setup

```
sudo -u root mysql -p
CREATE DATABASE test CHARACTER SET UTF8;
CREATE USER test@localhost IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON test.* TO test@localhost;
FLUSH PRIVILEGES;
exit

cd /path/to/project/
. ve/bin/activate
./manage.py migrate
./manage.py createsuperuser
```

## Running dev server

```
cd /path/to/project/
. ve/bin/activate
./manage.py runserver
```
