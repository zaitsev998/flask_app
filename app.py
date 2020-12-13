from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "iliya": generate_password_hash('123'),
    "kirill": generate_password_hash('321'),
    "yar": generate_password_hash('333')
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


@app.route('/profile')
@auth.login_required
def profile():
    return "{}, this is your profile!".format(auth.current_user())


@app.route('/photo/<number>')
@auth.login_required
def photo(number):
    return f'Photo {number}'


@app.route('/shareware')
def shareware():
    return 'Free for all!'


@app.route('/logout')
@auth.login_required
def logout():
    return f"{auth.current_user()} was logout!", 401


@app.route('/requestdata')
def request_data():
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr, request.user_agent)


@app.route('/index_page')
def index_page():
    return render_template('index.html', name='338')


if __name__ == '__main__':
    app.run(debug=True)
