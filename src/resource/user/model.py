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
    address = Column(String(255), nullable=True)
    spid_no = Column(BigInteger, nullable=True)
    is_organization = Column(Boolean, nullable=False)
    is_verify = Column(Boolean, default=False)
    is_plus_member = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())