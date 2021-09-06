from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://czzlruczixygma:d5589fad712202beda0475c16fd876d704c2f30c71cc0ce1b45aeb492816f99f@ec2-34-204-128-77.compute-1.amazonaws.com:5432/d3b8f91fdp5942"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()