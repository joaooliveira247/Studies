from pydantic import BaseModel, EmailStr
from school.schemas.article_schema import ArticleSchema


class UserSchemaBase(BaseModel):
    id: int | None = None
    name: str
    last_name: str
    email: EmailStr
    is_admin: bool = False

    class Config:
        orm_mode = True


class UserSchemaIn(UserSchemaBase):
    passwd: str


class UserSchemaArticles(UserSchemaBase):
    articles: list[ArticleSchema] | None


class UserSchemaUp(UserSchemaBase):
    name: str | None
    last_name: str | None
    email: EmailStr | None
    passwd: str | None
    is_admin: str | None
