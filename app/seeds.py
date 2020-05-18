import random
from app.models import Question, Answer

questions_list = [
    {
        'text': 'Nulla aliquet nisl lacinia nisl porta volutpat?',
        'user': '',
    }, {
        'text': 'Morbi velit metus, gravida eget dolor vel, porttitor aliquet est?',
        'user': '',
    }, {
        'text': 'Integer turpis nisl, rhoncus et lacinia eget, mattis ac ante?',
        'user': '',
    }, {
        'text': 'Mauris at massa sit amet libero pulvinar varius et quis nibh?',
        'user': '',
    }, {
        'text': 'Duis sem lorem, convallis vel tempus vestibulum, gravida vitae metus?',
        'user': '',
    }, {
        'text': 'Nam tempus nulla sapien, et aliquet turpis varius sit amet?',
        'user': '',
    }, {
        'text': 'Ut malesuada luctus neque, id dapibus sem ultrices in?',
        'user': '',
    }, {
        'text': 'Vestibulum laoreet turpis eget tincidunt feugiat?',
        'user': '',
    }, {
        'text': 'Aliquam tincidunt bibendum tellus eu imperdiet?',
        'user': '',
    }, {
        'text': 'Nulla facilisi?',
        'user': '',
    }, {
        'text': 'Nulla aliquet nisl lacinia nisl porta volutpat?',
        'user': '',
    }, {
        'text': 'Sed pellentesque enim nec ipsum elementum, ac tincidunt sem iaculis?',
        'user': '',
    }, {
        'text': 'Vestibulum ornare sit amet ipsum id tempus?',
        'user': '',
    }, {
        'text': 'Proin lacinia scelerisque euismod?',
        'user': '',
    }, {
        'text': 'Aenean eu diam suscipit, sodales velit ac, mollis odio?',
        'user': '',
    }, {
        'text': 'Nulla hendrerit, nunc non posuere rhoncus, orci ligula feugiat eros, id aliquam purus mauris egestas ipsum?',
        'user': '',
    }, {
        'text': 'Vivamus hendrerit efficitur diam?',
        'user': '',
    }, {
        'text': 'Ut consequat ornare convallis?',
        'user': '',
    }, {
        'text': 'Aenean commodo dictum odio, vulputate varius enim pellentesque vel?',
        'user': '',
    }, {
        'text': 'Cras eu massa vitae tortor venenatis ultricies eu facilisis nisl?',
        'user': '',
    }, {
        'text': 'Fusce non feugiat lorem?',
        'user': '',
    },
    {
        'text': 'Sed rutrum sem nec orci facilisis porttitor?',
        'user': '',
    }
]

