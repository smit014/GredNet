from database.database import Base
from sqlalchemy import Column, String, VARCHAR, DateTime, BigInteger, Integer
from datetime import datetime


class Data(Base):
    __tablename__ = "datasources"
    spid_no = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(30))
    phone_no = Column(BigInteger)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class OTP(Base):
    __tablename__ = "otps"
    id = Column(String, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    otp =Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
