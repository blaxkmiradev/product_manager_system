from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String, default="todo")
    product_id = Column(Integer, ForeignKey("products.id"))
