from database.database import Base
from sqlalchemy import Column, String, VARCHAR, Boolean, DateTime, BigInteger, ForeignKey
from datetime import datetime
from src.resource.user.model import User


class Organization(Base):
    __tablename__ = "organizations"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey(User.id), nullable=False)
    org_url = Column(String,nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())