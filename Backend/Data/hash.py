from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)

    # @staticmethod
    # def verify(self,plain_passwd,hashed_password):
    #     pwd_cxt.verify(plain_passwd,hashed_password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)