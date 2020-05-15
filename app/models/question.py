from datetime import datetime
from app.extensions import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(256), nullable=False)
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)
    answers = db.relationship('Answer', backref='question', lazy=False)

    def to_json(self):
        json = {
            'id': self.id,
            'text': self.text,
            'creationDate': self.creationDate,
            'questions': [item.to_json() for item in self.answers]
        }
        return json


'''
{
    "id": 123,
    "text": "My question",
    "user": "username",
    "creationDate": "2020-01-01 12:00:00",
    "answers": [
        {
            "id": 1234,
            "text": "My answer",
            "user": "another.username",
            "creationDate": "2020-01-01 12:00:00"
        }
    ]
}
'''