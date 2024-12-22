from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base =declarative_base()
Sessionlocal = sessionmaker(bind=engine)
