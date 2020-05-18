from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from app.models import Question

question_bp = Blueprint('question_routes', __name__)


@question_bp.route('/')
def get_questions_list():
    result = [item.to_json() for item in Question.get_questions_list()]

    return jsonify({'questions': result}), 200


@question_bp.route('/', methods=['POST'])
def create_question():
    try:
        json = request.get_json()

        errors = []

        username = json.get('user', '')
        text = json.get('text', '')

        if not username:
            errors.append({'field': 'user', 'message': 'User is required.'})

        if not text:
            errors.append({'field': 'text', 'message': 'Text is required.'})

        if errors:
            return jsonify({'errors': errors}), 422

        question = Question.create(username=username, text=text)
        question.save()

        return jsonify({'question': question.to_json()}), 201
    except BadRequest as e:
        return jsonify({
            'errors':
                'Something went wrong! Maybe your JSON is malformed. Please, fix it and try again.'
        }), 400


@question_bp.route('/<int:question_id>/', methods=['PUT', 'PATCH'])
def update_question(question_id):
    question = Question.query.get(question_id)

    # Implement update

    if not question:
        return jsonify({'errors': {'status': 'Question not found.'}}), 404

    return jsonify({'question': question.to_json()}), 200


@question_bp.route('/<int:question_id>/')
def get_question(question_id):
    question = Question.query.get(question_id)

    if not question:
        return jsonify({'errors': {'status': 'Question not found.'}}), 404

    return jsonify({'question': question.to_json()}), 200

