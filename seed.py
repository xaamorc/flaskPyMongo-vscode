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

# Create users
users = [
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'task': 'TASK001'
    },
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'task': 'TASK002'
    },
    {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
        'task': 'TASK003'
    }
]

# Insert tasks
taskCollection.insert_many(tasks)
usersCollection.insert_many(users)

pipeline = [
    {
        '$lookup': {
            'from': 'taskCollection',
            'localField': 'task',
            'foreignField': '_id',
            'as': 'task_info'
        }
    },
    {
        '$project': {
            '_id': 1,
            'name': 1,
            'task_info': 1
        }
    }
]

result = usersCollection.aggregate(pipeline)

for user in result:
    print(user)
