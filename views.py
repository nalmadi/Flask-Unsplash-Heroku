from flask import Blueprint, render_template
from flask import request
import requests
import os


# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():

    api_key = os.environ.get('UNSPLASH_KEY')
    print(api_key)
    api_response = requests.get('https://api.unsplash.com/photos/random?client_id=' + api_key)

    if api_response.status_code == 200:
        data = api_response.json()
        image_url = data['urls']['regular']
    else:
        image_url = None

    return render_template('index.html', image_url=image_url)



@main_blueprint.route('/conditional')
def conditional():
    user = 'admin'
    return render_template('conditional.html', user=user)


@main_blueprint.route('/loop')
def loop():
    users = ['admin', 'user', 'guest']
    return render_template('loop.html', items=users)


@main_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Logged in as {username}'
    
    return render_template('form.html')