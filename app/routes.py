from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import TaskCreate, TaskOut, NoteCreate, NoteOut
from app import crud
from app.auth import get_current_user

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    return await crud.create_task(db, task, user["id"])

@router.get("/tasks", response_model=list[TaskOut])
async def read_tasks(db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    return await crud.get_user_tasks(db, user["id"])

@router.post("/notes", response_model=NoteOut)
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    return await crud.create_note(db, note, user["id"])

@router.get("/notes", response_model=list[NoteOut])
async def read_notes(db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    return await crud.get_user_notes(db, user["id"])