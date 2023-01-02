from typing import Generator
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from school.core.database import Session
from school.core.auth import oauth2_schema
from school.core.configs import settings
from ..models.user_model import UserModel


class TokenData(BaseModel):
    username: str | None = None


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    except Exception:
        raise Exception("get_sesion() error.")
    finally:
        await session.close()


async def get_current_user(
    db: AsyncSession = Depends(get_session()),
    token: str = Depends(oauth2_schema),
) -> UserModel:
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User can't be autenticated.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")

        if username is None:
            raise credential_exception
        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credential_exception

    async with db as session:
        result = await session.execute(
            select(UserModel).filter(UserModel.id == int(token_data.username))
        )
        user: UserModel = result.scalars().unique().one_or_none()

        if user is None:
            raise credential_exception
        return user
