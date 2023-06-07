from flask import Flask, render_template, request
import random

app = Flask(__name__)
participants = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/raffle', methods=['POST'])
def raffle():
    name = request.form['name']
    email = request.form['email']
    participants.append({'name': name, 'email': email})
    return 'You have been entered into the raffle!'

@app.route('/draw')
def draw_winner():
    if not participants:
        return 'No participants in the raffle yet.'

    winner = random.choice(participants)
    return f'The winner is: {winner["name"]} ({winner["email"]})'

if __name__ == '__main__':
    app.run(debug=True)

