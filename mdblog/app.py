from flask import Flask
from flask import render_template
from .database import articles

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about_page():
    return render_template("about_page.jinja")

@flask_app.route("/articles/")
def view_articles_page():
    return render_template("articles_page.jinja", articles = articles.items())

@flask_app.route("/admin/")
def view_admin_page():
    return render_template("admin_page.jinja")

@flask_app.route("/article/<int:article_id>")
def view_article_page(article_id):
    article = articles.get(article_id)
    if article:
        return render_template("article_page.jinja", article = article)
    else:
        return render_template("article_not_found.jinja",article_id = article_id)

@flask_app.route("/login/")
def view_login_page():
    return render_template("login_page.jinja")

