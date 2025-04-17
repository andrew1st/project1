from sqlalchemy.future import select
from app.models import Task, Note
from app.schemas import TaskCreate, NoteCreate

# TASKS
async def create_task(db, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_user_tasks(db, user_id: int):
    result = await db.execute(select(Task).where(Task.owner_id == user_id))
    return result.scalars().all()

# NOTES
async def create_note(db, note: NoteCreate, user_id: int):
    db_note = Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    await db.commit()
    await db.refresh(db_note)
    return db_note

async def get_user_notes(db, user_id: int):
    result = await db.execute(select(Note).where(Note.owner_id == user_id))
    return result.scalars().all()