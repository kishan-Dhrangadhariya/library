# Library

### Get started with the application
- make sure you have >= python3.7.
- install postgresql using `sudo apt-get install postgresql`
- login into postgresql using following commanacd:
    - `sudo psql --u postgres`
- create a database called library using following command:
    - `CREATE DATABASE library;`
- add a password for postgres user using following command:
    - `ALTER USER postgres WITH PASSWORD 'my_db_password';`
- give permissions for the postgres user for library db using the below command:
    - `GRANT ALL PRIVILEGES ON DATABASE library to postgres;`
- now apply migrations using following command:
    - `python library.py migrate --init`
    - `python library.py migrate --migrate`
    - `python library.py migrate --upgrade`
    
- now you can initiate Library Application with following command:
    - `python library.py run`
