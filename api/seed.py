from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import Base, Migration
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_migration():
    db = SessionLocal()
    new_migration = Migration(timestamp=datetime.utcnow())
    db.add(new_migration)
    db.commit()
    print(f"Added new migration with ID: {new_migration.id}")
    db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed_migration()
