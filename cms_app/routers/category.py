from models import Category
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


db_dependency = Annotated[Session, Depends(get_db)]


class CategoryDTO(BaseModel):
    name: str
    description: str = Field(min_length=2, max_length=100)


@router.post(path='/category', status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category_dto: CategoryDTO):
    model = Category()

    model.name = category_dto.name
    model.description = category_dto.description
    model.is_active = True

    db.add(model)
    db.commit()

    return {
        'status_code': 201,
        'transaction': 'Successful'
    }


@router.get(path='/', status_code=status.HTTP_200_OK)
async def get_all_categories(db: db_dependency):
    return db.query(Category).all()


@router.get(path='/category/{category_id}', status_code=status.HTTP_200_OK)
async def get_category_by_id(db:db_dependency, category_id: int= Path(gt=0)):
    category_model = db.query(Category).filter(Category.id == category_id).first()

    if category_model is not None:
        return category_model

    raise HTTPException(
        status_code=404,
        detail='Category not found'
    )

