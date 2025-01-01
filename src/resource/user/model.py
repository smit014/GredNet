from database.database import Base
from sqlalchemy import Column, String, VARCHAR, Boolean, DateTime, BigInteger
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(VARCHAR(30))
    phone_no = Column(BigInteger)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(VARCHAR(1024), nullable=False)
    spid_no = Column(BigInteger, nullable=True)
    role = Column(String(25), nullable=False,default="alumni")
    is_verify = Column(Boolean, default=False)
    is_plus_member = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())