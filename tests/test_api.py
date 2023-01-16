import requests


def test_all_posts_request():
    response = requests.get('http://127.0.0.1:5000/api/posts')
    type(response.json())
    post_fields = {
        'poster_name',
        'poster_avatar',
        'pic',
        'content',
        'views_count',
        'likes_count',
        'pk'
    }

    assert type(response.json()) == list, 'Тип данных не соответствует ' \
                                          'ожидаемому типу'
    for post in response.json():
        assert set(post.keys()) == post_fields, 'Поля не соответствуют ' \
                                                'требованиям'


def test_posts_by_pk_request():
    pk = 6
    response = requests.get(f'http://127.0.0.1:5000/api/posts/{pk}')

    post_fields = {
        'poster_name',
        'poster_avatar',
        'pic',
        'content',
        'views_count',
        'likes_count',
        'pk'
    }

    assert type(response.json()) == dict, 'Тип данных не соответствует ' \
                                          'ожидаемому типу'
    if pk > 0:
        assert set(response.json().keys()) == post_fields, \
            'Поля не соответствуют требованиям'
    else:
        assert response.json() == {}, \
            'Поля не соответствуют требованиям'
