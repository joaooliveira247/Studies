from pydantic import BaseModel


class Curso(BaseModel):
    title: str
    classes: int
    time: int
