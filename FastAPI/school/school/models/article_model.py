from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from school.core.configs import settings


class ArticleModel(settings.DB_BASEMODEL):
    __tablename__ = "articles"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(256))
    description: str = Column(String(256))
    font_url: str = Column(String(256))
    user_id: int = Column(Integer, ForeignKey("users.id"))
    post_by = relationship(
        "UserModel", back_populates="articles", lazy="joined"
    )
