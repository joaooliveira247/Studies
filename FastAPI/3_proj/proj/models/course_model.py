from core.config import settings
from sqlalchemy import Column, Integer, String


class CourseModel(settings.DBBASEMODEL):
    __tablename__ = "courses"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    classes: int = Column(Integer)
    time: int = Column(Integer)
