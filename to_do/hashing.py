from passlib.context import CryptContext
from passlib.utils.decor import deprecated_method

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
