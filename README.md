# Access Mobile
Our team's Hack the Change 2024 hackathon project.

# Getting Started
## DB connectivity
You must [download and install PostgreSQL Command Line Tools](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) in order to connect to a shared remote database, or run your own PostgresSQL Server to run your own database.

You also need to add the PostgreSQL command line tools to your `PATH` environment variable. We currently use PostgreSQL 17 command line tools, so add `C:\Program Files\PostgreSQL\17\bin\` to `PATH`. [Windows Example](https://stackoverflow.com/a/72840768/1873164).

If you are not using a shared remote database that is already setup, you will have to create your own database in PostgreSQL 17. Once your DB server is running, connect via your favourtie DB tool (ex. pgAdmin 4) and run the following SQL command:
```sql
CREATE DATABASE amobile;
```

## Install Python Dependencies
Create a [virtual environment in VSCode](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command) or through command line.

For command line, in the root repo directory:
```bash
python -m venv .venv
```

Then install the pip dependencies:
```bash
pip install -r requirements.txt
```

## Create a .env file
Create a .env file in the root of this repo. Copy the environment variables specified in [access_mobile/settings.py](access_mobile/settings.py) to .env.

Update the following variables to your own DB settings:
```env
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Update any DB tables required for our Django server
```bash
python manage.py migrate
```

## Run the Django Server
```bash
python manage.py runserver
```
