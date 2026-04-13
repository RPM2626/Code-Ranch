from flask import Blueprint, render_template, request, redirect, url_for
from App.controllers import evaluate_guess, get_history, start_game

views = []
game_views = Blueprint("game_views", __name__)


@game_views.route("/")
def index():
    return render_template("index.html")


@game_views.route("/login")
def login():
    return render_template("login.html")


@game_views.route("/signup")
def signup():
    return render_template("signup.html")


@game_views.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        guess = request.form.get("guess", "").strip()

        if len(guess) == 4 and guess.isdigit():
            result = evaluate_guess(guess)
            if result["bulls"] == 4:
                return redirect(url_for("game_views.win"))

        return redirect(url_for("game_views.game"))

    return render_template("game.html", history=get_history())


@game_views.route("/win")
def win():
    return render_template("win.html")


@game_views.route("/history")
def history_page():
    return render_template("history.html", history=get_history())


@game_views.route("/reset")
def reset_game():
    start_game()
    return redirect(url_for("game_views.game"))


views.append(game_views)
