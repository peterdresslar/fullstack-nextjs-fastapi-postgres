from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Migration(Base):
    __tablename__ = "migrations"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

@app.get("/api/python")
def hello_world():
    return {"message": "<p>Hello, World!</p>"}

@app.get("/api/migration")
def get_latest_migration():
    db = SessionLocal()
    latest_migration = db.query(Migration).order_by(Migration.id.desc()).first()
    db.close()
    
    if latest_migration:
        seconds_ago = int((datetime.utcnow() - latest_migration.timestamp).total_seconds())
        return {
            "id": latest_migration.id,
            "seconds_ago": seconds_ago
        }
    else:
        raise HTTPException(status_code=404, detail="No migrations found")

@app.post("/api/migrate")
def create_migration():
    db = SessionLocal()
    new_migration = Migration(timestamp=datetime.utcnow())
    db.add(new_migration)
    db.commit()
    db.refresh(new_migration)
    db.close()
    return {"id": new_migration.id, "timestamp": str(new_migration.timestamp)}