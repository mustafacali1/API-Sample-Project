from cms_app.models import Category
from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, Path, status
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db())]

