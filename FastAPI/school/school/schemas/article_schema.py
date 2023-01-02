from pydantic import BaseModel, HttpUrl


class ArticleSchema(BaseModel):
    id: int | None = None
    title: str
    description: str
    font_url: HttpUrl
    user_id: int | None

    class Config:
        orm_mode = True
