from sqlalchemy import Column, Integer, String, Text, JSON
from src.database import Base

class UserProfile(Base):
    __tablename__ = "UserProfile"
    user_id = Column(String(255), primary_key=True)
    name = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    sex = Column(Text, nullable=True)
    interest_list = Column(JSON, nullable=True)