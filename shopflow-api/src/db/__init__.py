"""DB session factory placeholder"""

from typing import Generator


def get_db() -> Generator:
    """Dependency that provides a database session."""
    # Replace with your actual SQLAlchemy session factory
    raise NotImplementedError("Configure your database session in src/db/__init__.py")
    yield  # pragma: no cover
