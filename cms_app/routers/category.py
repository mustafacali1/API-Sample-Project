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


# DTO => Data Transfer Object

@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category_dto: CategoryDTO):
    pass
