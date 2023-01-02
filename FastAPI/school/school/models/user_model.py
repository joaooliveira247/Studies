from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from school.core.configs import settings


class UserModel(settings.DB_BASEMODEL):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(256), nullable=True)
    last_name: str = Column(String(256), nullable=True)
    email: str = Column(String(256), index=True, nullable=False, unique=True)
    passwd: str = Column(String(256), nullable=False)
    is_admin: bool = Column(Boolean, default=False)
    articles = relationship(
        "ArticleModel",
        cascade="all, delete-orphan",
        back_populates="post_by",
        uselist=True,
        lazy="joined",
    )
