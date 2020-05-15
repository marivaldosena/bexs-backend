from flask import Blueprint, jsonify, current_app
from app.models import Question

question_bp = Blueprint('question_routes', __name__)

@question_bp.route('/')
def get_questions_list():
    result = [item.to_json() for item in Question.query.all()]

    return jsonify({'questions': result}), 200

@question_bp.route('/', methods=['POST'])
def create_question():
    pass
