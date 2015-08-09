# Interval-Scheduling-Algorithm-with-Applied-Constraints




###Dependencies:

- Scrapy (Python web scraping package)

```sudo pip install scrapy```

- Network X (Python network graph tools)

```sudo pip install networkx```

- Peewee (Database interface)

```sudo pip install peewee```

- MySQLdb

```sudo apt-get install python-mysqldb```

- Bottle (Simple Webserver Package)

```sudo pip install bottle```


###MySQL Statements to Prepare

To use the webserver out of the box, start the mysql client:

```mysql -u <user>```

(by default, <user> will be 'root')

Run the following commands:

```CREATE DATABASE MyCampusSections;```

```CREATE USER 'hackweek'@'localhost' IDENTIFIED BY 'hackweekteam';```

```GRANT ALL PRIVILEGES ON MyCampusSections.* TO 'hackweek'@'localhost';```

```FLUSH PRIVILEGES;```

