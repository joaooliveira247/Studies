from pytz import timezone
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt
from ..models.user_model import UserModel
from ..core.configs import settings
from ..core.security import check_passwd, gen_hash
from pydantic import EmailStr

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PATH}/user/login"
)


async def authenticate(
    email: EmailStr, passwd: str, db: AsyncSession
) -> UserModel | None:
    async with db as session:
        result = await session.execute(
            select(UserModel).filter(UserModel.email == email)
        )

        user: UserModel = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not check_passwd(passwd, user.passwd):
            return None

        return user


def _gen_token(type: str, life_time: timedelta, sub: str) -> str:
    payload = {}
    timezone_sp = timezone("America/Sao_Paulo")
    expire_at = datetime.now(tz=timezone_sp) + life_time

    payload["type"] = type
    payload["exp"] = expire_at
    payload["iat"] = datetime.now(tz=timezone_sp)
    payload["sub"] = str(sub)

    return jwt.encode(
        payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM
    )

def gen_acess_token(sub: str) -> str:
    return _gen_token(
        type="acess_token",
        life_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )

