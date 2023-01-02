from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from school.models.__all_models import UserModel
from school.schemas.user_schema import (
    UserSchemaIn,
    UserSchemaUp,
    UserSchemaBase,
    UserSchemaArticles,
)
from school.core.dependencies import get_current_user, get_session
from school.core.security import gen_hash
from school.core.auth import authenticate, gen_acess_token


router = APIRouter()


@router.get("/logged", response_model=UserSchemaBase)
def get_logged(user_logged: UserModel = Depends(get_current_user)):
    return user_logged


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSchemaBase,
)
async def sign_up_user(
    user: UserSchemaIn, db: AsyncSession = Depends(get_session)
) -> UserSchemaBase:
    new_user: UserModel = UserModel(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        passwd=gen_hash(user.passwd),
        is_admin=user.is_admin,
    )
    async with db as session:
        session.add(new_user)
        await session.commit()
        return new_user


@router.get("/", response_model=list[UserSchemaBase])
async def get_users(
    db: AsyncSession = Depends(get_session),
) -> list[UserSchemaBase]:
    async with db as session:
        result = await session.execute(select(UserModel))
        users: list[UserModel] = result.scalars().unique().all()

        return users


@router.get(
    "/{id}", response_model=UserSchemaArticles, status_code=status.HTTP_200_OK
)
async def get_user(
    id: int, db: AsyncSession = Depends(get_session)
) -> UserSchemaBase:
    async with db as session:
        result = await session.execute(
            select(UserModel).filter(UserModel.id == id)
        )
        if not (user := result.scalars().unique().one_or_none()):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )
        return user


@router.put(
    "/{id}",
    response_model=UserSchemaBase,
    status_code=status.HTTP_202_ACCEPTED,
)
async def att_user(
    id: int, user: UserSchemaUp, db: AsyncSession = Depends(get_session)
) -> UserSchemaBase:
    async with db as session:
        result = await session.execute(
            select(UserModel).filter(UserModel.id == id)
        )
        if not (user_up := result.scalars().unique().one_or_none()):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )
        if user.name:
            user_up.name = user.name
        if user.last_name:
            user_up.last_name = user.last_name
        if user.email:
            user_up.email = user.email
        if user.is_admin:
            user_up.is_admin = user.is_admin
        if user.passwd:
            user_up.passwd = gen_hash(user.passwd)
        await session.commit()
        return user_up


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    id: int, db: AsyncSession = Depends(get_session)
) -> UserSchemaBase:
    async with db as session:
        result = await session.execute(
            select(UserModel).filter(UserModel.id == id)
        )
        if not (user := result.scalars().unique().one_or_none()):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
            )
        await session.delete(user)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session),
):
    user = await authenticate(
        email=form_data.username, passwd=form_data.password, db=db
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User or password wrong.",
        )
    return JSONResponse(
        content={
            "access_token": gen_acess_token(sub=user.id),
            "token_type": "bearer",
        },
        status_code=status.HTTP_200_OK,
    )
