from flask import Flask, render_template
from flask_pymongo import PyMongo
import os
# import subprocess

# Flask app
app = Flask(__name__)


# Configurazione Flask
# Template auto reload
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_URI'] = 'mongodb://localhost:27017/taskUsersDatabase'

# Root directory configuration
root_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(root_dir, 'views')

mongo = PyMongo(app)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/users')
def users_page():
    users = mongo.db.usersCollection.find()
    if users is not None:
        return render_template('users.html', users=users)
    else:
        return "Nessun utente trovato"
    
@app.route('/tasks')
def tasks_page():
    tasks = mongo.db.taskCollection.find()
    if tasks is not None:
        return render_template('tasks.html', tasks=tasks)
    else:
        return "Nessun task trovato"
    
@app.route('/task/<id>')
def task_page(id):
    task = mongo.db.taskCollection.find_one_or_404({'_id': id})
    return render_template('task.html', task=task)

@app.route('/user/<email>')
def user_page(email):
    user = mongo.db.usersCollection.find_one_or_404({'email': email})
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)