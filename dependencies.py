from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal


async def get_async_session() -> AsyncSession:
    """
    Provides an asynchronous database session. This function is designed to be used with FastAPI's Depends mechanism
    for dependency injection. It creates a new session, yields it for use in the route, and then closes the session
    once the route is done.

    This function is a context manager, which means it can be used in a 'with' statement. The session is automatically
    closed when the 'with' block is exited, even if an error occurs within the block.

    Returns:
        AsyncSession: The database session.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        await db_session.close()
