from flask import Flask, request, render_template

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


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'''
    <h1>Hello World!</h1>
    User-Agent: {user_agent}<br>
    <a href="/profile">/profile</a><br>
    <a href="/login">/login</a>
    '''


@app.route('/login')
def login():
    # do login procedure
    # redirects to /auth oid
    return 'NotImplementedError'


@app.route('/profile')
def profile():
    return render_template('profile.html')
