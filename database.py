from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
"""
Creates an asynchronous engine for the SQLAlchemy ORM. This engine is used to interact with the database.

The engine is created with the URL of the database, which is retrieved from the settings. The 'check_same_thread' 
connect argument is set to False, which allows the engine to be used in a multithreaded environment.

Args:
    SQLALCHEMY_DATABASE_URL (str): The URL of the database.
    connect_args (dict): A dictionary of arguments to pass to the engine's connect method.
"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
"""
Creates a sessionmaker that produces asynchronous sessions. These sessions are used to interact with the database.

The sessionmaker is configured to not automatically commit transactions or flush the session. This gives you more 
control over when these operations occur. The sessionmaker is bound to the engine, which means that sessions produced 
by it will use this engine to interact with the database.

Args:
    autocommit (bool): Whether to automatically commit transactions.
    autoflush (bool): Whether to automatically flush the session.
    bind (Engine): The engine to bind the sessionmaker to.
    class_ (type): The class to use for the sessions produced by the sessionmaker.
"""

Base = declarative_base()
"""
Creates a base class for declarative models. This base class contains a metaclass that produces appropriate 
Table objects from the classes you define.

This base class is used as a base for all ORM models in the application. By inheriting from this base class, 
models gain methods for querying the database, creating, updating, and deleting records, and more.
"""

