
import flask_login
from flask import flash, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash

from classes import User
from connections import app, login_manager


@app.route("/")
def home():
    return render_template(
        "index.html",
    )


@app.route("/data_tables")
def data_tables():
    return render_template("data_tables.html")


# Authentication handling
@login_manager.user_loader
def load_user(user):
    return User.query.get(user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html", login=True)

    email = request.form["email"]
    password = request.form["password"]
    user = User.query.filter_by(user=email).first()

    if not user or not check_password_hash(user.hash, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("login"))

    # If the above check passes, then we know the user has the right credentials
    flask_login.login_user(user)
    return redirect(url_for("home"))


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flask_login.logout_user()
    if request.method == "GET":
        message = "Logged out."
        return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True, threaded=False)
