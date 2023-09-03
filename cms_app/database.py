# this .py file's aim is create connection with SQL server

# We will take instance then we will use in CRUD operations

# FastAPI Doc
# https://fastapi.tiangolo.com/

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# we add a variable to keep database's location (dir)
SQLALCEMY_DATABASE_URL = 'sqlite:///./.cms.db'

# SQLALCMY_ORM is use for to configure how the connection will be between web app and database. We will use imported
# function above 'create_engine'.

engine = create_engine(
    SQLALCEMY_DATABASE_URL,
    connect_args={
        'check_same_thread': False
    }
)

# we will create session with the function we imported above 'sessionmaker()' then we will run our CRUD operations on
# this active session

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# bind => it connects the new session object and new engine
# autoflush => it clears the settings for every new session object
# autocommit => when we use SQLAlchemy without autocommit we manage function calling operations manually.

# We create an object with using declarative_base(). We create this object to help us to collect functions we need in
# the project.

Base = declarative_base()
