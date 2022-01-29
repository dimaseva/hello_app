from flask import Blueprint, render_template, redirect
from flask import flash

from .models import User
from .forms import UserForm

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["POST", "GET"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        if User.objects.filter(user_name=form.name.data):
            flash(f"Вже бачилися, {form.name.data}")
        else:
            flash(f"Привіт, {form.name.data}")
            User.objects.create(user_name=form.name.data)
        return redirect("/")
    return render_template("welcome.html", form=form)


@main_blueprint.route("/users")
def users():
    user_list = User.objects.all()
    return render_template("user_list.html", user_list=user_list)
