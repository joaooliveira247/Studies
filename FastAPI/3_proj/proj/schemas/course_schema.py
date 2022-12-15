from pydantic import BaseModel as SCBaseModel


class CourseSchema(SCBaseModel):
    id: int | None
    title: str
    classes: int
    time: int

    class Config:
        orm_mode = True

