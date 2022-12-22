from sqlmodel import Field, SQLModel


class CourseModel(SQLModel, table=True):
    __tablename__: str = "courses"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    classes: int
    time: int