answers_list = [
    {
        'text': 'In porttitor, nunc non vestibulum interdum, nisl odio bibendum purus, quis finibus mauris mauris cursus nibh.',
        'user': ''
    },
    {
        'text': 'Aenean ligula dolor, placerat non lacinia vel, dignissim et risus.',
        'user': '',
    },
    {
        'text': 'Donec ultricies eros ac magna luctus pellentesque.',
        'user': '',
    },
    {
        'text': 'Mauris quis mi ut purus accumsan tempor.',
        'user': '',
    },
    {
        'text': 'Nam eu congue libero, at blandit felis.',
        'user': '',
    },
    {
        'text': 'Etiam ac facilisis tellus.',
        'user': '',
    },
    {
        'text': 'Donec lacus ligula, facilisis ac vestibulum id, pretium ut dui.',
        'user': '',
    },
    {
        'text': 'Aenean scelerisque erat id purus faucibus malesuada.',
        'user': '',
    },
    {
        'text': 'Vestibulum pharetra ultrices nisi, et finibus lectus lobortis sit amet.',
        'user': '',
    },
    {
        'text': 'Pellentesque semper velit sit amet turpis porta feugiat.',
        'user': '',
    },
    {
        'text': 'Suspendisse felis magna, vulputate id luctus pretium, scelerisque vitae enim.',
        'user': '',
    },
    {
        'text': 'Integer quis molestie sapien, ut cursus sem.',
        'user': '',
    },
    {
        'text': 'Maecenas nec dolor ac ante molestie scelerisque.',
        'user': '',
    },
    {
        'text': 'Vestibulum eu dui aliquet, tempor libero id, blandit ex.',
        'user': '',
    },
    {
        'text': 'Curabitur et nisl viverra, vestibulum arcu in, vehicula libero.',
        'user': '',
    },
    {
        'text': 'Sed vitae sem id urna sagittis tempus.',
        'user': '',
    },
    {
        'text': 'Aliquam erat volutpat.',
        'user': '',
    },
    {
        'text': 'Nulla mollis, augue blandit consectetur luctus, lorem sem mollis nulla, sit amet lobortis elit urna vitae leo.',
        'user': '',
    },
    {
        'text': 'Vivamus pulvinar tincidunt nisi, a hendrerit nisi condimentum finibus.',
        'user': '',
    },
    {
        'text': 'Integer iaculis turpis sed ante scelerisque, a egestas tellus molestie.',
        'user': '',
    },
    {
        'text': 'Maecenas posuere urna dolor, id tempus lectus egestas sed.',
        'user': '',
    },
    {
        'text': 'Mauris pellentesque pharetra orci.',
        'user': '',
    },
    {
        'text': 'Maecenas ornare sodales pellentesque.',
        'user': '',
    },
    {
        'text': 'Etiam vel nibh nec massa interdum blandit.',
        'user': '',
    },
    {
        'text': 'Quisque quis maximus est.',
        'user': '',
    },
    {
        'text': 'Duis non interdum mi.',
        'user': '',
    },
    {
        'text': 'Sed viverra, augue at pretium blandit, massa dui pellentesque lectus, varius blandit massa leo ac felis.',
        'user': '',
    },
    {
        'text': 'Duis varius, lorem in aliquet tristique, ex turpis efficitur lectus, id consequat est augue egestas neque.',
        'user': '',
    },
    {
        'text': 'Vivamus nulla mi, tincidunt et orci a, eleifend auctor lectus.',
        'user': '',
    },
    {
        'text': 'Vestibulum finibus lectus eget leo sodales malesuada.',
        'user': '',
    },
    {
        'text': 'Curabitur id convallis nunc.',
        'user': '',
    },
    {
        'text': 'Fusce nec elementum urna, et molestie augue.',
        'user': '',
    },
    {
        'text': 'Fusce viverra ante risus, eget cursus erat congue id.',
        'user': '',
    },
    {
        'text': 'Phasellus ullamcorper pharetra nisi eu pulvinar.',
        'user': '',
    },
    {
        'text': 'Quisque mauris mauris, eleifend quis mollis ac, tristique sed eros.',
        'user': '',
    },
    {
        'text': 'Phasellus lobortis lorem a varius facilisis.',
        'user': '',
    },
    {
        'text': 'Donec sodales dictum ligula lobortis malesuada.',
        'user': '',
    },
    {
        'text': 'Pellentesque eget nulla eget est auctor eleifend.',
        'user': '',
    },
    {
        'text': 'Suspendisse euismod turpis vel nunc elementum, at molestie augue egestas.',
        'user': '',
    },
    {
        'text': 'Cras ullamcorper ex malesuada justo laoreet venenatis.',
        'user': '',
    },
    {
        'text': 'Maecenas purus turpis, placerat semper vulputate vel, bibendum ut orci.',
        'user': '',
    },
    {
        'text': 'Nulla facilisi.',
        'user': '',
    },
    {
        'text': 'Sed semper libero quis eleifend feugiat.',
        'user': '',
    },
    {
        'text': 'Praesent imperdiet non neque eu aliquam.',
        'user': '',
    },
    {
        'text': ' Phasellus ipsum felis, ornare non ligula at, ornare accumsan nisi.',
        'user': '',
    },
    {
        'text': 'Aenean sagittis dictum justo sed tincidunt.',
        'user': '',
    },
    {
        'text': 'Fusce non vestibulum ligula.',
        'user': '',
    },
    {
        'text': 'Curabitur laoreet dolor sed luctus consequat.',
        'user': '',
    },
    {
        'text': 'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.',
        'user': '',
    },
    {
        'text': 'Nulla sed enim non lectus eleifend lobortis a ut nisl.',
        'user': '',
    },
    {
        'text': 'Morbi iaculis libero in enim pharetra, non ultricies elit ornare.',
        'user': '',
    },
    {
        'text': 'Ut ultricies dui eu egestas sodales.',
        'user': '',
    },
    {
        'text': 'Donec lobortis nisi risus, eget laoreet ex convallis quis.',
        'user': '',
    },
    {
        'text': 'Sed id dui eu augue posuere pellentesque.',
        'user': '',
    },
    {
        'text': 'In et ligula tempor risus malesuada elementum.',
        'user': '',
    },
    {
        'text': 'Quisque ligula urna, ullamcorper ut neque at, lacinia semper mauris.',
        'user': '',
    },
    {
        'text': 'Ut egestas sagittis feugiat.',
        'user': '',
    },
    {
        'text': 'Vivamus iaculis, urna vel interdum blandit, massa nisl scelerisque ipsum, non ultrices lorem leo a mauris.',
        'user': '',
    },
    {
        'text': 'Cras sem arcu, egestas ut nibh tempor, venenatis consectetur est.',
        'user': '',
    },
]

