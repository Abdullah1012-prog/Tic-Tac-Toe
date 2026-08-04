from flask import Flask, render_template, request
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        difficulty = request.form['difficulty']

        if not username:
            return render_template('index.html')
        if not difficulty:
            return render_template('index.html')

        if difficulty == 'easy':
            return render_template('easy.html', username=username)
        elif difficulty == 'medium':
            return render_template('medium.html', username=username)
        elif difficulty == 'hard':
            return render_template('hard.html', username=username)


@app.route('/easy', methods=['GET', 'POST'])
def easy():
    return render_template('easy.html')


@app.route('/medium', methods=['GET', 'POST'])
def normal():
    return render_template('medium.html')


@app.route('/hard', methods=['GET', 'POST'])
def hard():
    return render_template('hard.html')