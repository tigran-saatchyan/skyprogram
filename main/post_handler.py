import json
import logging
from json import JSONDecodeError

from config import LOGGING_PATH

# logging.basicConfig(
#     filename=fr'{LOGGING_PATH}/post_handler.log',
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s'
# )


class PostHandler:

    def __init__(self, posts_path, comments_path, bookmarks_path):
        """
        Initiated paths for posts, comments and bookmarks
        :param posts_path:      - path stored in POSTS_JSON_PATH
        :param comments_path:   - path stored in COMMENTS_JSON_PATH
        :param bookmarks_path:  - path stored in BOOKMARK_JSON_PATH
        """
        self.posts_path = posts_path
        self.comments_path = comments_path
        self.bookmarks_path = bookmarks_path

    def __repr__(self):
        return f'posts_path={self.posts_path}, ' \
               f'comments_path={self.comments_path}, ' \
               f'bookmarks_path={self.bookmarks_path}'

    def get_posts_all(self):
        """
        Get all posts
        :return:    - list of all posts
        """
        posts = []
        try:
            with open(self.posts_path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            pass
            # logging.info(f'Ошибка загрузки файла {file.name}')
        return posts

    def get_posts_by_user(self, user_name):
        """
        Get all posts by username (poster_name)
        :param user_name:   - username (poster_name)
        :return:            - list of user posts
        """
        posts = self.get_posts_all()

        user_posts = [
            post
            for post in posts
            if post['poster_name'].lower() == user_name.lower()
        ]

        if not user_posts:
            raise ValueError(f'Пользователь {user_name} отсутствует')

        return user_posts

    def get_comments_from_json(self, post_id):
        """
        Get all comments from json
        :return:    - ist of comments
        """
        try:
            with open(self.comments_path, 'r', encoding='utf-8') as file:
                comments = json.load(file)

        except JSONDecodeError:
            # logging.info(f'Ошибка загрузки файла {file.name}')
            comments = None

        return comments

    def get_comments_by_post_id(self, post_id):
        """
        Get comments by post id
        :param post_id:     - post id
        :return:            - list of comments
        """

        comments = self.get_comments_from_json(post_id)

        user_comments = [
            comment
            for comment in comments
            if comment['post_id'] == post_id
        ]

        if not user_comments:
            user_comments = []
            raise ValueError(f'Отсутствует комментарий с post_id={post_id}')

        return user_comments

    def search_for_posts(self, query):
        """
        Searching for posts
        :param query:   - query to search
        :return:        - posts list containing query in content
        """
        posts = self.get_posts_all()
        posts_found = [
            post
            for post in posts
            if query.lower() in post['content'].lower()
        ]

        return posts_found

    def get_post_by_pk(self, pk):
        """
        Get post by specific PK
        :param pk:  - PK of post on posts.json
        :return:    - post by PK
        """
        posts = self.get_posts_all()
        post_by_pk = [post for post in posts if post['pk'] == pk]
        return post_by_pk[0]
