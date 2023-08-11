import logging
from typing import List
from fastapi import Depends, HTTPException, Request
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db


router = InferringRouter()


@router.get("/ht", tags=["healthcheck"])
def ht():
    return {"detail": "ок"}


@router.get("/find", response_model=List[schemas.FindBase], tags=["find"])
async def get_find(
        hash: str,
        db: Session = Depends(get_db),
):
    db_find = crud.get_find(db=db, hash=hash)
    if db_find is None:
        raise HTTPException(status_code=404, detail="Записи не найдены")
    return db_find


@router.post("/find", response_model=List[schemas.FindBase], tags=["find"])
async def post_find(
        request: Request,
        db: Session = Depends(get_db)
):
    db_sub = await crud.post_find(
        db=db,
        request=request
    )
    if db_sub is None:
        raise HTTPException(status_code=404, detail="Записи не найдены")
    return db_sub


@router.post("/problems/", tags=["find"])
async def post_problems(
        request: Request,
        db: Session = Depends(get_db)
):
    return await crud.post_problems(
        db=db,
        request=request
    )
