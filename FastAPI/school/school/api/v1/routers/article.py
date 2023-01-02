from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from school.models.__all_models import ArticleModel, UserModel
from school.schemas.article_schema import ArticleSchema
from school.core.dependencies import get_session, get_current_user


router: APIRouter = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ArticleSchema
)
async def post_article(
    article: ArticleSchema,
    user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
) -> ArticleSchema:
    new_article: ArticleModel = ArticleModel(
        title=article.title,
        description=article.description,
        font_url=article.font_url,
        user_id=user.id,
    )
    db.add(new_article)
    await db.commit()

    return new_article


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[ArticleSchema]
)
async def get_articles(
    db: AsyncSession = Depends(get_session),
) -> list[ArticleSchema]:
    async with db as session:
        result = await session.execute(select(ArticleModel))
        articles: list[ArticleModel] = result.scalars().unique().all()

        return articles


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=ArticleSchema
)
async def get_article_by_id(
    id: int, db: AsyncSession = Depends(get_session)
) -> ArticleSchema:
    async with db as session:
        result = await session.execute(
            select(ArticleModel).filter(ArticleModel.id == id)
        )
        article: ArticleModel = result.scalars().unique().one_or_none()

        if not article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found.",
            )
        return article


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=ArticleSchema
)
async def att_article(
    id: int,
    article: ArticleSchema,
    user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
) -> ArticleSchema:
    async with db as session:
        result = await session.execute(
            select(ArticleModel).filter(ArticleModel.id == id)
        )
        article_up: ArticleModel = result.scalars().unique().one_or_none()

        if not article_up:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found.",
            )
        if article.title:
            article_up.title = article.title
        if article.description:
            article_up.description = article.description
        if article.font_url:
            article_up.font_url = article.font_url
        if user.id != article_up.user_id:
            article_up.user_id = user.id

        await session.commit()

        return article_up


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=ArticleSchema,
)
async def delete_article(
    id: int,
    user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
) -> Response:
    async with db as session:
        result = await session.execute(
            select(ArticleModel)
            .filter(ArticleModel.id == id)
            .filter(ArticleModel.id == user.id)
        )
        article_del: ArticleModel = result.scalars().unique().one_or_none()

        if not article_del:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found.",
            )
        await session.delete(article_del)

        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
