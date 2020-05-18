import os
import json
from flask import url_for, request


class TestRoutes:
    headers = {
        'Content-Type': 'application/json',
    }

    questions_list = [
        {
            'text': 'Nulla aliquet nisl lacinia nisl porta volutpat?',
            'user': 'leo.rolland@example.com',
        }, {
            'text': 'Morbi velit metus, gravida eget dolor vel, porttitor aliquet est?',
            'user': 'gordon.morris@example.com',
        }, {
            'text': 'Integer turpis nisl, rhoncus et lacinia eget, mattis ac ante?',
            'user': 'greg.moore@example.com',
        }, {
            'text': 'Mauris at massa sit amet libero pulvinar varius et quis nibh?',
            'user': 'ayse.kunt@example.com',
        }
    ]

    answers_list = [
        {
            'text': 'In porttitor, nunc non vestibulum interdum, nisl odio bibendum purus, quis finibus mauris mauris cursus nibh.',
            'user': 'ulku.ozbir@example.com'
        },
        {
            'text': 'Aenean ligula dolor, placerat non lacinia vel, dignissim et risus.',
            'user': 'dunja.rumpf@example.com',
        },
        {
            'text': 'Donec ultricies eros ac magna luctus pellentesque.',
            'user': 'karla.viken@example.com',
        },
        {
            'text': 'Mauris quis mi ut purus accumsan tempor.',
            'user': 'heather.henry@example.com',
        },
        {
            'text': 'Nam eu congue libero, at blandit felis.',
            'user': 'rose.robertson@example.com',
        },
        {
            'text': 'Etiam ac facilisis tellus.',
            'user': 'raquel.brun@example.com',
        },
        {
            'text': 'Donec lacus ligula, facilisis ac vestibulum id, pretium ut dui.',
            'user': 'paulina.laurent@example.com',
        },
        {
            'text': 'Aenean scelerisque erat id purus faucibus malesuada.',
            'user': 'tilda.todal@example.com',
        },
        {
            'text': 'Vestibulum pharetra ultrices nisi, et finibus lectus lobortis sit amet.',
            'user': 'simona.lopez@example.com',
        },
        {
            'text': 'Pellentesque semper velit sit amet turpis porta feugiat.',
            'user': 'johan.jensen@example.com',
        },
        {
            'text': 'Suspendisse felis magna, vulputate id luctus pretium, scelerisque vitae enim.',
            'user': 'amelia.morales@example.com',
        },
        {
            'text': 'Integer quis molestie sapien, ut cursus sem.',
            'user': 'sarah.bonnet@example.com',
        },
        {
            'text': 'Maecenas nec dolor ac ante molestie scelerisque.',
            'user': 'leo.niva@example.com',
        },
        {
            'text': 'Vestibulum eu dui aliquet, tempor libero id, blandit ex.',
            'user': 'eren.numanoglu@example.com',
        },
        {
            'text': 'Curabitur et nisl viverra, vestibulum arcu in, vehicula libero.',
            'user': 'nicolas.garcia@example.com',
        },
        {
            'text': 'Sed vitae sem id urna sagittis tempus.',
            'user': 'henry.ugelstad@example.com',
        },
        {
            'text': 'Aliquam erat volutpat.',
            'user': 'barry.otoole@example.com',
        }
    ]

    # ==============================================================================

    def test_is_api_running(self, client):
        response = client.get(url_for('home'))
        assert response.status_code == 200

        received_data = json.loads(response.data)
        assert 'status' in received_data
        assert received_data['status'] == 'API running'

    # ==============================================================================

    def test_get_question_list(self, client):
        response = client.get(url_for('question_routes.get_questions_list'))
        print(response.data)
        assert response.status_code == 200

        received_data = json.loads(response.data)
        assert 'questions' in received_data

    # ==============================================================================

    def test_invalid_question_creation(self, client):
        sent_data = {
            'text': 'Lorem ipsum dolor',
        }
        response = client.post(url_for('question_routes.create_question'),
                               data=json.dumps(sent_data),
                               headers=self.headers)

        received_data = json.loads(response.data)
        assert response.status_code == 422
        assert 'errors' in received_data

        assert 'user' in [error['field'] for error in received_data['errors']]

    def test_create_question_successfully(self, client):
        for item in self.questions_list:
            response = client.post(url_for('question_routes.create_question'),
                                   data=json.dumps(item),
                                   headers=self.headers)
            assert response.status_code == 201

            # Verify if Question was created
            received_data = json.loads(response.data)

            # See if 'question' and 'answers' keys exist in the returned JSON
            assert 'question' in received_data
            assert 'answers' in received_data['question']
            assert 'user' in received_data['question']

    def test_answer_question(self, client):
        assert 1 == 1
