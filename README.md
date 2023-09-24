Datenbank und Web Entwicklung (DBWE) Ergänzungen
===============================================================================

The project contains additions to the [official DBWE source code](https://github.com/dozent2018/IFA_DBWE) with some more examples and code snippets. The source code is delivered as is, under the [MIT License](LICENSE). Feel free to use, share or clone it for your needs.

**Inhalt**
[TOC]

# SQL

## Scripts

| Script                   | Database  | Lehrmittel                     |
| ------------------------ | --------- | ------------------------------ | 
| sql03_base.sql           | course    | 3.  Grundoperationen           |
| sql04_fk.sql             | course    | 4.2 Schlüsselbeziehungen       |
| sql04_fk2-beispiele.sql  | beispiele | 4.3 Select mit Join            |
| sql05_func-beispiele.sql | beispiele | 5.  Funktionen und Gruppierung |
| sql06_sq-beispiele.sql   | beispiele | 6.  Subqueries                 |


## SQL Terminal 

### Start Terminal als Admin (empfohlen)
```
mariadb -u admin -p
``` 
password: admin


### Start Terminal als Root
```
sudo mariadb -u root -p
``` 
password lab: lab
password: [empty]


### Select database to use
``` 
show databases;
create database course;
use course;
``` 

### Load and execute script
``` 
source path/to/your/script.sql;
``` 


# Python

## Scripts

| Script                   | Database  | Lehrmittel                     |
| ------------------------ | --------- | ------------------------------ | 
| hello.py                 | n/a       | 01 Vorbereitungen              |
| db01_config.sql          | beispiele | 18 Zugriff auf Datenbanken     |
| db02_connect.sql         | beispiele | 18 Zugriff auf Datenbanken     |
| db03_select.sql          | beispiele | 18 Zugriff auf Datenbanken     |


##  Conda Befehle

| Command                             | Description                     |
| ----------------------------------- | ------------------------------- | 
| conda --verson                      | Show version |
| conda info --envs                   | Show conda environments |
| conda list                          | Show installed libraries |
| conda install <package>             | Install a package |
| conda update <package>              | Update a package |
| conda create -n <env>               | Create conda environment |
| conda env create -f environment.yml | Create conda environment |
| conda env update -f environment.yml | Update conda environment |
| conda env remove -n <name>          | Remove conda environment |
| pip install <package>               | Install a package |
| pip update <package>                | Update a package |


# Flask

## Apps

| App     | Database  | Lehrmittel  |
| ------- | --------- | ----------- | 
| [blog03](https://github.com/iten-engineering/dbwe/tree/main/flask/blog03)     | n/a  | 01-03 Basistechnologien, Templates                |
| [blog04](https://github.com/iten-engineering/dbwe/tree/main/flask/blog04)     | n/a  | 04 Forms                                          |
| [blog05](https://github.com/iten-engineering/dbwe/tree/main/flask/blog05)     | blob | 05 Datenbanken, Models                            |
| [blog05+](https://github.com/iten-engineering/dbwe/tree/main/flask/blog05%2B) | blob | 05 Datenbanken, Models, DataLoad to/from DB       |
| [blog06](https://github.com/iten-engineering/dbwe/tree/main/flask/blog06)     | blob | 06 Benutzer Login                                 |
| [blog07](https://github.com/iten-engineering/dbwe/tree/main/flask/blog07)     | blob | 07 Benutzer Profile                               |


Fach Architektur (ITAR)
- 08 Fehlerbehandlung
- 09 Follower
- 10 Blog Posts
- 11 E-Mail
- 12 Bootstrap
- 13 Depoyment
- 14 RESTful API


## Lehrmittel Kapitel 5

Sobald die models.py Datei mit der Definition der Klassen User und Post erstellt ist, können mit der SQLite Datenbank Einträge erstellt und abgefragt werden.


1. Open shell, change dir to the project and define the following env variable: 
   ``` 
   export FLASK_APP=blog.py
   ``` 

2. Execute: 
   ``` 
   flask db init
   ``` 

3. Execute: 
   ``` 
   flask db stamp head 
   flask db migrate
   flask db upgrade
   ``` 

   Details siehe: 
   https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date

4. Start SQLite:
   ``` 
   sqlite3 app.db
   ``` 

5. Show schema:
   ``` 
   .schema
   ``` 
   
6. Create class Post and update database:
   ``` 
   flask db migrate
   flask db upgrade
   ``` 
         
7. Start Flask shell:
   ``` 
   flask shell
   ``` 
   
   and show objects:
   ``` 
   db
   User
   Post
   ``` 

8. Create User Sam:
   ``` 
   u = User(username="Sam", email="sam@guru.com")
   db.session.add(u)
   db.session.commit()
   User.query.all()
   User.query.get(1)
   ``` 

9. Create User Anna:
   ``` 
   u = User(username="Anna", email="anna@guru.com")
   db.session.add(u)
   db.session.commit()
   User.query.all()
   User.query.get(2)
   ``` 

10. Show users:
    ``` 
    users = User.query.all()
    for u in users:
       print(u.id, u.username, u.email)
    <enter>
    ``` 

11. Create Posts for user Sam:
    ``` 
    sam = User.query.get(1)
    p = Post(body="My first post", user_id=sam.id)
    db.session.add(p)
    p = Post(body="My second post", user_id=sam.id)
    db.session.add(p)
    db.session.commit()
    Post.query.all()
    ``` 

12. Objekte wieder löschen:
    ``` 
    posts = Post.query.all()
    for p in posts:
      db.session.delete(p)
    <enter>
    Post.query.all()


    users = User.query.all()
    for u in users:
      db.session.delete(u)
    <enter>
    User.query.all()
    ``` 


Weitere Informationen:

- Beispiel von Queries mit und ohne Filter:
  Lehrmittel Seite 75ff

- Versuch mit Maria DB
  Lehrmittel Seite 87ff


## Lehrmittel Kapitel 6

Es muss das bisherige Login ausgebaut werden!


## Lehrmittel Kapitel 7

Achtung bei der DB Migration infolge der neuen User Felder (Lehrmittel Kapitel 7.5), gibt es Probleme mit den Testdaten. Daher muss für die Migration die Daten zuerst gelöscht werden, dann auskommentiert. Nach der Migration können diese wieder wie bisher geladen werden.

Folgende Schritte sind auszuführen:

1. Löschen der Daten
   blog.py: anstelle testdata.load() testdata.clear() einfügen

2. Start Anwendung, jetzt werden die Daten gelöscht. Stop Anwendung

3. blog.py: Das Laden der Daten komplett auskommentieren
   Jetzt kann mit der DB Migration begonnen werden.

4. DB Migration mit:
   flask db migrate -m "Add new user fields."
   flast db upgrade

5. blog.py: Laden der Testdaten wieder einkommentieren. 
   testdata.clear() mit testdata.load() ersetzten

6. Start Anwendung.


# Alias

Die Shell hat folgenden `x` - alias definiert. Damit können die Python Umgebung verwaltet werden, das Login in die DB gemacht werden und einfach in die Projektverzeichnisse gewechselt werden. 

Anzeige aliases 'x':
- alias x='alias | grep x'

Conda environment:
- alias x-activate='conda activate dbwe'
- alias x-create='conda env create -f environment.yml'
- alias x-update='conda env update -f environment.yml'

Database:
- alias xd='conda activate dbwe; cd /home/lab/workspace/dbwe'
- alias xdb='mariadb -u admin -p'
- alias xdbroot='sudo mariadb -u root -p'

Projekte:
- alias xf='conda activate dbwe; cd /home/lab/workspace/dbwe/flask'
- alias xp='conda activate dbwe; cd /home/lab/workspace/dbwe/python'
- alias xs='conda activate dbwe; cd /home/lab/workspace/dbwe/sql'
- alias xw='conda activate dbwe; cd /home/lab/workspace'

---
_The end._



