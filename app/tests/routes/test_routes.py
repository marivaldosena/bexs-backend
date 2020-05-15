import os
import json
from flask import url_for , request


class TestRoutes:
    headers = {
        'Content-Type': 'application/json',
    }

    questions = [{
            'text': 'Nulla aliquet nisl lacinia nisl porta volutpat.',
            'user': 'leo.rolland@example.com',
            '': ''
        }]

    # answers = [{
    #         "text": "My answer",
    #         "user": "another.username",
    #         "creationDate": "2020-01-01 12:00:00"
    #     }]

    # ==============================================================================

    def test_is_api_running(self , client):
        response = client.get(url_for('home'))
        assert response.status_code == 200

        received_data = json.loads(response.data)
        assert 'status' in received_data
        assert received_data['status'] == 'API running'

    # ==============================================================================

    def test_get_question_list(self , client):
        response = client.get(url_for('question_routes.get_questions_list'))
        assert response.status_code == 200

        received_data = json.loads(response.data)
        assert 'questions' in received_data

    # ==============================================================================

    def test_create_question_successfully(self, client):
        response = client.post(url_for('question_routes.create_question'),
                               data=)
        assert response.status_code == 201

        # Verify if Question was created
        received_data = json.loads(response.data)

        # See if 'question' and 'answers' keys exist in the returned JSON
        assert 'question' in received_data
        assert 'answers' in received_data['question']


