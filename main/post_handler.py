import logging
from json import JSONDecodeError

from config import LOGGING_PATH
from .utils import convert_tags_to_links, read_json, write_json

post_handler_logger = logging.getLogger('main')
post_handler_logger.setLevel(logging.INFO)
post_file_handler = logging.FileHandler(fr'{LOGGING_PATH}/main.log')
post_file_handler.setLevel(logging.INFO)
file_handler_formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
)
post_file_handler.setFormatter(file_handler_formatter)
post_handler_logger.addHandler(post_file_handler)


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
            posts = read_json(self.posts_path)
        except JSONDecodeError:
            post_handler_logger.info(
                'ph****************************************************'
            )
            post_handler_logger.exception('JSONDecodeError')
        return posts

    def get_posts_by_user(self, user_name):
        """
        Get all posts by username (poster_name)
        :param user_name:   - username (poster_name)
        :return:            - list of user posts
        """
        posts = self.get_posts_all()

        user_posts = [
            convert_tags_to_links(post)
            for post in posts
            if post['poster_name'].lower() == user_name.lower()
        ]

        return user_posts

    def get_comments_from_json(self, post_id):
        """
        Get all comments from json
        :return:    - ist of comments
        """
        try:
            comments = read_json(self.comments_path)

        except JSONDecodeError:
            comments = None
            post_handler_logger.info(
                'ph****************************************************'
            )
            post_handler_logger.exception('JSONDecodeError')
        posts = self.get_posts_all()

        post_ids = [
            post['pk']
            for post in posts
        ]

        if post_id not in post_ids:
            raise ValueError(
                f"По такому post_id={post_id} постов не "
                f"обнаружено"
            )

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

        return user_comments

    def search_for_posts(self, query):
        """
        Searching for posts
        :param query:   - query to search
        :return:        - posts list containing query in content
        """
        posts = self.get_posts_all()
        posts_found = [
            convert_tags_to_links(post)
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
        post_by_pk = [convert_tags_to_links(post) for post in posts if
                      post['pk'] == pk]

        return post_by_pk[0]

    def get_posts_with_tags(self, tag):
        posts = self.get_posts_all()
        posts_with_tags = []
        hashtag = '#' + tag
        for post in posts:
            if hashtag in post["content"]:
                posts_with_tags.append(convert_tags_to_links(post))
        return posts_with_tags

    def add_remove_bookmark(self, pk):
        post = self.get_post_by_pk(pk)
        bookmarks = read_json(self.bookmarks_path)
        if post in bookmarks:
            bookmarks.remove(post)
        else:
            bookmarks.append(post)

        write_json(self.bookmarks_path, bookmarks)

    def get_all_bookmarks(self):
        return read_json(self.bookmarks_path)
