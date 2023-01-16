import logging

from flask import Blueprint, jsonify

from config import *
from main.post_handler import PostHandler

api_blueprint = Blueprint(
    'api_blueprint',
    __name__,
    url_prefix="/api"
)

api_logger = logging.getLogger('api')
api_logger.setLevel(logging.INFO)
api_file_handler = logging.FileHandler(fr'{LOGGING_PATH}/api.log')
api_file_handler.setLevel(logging.INFO)
file_handler_formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
)
api_file_handler.setFormatter(file_handler_formatter)
api_logger.addHandler(api_file_handler)

post_handler = PostHandler(
    POSTS_JSON_PATH,
    COMMENTS_JSON_PATH,
    BOOKMARK_JSON_PATH
)


@api_blueprint.route('/posts')
def all_posts_request():
    """
    API response for all posts request
    :return: - all posts json
    """
    api_logger.info('api****************************************************')
    api_logger.info('Запрос на получение всех постов')
    all_posts = post_handler.get_posts_all()
    api_logger.info(f'Постов готово к отправке: {len(all_posts)}')
    return jsonify(all_posts)


@api_blueprint.route('/posts/<int:post_pk>')
def post_by_pk_request(post_pk):
    """
    API response for post by pk request
    :param post_pk: - post pk
    :return:        - posts by pk json
    """
    api_logger.info('api****************************************************')
    api_logger.info(f'Запрос на полчение поста по post_pk={post_pk}')
    try:
        post_by_pk = post_handler.get_post_by_pk(post_pk)

    except IndexError as e:
        post_by_pk = {}
        api_logger.exception('IndexError ---------->')
    except ValueError as e:
        post_by_pk = {}
        api_logger.exception('ValueError ---------->')
    api_logger.info(f'Постов готово к отправке: {1 if post_by_pk else 0}')
    return jsonify(post_by_pk)
