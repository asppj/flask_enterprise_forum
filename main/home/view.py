from flask import request, render_template, flash, redirect, url_for
from . import nav_blueprint
from .form import LoginForm


@nav_blueprint.route('/')
def index():
    flash("home", 'info')
    return render_template('home/home.html', title_name='主页')


@nav_blueprint.route('/service')
def service():
    flash("service", 'success')
    flash("service", 'info')
    flash("service", 'danger')
    return render_template('home/service.html', title_name='服务')


@nav_blueprint.route('/about1')
def about1():
    return render_template('home/about.html', title_name='项目一')


@nav_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        print(request)
        if form.validate_on_submit():
            pass
            return redirect(request.args.get('next') or url_for('home.index'))
    return render_template('home/login.html', form=form)