users_list = [
    {
        'username': 'Leo Rolland',
        'email': 'leo.rolland@example.com',
    },
    {
        'username': 'Gordon Morris',
        'email': 'gordon.morris@example.com',
    },
    {
        'username': 'Greg Moore',
        'email': 'greg.moore@example.com',
    },
    {
        'username': 'Ayse Kunt',
        'email': 'ayse.kunt@example.com',
    }, {
        'username': 'Juana Mora',
        'email': 'juana.mora@example.com',
    },
    {
        'username': 'Medina Renard',
        'email': 'medina.renard@example.com',
    },
    {
        'username': 'Raymond Jimenez',
        'email': 'raymond.jimenez@example.com',
    },
    {
        'username': 'Shawn Young',
        'email': 'shawn.young@example.com',
    },
    {
        'username': 'Johann Pichler',
        'email': 'johann.pichler@example.com',
    },
    {
        'username': 'Willie Wright',
        'email': 'willie.wright@example.com',
    },
    {
        'username': 'Zoe Morris',
        'email': 'zoe.morris@example.com',
    },
    {
        'username': 'Milan Brunke',
        'email': 'milan.brunke@example.com',
    },
    {
        'username': 'Arturo Ibanez',
        'email': 'arturo.ibanez@example.com',
    },
    {
        'username': 'Alexis Colin',
        'email': 'alexis.colin@example.com',
    },
    {
        'username': 'Jurgen Andre',
        'email': 'jurgen.andre@example.com',
    },
    {
        'username': 'Ryan Wilson',
        'email': 'ryan.wilson@example.com',
    },
    {
        'username': 'Adilson Vlasman',
        'email': 'adilson.vlasman@example.com',
    },
    {
        'username': 'Lily Thompson',
        'email': 'lily.thompson@example.com',
    },
    {
        'username': 'Iracilda Ribeiro',
        'email': 'iracilda.ribeiro@example.com',
    },
    {
        'username': 'Julie Garcia',
        'email': 'julie.garcia@example.com',
    },
    {
        'username': 'Albert Madsen',
        'email': 'albert.madsen@example.com',
    },
    {
        'username': 'Ignacio Calvo',
        'email': 'ignacio.calvo@example.com',
    },
    {
        'username': 'David Butler',
        'email': 'david.butler@example.com',
    },
    {
        'username': 'Emilia Duran',
        'email': 'emilia.duran@example.com',
    },
    {
        'username': 'Leo Karvonen',
        'email': 'leo.karvonen@example.com',
    },
    {
        'username': 'Aatu Wainio',
        'email': 'aatu.wainio@example.com',
    },
    {
        'username': 'Stefano Meyer',
        'email': 'stefano.meyer@example.com',
    },
    {
        'username': 'Eloise Roche',
        'email': 'eloise.roche@example.com',
    },
    {
        'username': 'Natan Pettersson',
        'email': 'natan.pettersson@example.com',
    },
    {
        'username': 'Brooke Gutierrez',
        'email': 'brooke.gutierrez@example.com',
    },
    {
        'username': 'Anina Meunier',
        'email': 'anina.meunier@example.com',
    },
    {
        'username': 'Vicky Moore',
        'email': 'vicky.moore@example.com',
    },
    {
        'username': 'Swrn Rdyy',
        'email': 'swrn.rdyy@example.com',
    },
    {
        'username': 'Barry Otoole',
        'email': 'barry.otoole@example.com',
    },
    {
        'username': 'Henry Ugelstad',
        'email': 'henry.ugelstad@example.com',
    },
    {
        'username': 'Nicolas Garcia',
        'email': 'nicolas.garcia@example.com',
    },
    {
        'username': 'Eren Numanoglu',
        'email': 'eren.numanoglu@example.com',
    },
    {
        'username': 'Leo Niva',
        'email': 'leo.niva@example.com',
    },
    {
        'username': 'Sarah Bonnet',
        'email': 'sarah.bonnet@example.com',
    },
    {
        'username': 'Amelia Morales',
        'email': 'amelia.morales@example.com',
    },
    {
        'username': 'Johan Jensen',
        'email': 'johan.jensen@example.com',
    },
    {
        'username': 'Simona Lopez',
        'email': 'simona.lopez@example.com',
    },
    {
        'username': 'Tilda Todal',
        'email': 'tilda.todal@example.com',
    },
    {
        'username': 'Paulina Laurent',
        'email': 'paulina.laurent@example.com',
    },
    {
        'username': 'Raquel Brun',
        'email': 'raquel.brun@example.com',
    },
    {
        'username': 'Rose Robertson',
        'email': 'rose.robertson@example.com',
    },
    {
        'username': 'Heather Henry',
        'email': 'heather.henry@example.com',
    },
    {
        'username': 'Karla Viken',
        'email': 'karla.viken@example.com',
    },
    {
        'username': 'Dunja Rumpf',
        'email': 'dunja.rumpf@example.com',
    },
    {
        'username': 'Ulku Ozbir',
        'email': 'ulku.ozbir@example.com',
    }
]


def seed_all():
    for item in questions_list:
        num = random.randint(0, len(users_list) - 1)
        question = Question.create(
            text=item['text'], username=users_list[num]['email'])
        print(f'Seeding question `{question.text}`')
        question.save()

        max_answers = random.randint(0, 20)

        for i in range(max_answers):
            a_num = random.randint(0, len(answers_list) - 1)
            num = random.randint(0, len(users_list) - 1)
            answer = Answer.create(
                text=answers_list[a_num]['text'],
                username=users_list[num]['email'],
                question=question
            )
            print(
                f'Seeding answer `{answer.text}` to question `{question.text}`')
            answer.save()

    print('Finished seeding.')
