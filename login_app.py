from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

# Flask globals
#
# current_app (Application context)
# The application instance for the active application.
#
# g (Application context)
# An object that the application can use for temporary storage during the
# handling of a request. This variable is reset with each request.
#
# request (Request context)
# The request object, which encapsulates the contents of an HTTP request sent
# by the client.
#
# session (Request context)
# The user session, a dictionary that the application can use to store values
# that are “remembered” between requests.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret string'
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'''
    <h1>Carafe default dashboard</h1>
    <p>User-Agent: {user_agent}</p>
    <a href="/profile">/profile</a><br>
    <a href="/login">/login</a><br>

    <p>
        <h3>GET-method</h3>
        GET-request transfers data plaintext to server
        <form action="/user" method="get">
            <label for="user">Name:</label>
            <input type="text" name="user"/>
            <input type="submit" value="submit">
        </form>
    </p>
    '''

@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1>''', 404


@app.route('/login')
def login():
    # do login procedure
    # redirects to /auth oid
    return 'NotImplementedError'


@app.route('/profile')
def profile():
    return render_template('profile.html')
    # return render_template('user.html')


@app.route('/user')
def user():
    user = request.args.get('user')
    print(user)
    return render_template('user.html', name=user)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
