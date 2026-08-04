from backend.database import SessionLocal, engine, Base
from backend.models import User, Project, Task

def seed_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    user = User(name="Ops Lead", email="ops@blinkit.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    project1 = Project(title="Dark Store Ops", owner_id=user.id)
    project2 = Project(title="Engineering Pod B", owner_id=user.id)
    db.add_all([project1, project2])
    db.commit()

    sample_tasks = [
        Task(title="Audit Cold Storage", priority="high", due_date="today", project_id=project1.id),
        Task(title="Restock Shelf 4", priority="medium", due_date="tomorrow", project_id=project1.id),
        Task(title="Fix Scanner App", priority="low", due_date="next friday", project_id=project2.id),
    ]
    db.add_all(sample_tasks)
    db.commit()
    db.close()
    print("Database successfully seeded!")

if __name__ == "__main__":
    seed_database()
