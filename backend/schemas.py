from pydantic import BaseModel, Field, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str

    @field_validator('name', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Field cannot be empty or whitespace only')
        return v.strip()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class ProjectCreate(BaseModel):
    title: str
    owner_id: int

    @field_validator('title')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

class ProjectResponse(BaseModel):
    id: int
    title: str
    owner_id: int

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    priority: str = Field(default="medium", pattern="^(low|medium|high)$")
    due_date: Optional[str] = None
    created_at: Optional[str] = None
    project_id: int

    @field_validator('title')
    def validate_title(cls, v):
        if not v or not v.strip():
            raise ValueError("Task title cannot be empty or blank")
        return v.strip()

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    priority: Optional[str] = Field(default=None, pattern="^(low|medium|high)$")
    due_date: Optional[str] = None

    @field_validator('title')
    def validate_title(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Task title cannot be empty or blank")
        return v.strip() if v is not None else v

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    due_date: Optional[str] = None
    created_at: str
    project_id: int

    class Config:
        from_attributes = True


class QuickAddRequest(BaseModel):
    description: str
    project_id: int

    @field_validator('description')
    def validate_desc(cls, v):
        if not v or not v.strip():
            raise ValueError("Description cannot be empty")
        return v.strip()
