from config import *
from main.post_handler import *

post_handler = PostHandler(
    POSTS_JSON_PATH,
    COMMENTS_JSON_PATH,
    BOOKMARK_JSON_PATH

)
print(post_handler)
all_posts = post_handler.get_posts_all()
all_comments = post_handler.get_comments_from_json()


def test_init():
    """
    Returns repr of initiated paths
    """

    assert str(post_handler) == f'posts_path={POSTS_JSON_PATH}, ' \
                                f'comments_path={COMMENTS_JSON_PATH}, ' \
                                f'bookmarks_path={BOOKMARK_JSON_PATH}'


def test_get_posts_all():
    """
    Returns all posts
    """
    try:
        with open(post_handler.posts_path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
    except JSONDecodeError:
        raise FileNotFoundError(f'Ошибка загрузки файла {file.name}')

    assert post_handler.get_posts_all() == posts


def test_get_posts_by_user():
    """
    Returns posts of specified user
    """
    poster_name = 'johnny'
    user_posts = [
        post
        for post in all_posts
        if post['poster_name'] == poster_name
    ]

    assert post_handler.get_posts_by_user(poster_name) == user_posts


def test_get_comments_by_post_id():
    """
    Returns comment by post id
    """
    post_id = 2
    user_comments = [
        comment
        for comment in all_comments
        if comment['post_id'] == post_id
    ]
    assert post_handler.get_comments_by_post_id(post_id) == user_comments


def test_search_for_posts():
    """
    Searching for posts by query
    """
    query = 'погулять'
    posts_found = [
        post
        for post in all_posts
        if query.lower() in post['content'].lower()
    ]
    assert post_handler.search_for_posts(query) == posts_found


def test_get_post_by_pk():
    """
    Returns post by PK
    """
    pk = 2
    post_by_pk = [post for post in all_posts if post['pk'] == pk]
    assert post_handler.get_post_by_pk(pk) == post_by_pk
