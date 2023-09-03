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


# DTO => Data Transfer Object, UI => User Interface

class CategoryDTO(BaseModel):
    name: str
    description: str = Field(min_length=2, max_length=100)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category_dto: CategoryDTO):
    model = Category()

    model.name = category_dto.name
    model.description = category_dto.description
    model.is_active = True

    db. add(model)
    db.commit()

    return {
        'status_code': 201,
        'transaction': 'Successful'
    }