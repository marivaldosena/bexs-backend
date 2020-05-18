from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app.models import (
    Question,
    Answer
)

answer_bp = Blueprint('answer_routes', __name__)


@answer_bp.route('/', methods=['POST'])
def answer_question():
    try:
        json = request.get_json()

        errors = []

        username = json.get('user', '')
        text = json.get('text', '')
        question_id = json.get('questionId', '')

        if not username:
            errors.append({'field': 'user', 'message': 'User is required.'})

        if not text:
            errors.append({'field': 'text', 'message': 'Text is required.'})

        if not question_id:
            errors.append(
                {'field': 'questionId', 'message': 'Question ID is required.'})
        else:
            if not isinstance(int(question_id), int):
                errors.append(
                    {'field': 'questionId', 'message': 'Question ID must be a integer.'})

            question = Question.query.get(question_id)

            if not question:
                errors.append(
                    {'field': 'questionId', 'message': 'Question ID is not valid.'})

        if errors:
            return jsonify({'errors': errors}), 422

        answer = Answer.create(question=question, text=text, username=username)
        answer.save()

        return jsonify({'answer': answer.to_json()}), 201

    except BadRequest as bad_e:
        return jsonify({
            'errors':
            'Something went wrong! Maybe your JSON is malformed. Please, fix it and try again.'
        }), 400

    except ValueError as val_e:
        errors.append(
            {'field': 'questionId', 'message': 'Question ID must be a integer.'})

        return jsonify({
            'errors':
            errors
        }), 400
