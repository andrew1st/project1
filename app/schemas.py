from pydantic import BaseModel

# Shared Models
class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class NoteBase(BaseModel):
    title: str
    content: str

# Task
class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    class Config:
        from_attributes = True  # instead of orm_mode = True

# Note
class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    class Config:
        orm_mode = True

# User
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True