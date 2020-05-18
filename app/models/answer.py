from datetime import datetime
from typing import Dict
from app.extensions import db


class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(120), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'questions.id'), nullable=False)

    def to_json(self):
        json = {
            'id': self.id,
            'text': self.text,
            'user': self.username,
            'question': self.question.text,
            'questionId': self.question_id,
            'creationDate': self.creationDate.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return json

    @classmethod
    def create(cls, **kwargs: Dict[str, str]):
        text = kwargs.get('text', '')
        username = kwargs.get('username', '')
        question = kwargs.get('question', '')

        item = cls(text=text, username=username, question=question)

        return item

    def save(self):
        db.session.add(self)
        db.session.commit()
