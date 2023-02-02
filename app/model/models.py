from app import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #finished_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    complete = db.Column(db.Boolean)