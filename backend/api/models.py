from sqlalchemy import String, Boolean,Integer, Column,Float
from api.database import Base

class Operation(Base):
    __tablename__ = 'operations'


    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String(255), nullable=False)
    result = Column(Float, nullable=False)