from pymongo import MongoClient
from faker import Faker
import datetime

# Connect to MongoDB
client = MongoClient('localhost', 27017)
client.drop_database('taskUsersDatabase')

db = client['taskUsersDatabase']
taskCollection = db['taskCollection']
usersCollection = db['usersCollection']

# Create Faker object
fake = Faker()

# Create tasks
tasks = [
    {
        '_id': 'TASK001',
        'task': fake.text(max_nb_chars=200),
        'is_completed': fake.boolean(chance_of_getting_true=50),
        'due_date': datetime.datetime.now()
    },
    {
        '_id': 'TASK002',
        'task': fake.text(max_nb_chars=200),
        'is_completed': fake.boolean(chance_of_getting_true=50),
        'due_date': datetime.datetime.now()
    },
    {
        '_id': 'TASK003',
        'task': fake.text(max_nb_chars=200),
        'is_completed': fake.boolean(chance_of_getting_true=50),
        'due_date': datetime.datetime.now()
    },
    {
        '_id': 'TASK004',
        'task': fake.text(max_nb_chars=200),
        'is_completed': fake.boolean(chance_of_getting_true=50),
        'due_date': datetime.datetime.now()
    },
    {
        '_id': 'TASK005',
        'task': fake.text(max_nb_chars=200),
        'is_completed': fake.boolean(chance_of_getting_true=50),
        'due_date': datetime.datetime.now()
    }
]

tasks_dict = {task['_id']: task['task'] for task in tasks}  # Create a dictionary with task id as key and task as value

# Create users
users = [
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'tasks': [
            {'id': 'TASK001', 'description': tasks_dict['TASK001']},  # Add task description
            {'id': 'TASK002', 'description': tasks_dict['TASK002']},
            {'id': 'TASK003', 'description': tasks_dict['TASK003']},
            {'id': 'TASK004', 'description': tasks_dict['TASK004']},
            {'id': 'TASK005', 'description': tasks_dict['TASK005']}
        ]
    },
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'tasks': [
            {'id': 'TASK001', 'description': tasks_dict['TASK001']},
            {'id': 'TASK005', 'description': tasks_dict['TASK005']}
        ]
    },
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'tasks': [
            {'id': 'TASK005', 'description': tasks_dict['TASK005']}
        ]
    }
]

# Insert tasks
taskCollection.insert_many(tasks)
usersCollection.insert_many(users)
