import logging

from flask import Flask, render_template, send_from_directory

from api.api import api_blueprint
from main.main import main_blueprint


app = Flask(
    __name__,
    static_folder='static',
    template_folder='template'
)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_500_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
