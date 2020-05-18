from datetime import datetime
from typing import Dict
from app.extensions import db
from sqlalchemy import desc


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(256), nullable=False)
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(120), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=False)

    def to_json(self):
        json = {
            'id': self.id,
            'text': self.text,
            'user': self.username,
            'creationDate': self.creationDate.strftime('%Y-%m-%d %H:%M:%S'),
            'answers': [item.to_json() for item in self.answers],
            'answersQty': len(self.answers),
        }
        return json

    @classmethod
    def create(cls, **kwargs: Dict[str, str]):
        text = kwargs.get('text', '')
        username = kwargs.get('username', '')

        item = cls(text=text, username=username)

        return item

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_questions_list(cls):
        result = cls.query.order_by(desc(cls.creationDate)).all()

        return result
