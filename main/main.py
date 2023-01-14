# import logging


from flask import Blueprint, render_template, request

from config import *
from main.utils import set_suffix
from .post_handler import PostHandler

main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    static_folder='static',
    static_url_path='/main/static/',
    template_folder='templates',
    url_prefix="/"
)

post_handler = PostHandler(
    POSTS_JSON_PATH,
    COMMENTS_JSON_PATH,
    BOOKMARK_JSON_PATH
)


@main_blueprint.route('/')
def main_page():
    """
    Index page
    :return:
    """
    all_posts = post_handler.get_posts_all()
    return render_template('index.html', all_posts=all_posts)


@main_blueprint.route('/post/<int:post_pk>')
def post_page(post_pk):
    post_by_pk = post_handler.get_post_by_pk(post_pk)
    post_comments = post_handler.get_comments_by_post_id(post_by_pk['pk'])
    case_declination = f"{len(post_comments)} коментари" \
                       f"{set_suffix(len(post_comments))}"

    return render_template(
        'post.html',
        post_by_pk=post_by_pk,
        post_comments=post_comments,
        case_declination=case_declination
    )


@main_blueprint.route('/user-feed/<username>')
def user_feed_page(username):
    """
    Index page
    :return:
    """
    user_posts = post_handler.get_posts_by_user(username)

    return render_template(
        'user-feed.html',
        user_posts=user_posts,
        username=username
    )


@main_blueprint.route('/search', methods=['GET'])
def search_page():

    query = request.args.get('query')
    found_posts = post_handler.search_for_posts(query)

    return render_template(
        'search.html',
        found_posts=found_posts
    )
