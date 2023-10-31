from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []

class Task:
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    task_list = [{'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks]
    return jsonify(task_list)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data['title']
    description = data['description']
    completed = data['completed']
    task = Task(title, description, completed)
    tasks.append(task)
    return 'Task added', 201

@app.route('/api/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        return 'Task deleted', 200
    else:
        return 'Task not found', 404

if __name__ == '__main__':
    app.run(debug=True)
