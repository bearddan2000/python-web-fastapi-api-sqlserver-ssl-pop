from fastapi import Depends, FastAPI
import uvicorn

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

import settings
from model import PopModel

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)
app = FastAPI()

# Dependency
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get('/pop')
def get_all(db: Session = Depends(get_db)):
    pops = db.query(PopModel).all()
    results = [
        {
            "id": pop.id,
            "name": pop.name,
            "color": pop.color
        } for pop in pops]

    return {"results": results}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0')
