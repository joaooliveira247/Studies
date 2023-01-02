from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_passwd(passwd: str, hash_passwd: str) -> bool:
    pwd_context.verify(passwd, hash_passwd)


def gen_hash(passwd: str) -> str:
    return pwd_context.hash(passwd)
