from fastapi import APIRouter
from app.models.array import ArrayOperation, ArrayBase

router = APIRouter(prefix="/array", tags=["Array"])


@router.post("/create")
def create_array(config: ArrayBase):
    pass


@router.post("/insert")
def insert_value(operation: ArrayOperation):
    pass


@router.put("/deletion")
def delete_value(operation: ArrayOperation):
    pass


@router.get("/contains")
def contain_value(operation: ArrayOperation):
    pass


@router.get("/display")
def display_array():
    pass
