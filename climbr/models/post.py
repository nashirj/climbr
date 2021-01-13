from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey

class Post(db.Model):
    __tablename__ = 'post'

    uid = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(), nullable=False)
    body = Column(String(), nullable=False)
    climbing_route = Column(String(), nullable=False)
    poster_username = Column(String(), nullable=False)
    poster_uid = Column(Integer, ForeignKey("user.uid"), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    
    def __init__(self, title, body, climbing_route, poster_username, poster_uid):
        self.title = title
        self.body = body
        self.climbing_route = climbing_route
        self.poster_username = poster_username
        self.poster_uid = poster_uid

    def __repr__(self):
        return '<uid {}>'.format(self.uid)
