from flask import Blueprint, redirect, render_template, request

from config import *
from main.utils import set_suffix
from .post_handler import PostHandler, post_handler_logger


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
    Index page shows all posts
    """
    all_posts = post_handler.get_posts_all()
    all_bookmarks = post_handler.get_all_bookmarks()
    bookmark_count = len(
        list(
            {
                post['pk']: post
                for post in all_bookmarks
            }.values()
        )
    )
    for post in all_posts:
        if post in all_bookmarks:
            post['active'] = 'active'
            post['add_remove'] = 'remove'
        else:
            post['add_remove'] = 'add'
    return render_template(
        'index.html',
        all_posts=all_posts,
        bookmark_count=bookmark_count
    )


@main_blueprint.route('/post/<int:post_pk>')
def post_page(post_pk):
    """
    Post page - shows specific post by pk
    """
    post_by_pk_not_found = {
        "poster_name"  : 'FourHundredFour',
        "poster_avatar": "/main/static/img/no_ava.png",
        "pic"          : "/main/static/img/no_pic.webp",
        "content"      : f"Пользователь c post_pk={post_pk} не найден",
        "views_count"  : 404,
        "likes_count"  : 404,
        "pk"           : 0
    }

    no_comments = [
        {
            "post_id"       : 0,
            "commenter_name": "Lord Voldemort",
            "comment"       : f"Ssaeahashathifff sssaeahathireth &#128013;",
            "pk"            : 0
        }
    ]
    all_bookmarks = post_handler.get_all_bookmarks()

    try:
        post = post_handler.get_post_by_pk(post_pk)
        if post in all_bookmarks:
            post['active'] = 'active'
            post['add_remove'] = 'remove'
        else:
            post['add_remove'] = 'add'
        post_comments = post_handler.get_comments_by_post_id(post['pk'])
    except IndexError:
        post = post_by_pk_not_found
        post_comments = no_comments
        post_handler_logger.info(
            'main****************************************************'
        )
        post_handler_logger.exception(
            f'post_pk={post_pk} не существует'
        )
    except ValueError as e:
        post = post_by_pk_not_found
        post_comments = no_comments
        post_handler_logger.info(
            'main****************************************************'
        )
        post_handler_logger.exception('ValueError')

    case_declination = f"{len(post_comments)} коментари" \
                       f"{set_suffix(len(post_comments))}"

    return render_template(
        'post.html',
        post=post,
        post_comments=post_comments,
        case_declination=case_declination
    )


@main_blueprint.route('/user/<username>')
def user_feed_page(username):
    """
    User feed page - shows all posts of user by username
    """
    user_posts = post_handler.get_posts_by_user(username)

    all_bookmarks = post_handler.get_all_bookmarks()
    for post in user_posts:
        if post in all_bookmarks:
            post['active'] = 'active'
            post['add_remove'] = 'remove'
        else:
            post['add_remove'] = 'add'
    if not user_posts:
        user_posts = [
            {
                "poster_name"  : username,
                "poster_avatar": "/main/static/img/no_ava.png",
                "pic"          : "/main/static/img/no_pic.webp",
                "content"      : "Пользователь не найден",
                "views_count"  : 404,
                "likes_count"  : 404,
                "pk"           : 0
            }
        ]

    return render_template(
        'user-feed.html',
        user_posts=user_posts,
        username=username
    )


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    """
    Search page - shows all posts found by specific query/substr
    """
    query = request.args.get('query')
    found_posts = post_handler.search_for_posts(query)
    all_bookmarks = post_handler.get_all_bookmarks()
    for post in found_posts:
        if post in all_bookmarks:
            post['active'] = 'active'
            post['add_remove'] = 'remove'
        else:
            post['add_remove'] = 'add'
    return render_template(
        'search.html',
        found_posts=found_posts
    )


@main_blueprint.route('/tag/<tag>')
def tag_page(tag):
    """
    HashTag page - shows all posts found by specific HashTag
    """
    posts_with_tags = post_handler.get_posts_with_tags(tag)
    all_bookmarks = post_handler.get_all_bookmarks()
    for post in posts_with_tags:
        if post in all_bookmarks:
            post['active'] = 'active'
            post['add_remove'] = 'remove'
        else:
            post['add_remove'] = 'add'
    return render_template(
        'tag.html',
        posts_with_tags=posts_with_tags,
        tag=tag
    )


@main_blueprint.route('/bookmarks')
def bookmark_page():
    """
    Bookmark page - shows all posts added to Bookmarks
    """
    all_bookmarks = post_handler.get_all_bookmarks()
    for post in all_bookmarks:
        post['active'] = 'active'
        post['add_remove'] = 'remove'
    return render_template(
        'bookmarks.html',
        all_bookmarks=all_bookmarks
    )


@main_blueprint.route('/bookmarks/add/<int:pk>')
def add_bookmark_page(pk):
    """
    Add Bookmark view - activates add/remove function
    """
    post_handler.add_remove_bookmark(pk)

    return redirect("/", code=302)


@main_blueprint.route('/bookmarks/remove/<int:pk>')
def remove_bookmark_page(pk):
    """
    Add Bookmark view - activates add/remove function
    """
    post_handler.add_remove_bookmark(pk)

    return redirect("/", code=302)
