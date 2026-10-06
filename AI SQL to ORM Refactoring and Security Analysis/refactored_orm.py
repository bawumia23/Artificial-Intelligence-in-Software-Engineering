import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Declarative Base & Model Definition
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), nullable=False)


# 2. Database Connection & Session Setup via Environment Variables
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "yourpassword")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "example_db")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


# 3. ORM CRUD Functions
def create_tables():
    """Create all defined tables in the database."""
    Base.metadata.create_all(engine)


def create_user(session, username: str, email: str) -> User | None:
    """Create a new user using ORM session management."""
    if not username or not email:
        print("Username and email are required.")
        return None
    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"User '{username}' created successfully.")
        return user
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {e}")
        return None


def get_user_by_username(session, username: str) -> User | None:
    """Retrieve a single user by username."""
    return session.query(User).filter(User.username == username).first()


def update_user_email(session, username: str, new_email: str) -> bool:
    """Update a user's email address."""
    user = get_user_by_username(session, username)
    if not user:
        print(f"User '{username}' not found.")
        return False
    try:
        user.email = new_email
        session.commit()
        print(f"User '{username}' email updated successfully.")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error updating user: {e}")
        return False


def delete_user(session, username: str) -> bool:
    """Delete a user by username."""
    user = get_user_by_username(session, username)
    if not user:
        print(f"User '{username}' not found.")
        return False
    try:
        session.delete(user)
        session.commit()
        print(f"User '{username}' deleted successfully.")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting user: {e}")
        return False


def list_users(session) -> list[User]:
    """List all users in the database."""
    return session.query(User).all()


# Usage Example
if __name__ == "__main__":
    create_tables()
    with SessionLocal() as session:
        new_user = create_user(session, "johndoe", "john@example.com")
        fetched_user = get_user_by_username(session, "johndoe")
        update_user_email(session, "johndoe", "john.new@example.com")
        all_users = list_users(session)
        delete_user(session, "johndoe")
