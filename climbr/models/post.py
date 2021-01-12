from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey

class Post(db.Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    body = Column(String(), nullable=False)
    climbing_route = Column(String(), nullable=False)
    poster_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    # ForeignKeyConstraint(["poster_id"],["user.id"], nullable=False)

    def __init__(self, title, body, climbing_route, poster_id):
        self.title = title
        self.body = body
        self.climbing_route = climbing_route
        self.poster_id = poster_id

    def __repr__(self):
        return '<id {}>'.format(self.id)


# CREATE TABLE POST (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     author_id INTEGER NOT NULL,
#     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     title TEXT NOT NULL,
#     body TEXT NOT NULL,
#     climbing_route TEXT NOT NULL,
#     FOREIGN KEY (author_id) REFERENCES user (id)
# );
