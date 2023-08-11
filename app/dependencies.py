from fastapi.security import HTTPBearer
from app.database import SessionLocal


http_credentials = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
