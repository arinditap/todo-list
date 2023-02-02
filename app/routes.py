from app import app
from flask import request
from app.controller import Controller

@app.route("/todo", methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        return Controller.home()
    else:
        return Controller.add()


@app.route("/todo/<id>", methods=["GET", "PUT", "DELETE"])
def detailTodo(id):
    if request.method == 'GET':
        return Controller.todo_detail(id)
    elif request.method == 'PUT':
        return Controller.update(id)
    elif request.method == 'DELETE':
        return Controller.delete(id)

#@app.route("/todo/<id>/finish", methods=['GET'])
#def todo_detail(id):
    #todo = Todo.query.filter_by(id=id)

if __name__ == "__main__":
    app.run(debug=True)