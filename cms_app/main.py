from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# we don't use migration term for using migration with FastAPI
# Only thing we should do is go to main folder in terminal then run 'uvicorn main:app -- reload' powershell code.


models.Base.metadata.create_all(bind=engine)
