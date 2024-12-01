from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hasher():
    """Класс для хэширования паролей и их дальнейшей проверки"""

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Проверяет хэши паролей"""
        return password_context.verify((plain_password, hashed_password))

    @staticmethod
    def get_password_hash(password):
        """Хэширует пароль"""
        return password_context.hash(password)
