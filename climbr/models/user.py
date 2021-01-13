from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, String

class User(db.Model):
    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True, nullable=False)
    username = Column(String())
    password = Column(String())
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<uid {}>'.format(self.uid)
