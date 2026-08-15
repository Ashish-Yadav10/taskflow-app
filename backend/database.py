from datetime import datetime
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./taskflow.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def ensure_task_created_at_column():
    inspector = inspect(engine)
    if "tasks" not in inspector.get_table_names():
        Base.metadata.create_all(bind=engine)
        return

    columns = [column["name"] for column in inspector.get_columns("tasks")]
    if "created_at" not in columns:
        with engine.begin() as conn:
            conn.execute(text("ALTER TABLE tasks ADD COLUMN created_at VARCHAR"))
            conn.execute(
                text("UPDATE tasks SET created_at = :ts WHERE created_at IS NULL"),
                {"ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
