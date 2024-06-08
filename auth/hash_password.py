from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hashes a password using the bcrypt hashing algorithm.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password.

    Args:
        plain_password (str): The plain text password to verify.
        hashed_password (str): The hashed password to verify against.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return password_context.verify(plain_password, hashed_password)
