from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, validators
from wtforms.fields.simple import SubmitField
from wtforms.validators import Required

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'hWdsd39lg'


# --------------------------- FORMS --------------------------- #

class SearchForm(FlaskForm):
    buscar = StringField('Buscar')
    lupa = SubmitField('<i class="fa fa-search fa-lg">&nbsp;</i>')

class LoginForm(FlaskForm):
    username = StringField('Ingresar usuario', validators=[Required("Campo necesario.")])
    password = PasswordField('Ingresar contraseña', validators=[Required("Campo necesario.")])
    remember = BooleanField('Recordar Inicio de sesión')
    submit = SubmitField('INICIAR SESIÓN')

class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario')
    password = PasswordField('Contrasena')
    confirm_password = PasswordField('Confirmar Contrasena')
    birth_day = SelectField('Dia', choices= ['Seleccione'] + list(range(1, 32)))
    birth_month = SelectField('Mes', choices=['Seleccione','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
    birth_year = SelectField('Año', choices= ['Seleccione'] + list(range(1940,2021)))
    select_sex = SelectField('Sexo', choices=['Seleccione','Masculino', 'Femenino', 'No binario'])
    submit = SubmitField('Confirmar Registro')


# --------------------------- ROUTES --------------------------- #

#INDEX
@app.route('/')
def home():
    return render_template('index.html')

#LOGIN
@app.route('/login/', methods=['POST', 'GET'])
def login():
    search_form = SearchForm()
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # autenticacion
        return redirect(url_for('home'))
    elif search_form.validate_on_submit():
        pass
    return render_template('login.html', form=login_form, search_form=search_form)

#REGISTER
@app.route('/registro/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass 
    else:
        register_form = RegisterForm()
    return render_template('register.html', register_form=register_form)

#PROFILE_USER
@app.route('/perfil/')
def show_user_profile():
    return render_template('perfil_user.html')

#BUSCAR
@app.route('/buscar/<string:movie_name>', methods=['GET'])
def search(movie_name=None):
    return render_template('buscar.html', movie_name=movie_name)

#MOVIE DETAILS
@app.route('/watch/<string:movie>')
def show_movie(movie=None):
    return render_template('movie_detailed.html', movie=movie)

#PRONTO
@app.route('/pronto/', methods=['GET'])
def upcoming_movies():
    return render_template('pronto.html')

#FUNCIONES ADMIN
@app.route('/admin_funciones/', methods=['GET', 'POST'])
def manage_functions():
    if request.method == 'POST':
        pass
    return render_template('funciones.html')

#PELICULAS ADMIN
@app.route('/admin_peliculas/', methods=['GET', 'POST'])
def manage_movies():
    if request.method == 'POST':
        pass
    return render_template('peliculas.html')

#ROL Y USER ADMIN
@app.route('/admin_user/', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        pass
    return render_template('rolyuser.html')