from . import db
from datetime import date

class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    poster = db.Column(db.String(100))
    created_at = db.Column(db.Date)
    
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

        today = date.today()
        created_at = today.strftime("%d/%m/%Y")
        self.created_at = created_at