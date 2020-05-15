from datetime import datetime
from app.extensions import db

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    def to_json(self):
        json = {
            'id': self.id,
            'text': self.text,
            'creationDate': self.creationDate,
        }
        return json