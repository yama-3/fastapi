from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import schemas.task as task_schema
import cruds.task as task_crud
from db import SessionLocal

router = APIRouter()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="１つ目のTODOタスク")]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_crud.create_task(db, task)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return
